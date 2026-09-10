"""Generate the deterministic Chapter 31 transformation ledger."""
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/"data/generated/ch31_sample.csv"
def build_rows():
 return [
  {"step_order":1,"step":"Validate source schema","input_rows":10240,"output_rows":10240,"affected_values":0,"status":"passed","audit_note":"Required raw columns present; snapshot hash retained"},
  {"step_order":2,"step":"Standardise order ID","input_rows":10240,"output_rows":10240,"affected_values":83,"status":"passed","audit_note":"Trim and uppercase; raw identifier retained"},
  {"step_order":3,"step":"Parse quantity","input_rows":10240,"output_rows":10240,"affected_values":10118,"status":"warning","audit_note":"122 placeholders or invalid forms flagged; none changed to zero"},
  {"step_order":4,"step":"Map city","input_rows":10240,"output_rows":10240,"affected_values":417,"status":"warning","audit_note":"Versioned mapping applied; 6 unknown values preserved"},
  {"step_order":5,"step":"Preserve currency","input_rows":10240,"output_rows":10240,"affected_values":10240,"status":"passed","audit_note":"IDR, AED, and USD amounts retained; conversion requires a dated rate"},
  {"step_order":6,"step":"Parse declared dates","input_rows":10240,"output_rows":10240,"affected_values":10240,"status":"passed","audit_note":"Approved formats and source timezones only"},
  {"step_order":7,"step":"Select latest revision","input_rows":10240,"output_rows":9870,"affected_values":370,"status":"passed","audit_note":"Highest valid revision selected deterministically"},
  {"step_order":8,"step":"Validate final schema","input_rows":9870,"output_rows":9870,"affected_values":0,"status":"passed","audit_note":"No blocking failures; analysis-ready snapshot hashed"},
 ]
def main():
 rows=build_rows();OUT.parent.mkdir(parents=True,exist_ok=True)
 with OUT.open("w",newline="",encoding="utf-8") as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
 print(f"Wrote {len(rows)} rows to {OUT.relative_to(ROOT)}")
if __name__=="__main__":main()
