"""Generate deterministic two-group power-planning values for Chapter 22."""
from __future__ import annotations
import csv,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/'data/generated/ch22_sample.csv'
def cdf(x):return .5*(1+math.erf(x/math.sqrt(2)))
def power(d,n,z=1.959963984540054):
    shift=d*math.sqrt(n/2);return cdf(-z-shift)+1-cdf(z-shift)
def build_rows():
    rows=[];sd=4.;mpie=1.
    for d in (.1,.2,.4,.6,.8):
        for n in range(10,201,10):
            p=power(d,n);effect=d*sd
            rows.append({'standardized_effect_d':d,'effect_delivery_days':round(effect,2),'sample_size_per_group':n,'total_sample_size':2*n,'alpha_two_sided':.05,'planned_power':round(p,6),'assumed_sd_days':sd,'minimum_practical_effect_days':mpie,'meets_80_percent_power':'Yes' if p>=.8 else 'No','practically_meaningful':'Yes' if effect>=mpie else 'No'})
    return rows
def main():
    rows=build_rows();OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    with OUTPUT.open('w',newline='',encoding='utf-8') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    print(f'Wrote {len(rows)} rows to {OUTPUT.relative_to(ROOT)}')
if __name__=='__main__':main()
