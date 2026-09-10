"""Generate the Chapter 12 natural-frequency Bayes table."""
from __future__ import annotations
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "data/generated/ch12_sample.csv"

def build_rows():
    total=1000
    cells=[("defective","alert",18,20,67),("defective","no_alert",2,20,933),("sound","alert",49,980,67),("sound","no_alert",931,980,933)]
    rows=[]
    for quality,signal,count,quality_total,signal_total in cells:
        rows.append({
            "quality_status":quality,"camera_signal":signal,"carton_count":count,"total_cartons":total,
            "quality_group_total":quality_total,"signal_group_total":signal_total,"joint_probability":count/total,
            "signal_given_quality":count/quality_total,"quality_given_signal":count/signal_total,
            "posterior_defect_if_alert":18/67 if signal=="alert" else 2/933,
        })
    return rows

def main():
    rows=build_rows(); OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    with OUTPUT.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    print(f"Wrote {len(rows)} rows to {OUTPUT.relative_to(ROOT)}")
if __name__=="__main__": main()
