"""Generate deterministic multilingual message-routing data for Chapter 44."""

import csv
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data/generated/ch44_sample.csv"
ROUTES = ("service", "quality", "finance", "sales")
LANGUAGES = ("id", "en")
CHANNELS = ("email", "portal", "chat")
TRAIN_CONVERSATIONS = 128
TOTAL_CONVERSATIONS = 160
REVIEW_THRESHOLD = 0.68

PHRASES = {
    ("service", "en"): (
        "delivery is late and has not reached our warehouse",
        "please trace the delayed shipment and confirm arrival",
        "our order is missing after the promised delivery date",
        "the carrier has not delivered the cartons",
        "when will the overdue shipment arrive",
        "we need an update on the delivery delay",
    ),
    ("service", "id"): (
        "pengiriman terlambat dan belum tiba di gudang kami",
        "mohon lacak kiriman dan konfirmasi waktu kedatangan",
        "pesanan belum diterima setelah tanggal yang dijanjikan",
        "kurir belum mengantar karton ke gudang",
        "kapan kiriman yang terlambat akan tiba",
        "kami perlu kabar tentang keterlambatan pengiriman",
    ),
    ("quality", "en"): (
        "cartons arrived damaged and several seals are broken",
        "the product smells unusual and needs quality review",
        "please investigate the leaking packages in this batch",
        "we found crushed cartons during receiving inspection",
        "the batch colour differs from the approved sample",
        "damaged goods require replacement and investigation",
    ),
    ("quality", "id"): (
        "karton tiba dalam kondisi rusak dan segelnya terbuka",
        "produk berbau tidak biasa dan perlu pemeriksaan mutu",
        "mohon periksa kemasan bocor pada batch ini",
        "kami menemukan karton penyok saat penerimaan",
        "warna batch berbeda dari sampel yang disetujui",
        "barang rusak perlu diganti dan diselidiki",
    ),
    ("finance", "en"): (
        "the invoice total does not match our purchase order",
        "please send a copy of the outstanding credit note",
        "our payment was posted against the wrong invoice",
        "we need the tax invoice for last month's shipment",
        "the account statement shows an unexplained balance",
        "please confirm receipt of the bank transfer",
    ),
    ("finance", "id"): (
        "jumlah faktur tidak sesuai dengan pesanan pembelian",
        "mohon kirim salinan nota kredit yang belum diterima",
        "pembayaran kami dicatat pada faktur yang salah",
        "kami membutuhkan faktur pajak untuk kiriman bulan lalu",
        "laporan akun menunjukkan saldo yang tidak jelas",
        "mohon konfirmasi penerimaan transfer bank",
    ),
    ("sales", "en"): (
        "please quote prices for the new coffee catalogue",
        "we want to place an order for the seasonal range",
        "send product availability and minimum order quantities",
        "can your sales team discuss distributor pricing",
        "please share the latest catalogue and promotion terms",
        "we need a quotation for twelve pallets of noodles",
    ),
    ("sales", "id"): (
        "mohon kirim harga untuk katalog kopi terbaru",
        "kami ingin memesan rangkaian produk musiman",
        "kirim ketersediaan produk dan jumlah pesanan minimum",
        "bisakah tim penjualan membahas harga distributor",
        "mohon bagikan katalog dan syarat promosi terbaru",
        "kami memerlukan penawaran untuk dua belas palet mi",
    ),
}

# Later messages contain realistic overlap; the first topic remains the routing label.
AMBIGUOUS = {
    "service": "the invoice is ready but the delivery is still late",
    "quality": "thank you for replacing the damaged cartons",
    "finance": "the shipment arrived but the invoice amount is wrong",
    "sales": "after the quality review please quote the replacement order",
}


def build_documents():
    start = datetime(2026, 1, 5, 8, tzinfo=timezone.utc)
    rows = []
    for conversation in range(TOTAL_CONVERSATIONS):
        route = ROUTES[conversation % len(ROUTES)]
        language = LANGUAGES[(conversation // len(ROUTES)) % len(LANGUAGES)]
        phrase_bank = PHRASES[(route, language)]
        for turn in range(2):
            phrase = phrase_bank[(conversation // 8 + turn) % len(phrase_bank)]
            if conversation >= 144 and turn == 1:
                phrase = AMBIGUOUS[route]
                language = "en"
            timestamp = start + timedelta(hours=18 * conversation + turn)
            split = "train" if conversation < TRAIN_CONVERSATIONS else "test"
            rows.append(
                {
                    "message_id": f"M44-{len(rows) + 1:03d}",
                    "conversation_id": f"C44-{conversation + 1:03d}",
                    "message_timestamp_utc": timestamp.isoformat().replace("+00:00", "Z"),
                    "language": language,
                    "channel": CHANNELS[conversation % len(CHANNELS)],
                    "redaction_status": "synthetic_no_personal_data",
                    "route_label": route,
                    "split": split,
                    "message_text": phrase,
                }
            )
    return rows


def add_model_outputs(rows):
    train = [r for r in rows if r["split"] == "train"]
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=2, sublinear_tf=True)
    x_train = vectorizer.fit_transform([r["message_text"] for r in train])
    model = LogisticRegression(max_iter=1000, random_state=44).fit(
        x_train, [r["route_label"] for r in train]
    )
    probabilities = model.predict_proba(vectorizer.transform([r["message_text"] for r in rows]))
    predictions = model.classes_[probabilities.argmax(axis=1)]
    confidence = probabilities.max(axis=1)
    for row, prediction, score in zip(rows, predictions, confidence):
        row["predicted_route"] = str(prediction)
        row["confidence"] = f"{score:.6f}"
        row["review_required"] = "1" if score < REVIEW_THRESHOLD else "0"
        row["correct_prediction"] = "1" if prediction == row["route_label"] else "0"
    return rows


def main():
    rows = add_model_outputs(build_documents())
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
