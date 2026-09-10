"""Generate the deterministic Chapter 33 evaluation-window ledger."""
import csv
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/"data/generated/ch33_sample.csv"

def build_rows():
    windows=[
        ("cv_1","validation","2024-01-01","2024-05-31","2024-07-01","2024-07-31",2480,430,0.142,18800,0.78,54),
        ("cv_2","validation","2024-01-01","2024-09-30","2024-11-01","2024-11-30",4210,470,0.149,17600,0.81,57),
        ("cv_3","validation","2024-01-01","2025-01-31","2025-03-03","2025-03-31",5870,510,0.157,18100,0.80,64),
        ("cv_4","validation","2024-01-01","2025-05-31","2025-07-01","2025-07-31",7540,525,0.166,19300,0.79,69),
        ("final_test","test","2024-01-01","2025-12-01","2026-01-01","2026-03-31",10240,1620,0.171,20100,0.77,226),
    ]
    return [{"window_id":w[0],"evaluation_role":w[1],"train_start":w[2],"train_end":w[3],"gap_days":30,"evaluation_start":w[4],"evaluation_end":w[5],"train_shipments":w[6],"evaluation_shipments":w[7],"late_rate":f"{w[8]:.3f}","expected_loss_idr":w[9],"late_recall":f"{w[10]:.2f}","false_alerts":w[11]} for w in windows]

def main():
    rows=build_rows();OUT.parent.mkdir(parents=True,exist_ok=True)
    with OUT.open("w",newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=rows[0]);writer.writeheader();writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {OUT.relative_to(ROOT)}")

if __name__=="__main__":main()
