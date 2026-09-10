"""Generate deterministic probability-distribution teaching values for Chapter 18."""
from __future__ import annotations
import csv,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/'data/generated/ch18_sample.csv'
def normal_cdf(x,mu,s):return .5*(1+math.erf((x-mu)/(s*math.sqrt(2))))
def build_rows():
    rows=[]
    def add(family,kind,x,v,cdf,p1,p2='',support=''):
        rows.append({'distribution':family,'variable_type':kind,'x':x,'mass_or_density':round(v,8),'cumulative_probability':round(cdf,8),'parameter_1':p1,'parameter_2':p2,'support':support})
    c=0
    for x in range(11):
        v=math.comb(10,x)*.2**x*.8**(10-x);c+=v;add('Binomial','Discrete',x,v,c,'n=10','p=0.2','0 through 10')
    c=0
    for x in range(13):
        v=math.exp(-2)*2**x/math.factorial(x);c+=v;add('Poisson','Discrete',x,v,c,'lambda=2','','non-negative integers')
    for x in [i/2 for i in range(21)]:add('Uniform','Continuous',x,.1,min(max(x/10,0),1),'a=0','b=10','0 through 10')
    for x in range(55,146,5):
        v=math.exp(-.5*((x-100)/15)**2)/(15*math.sqrt(2*math.pi));add('Normal','Continuous',x,v,normal_cdf(x,100,15),'mu=100','sigma=15','all real values')
    for x in [i/2 for i in range(21)]:
        v=.5*math.exp(-.5*x);add('Exponential','Continuous',x,v,1-math.exp(-.5*x),'rate=0.5','','zero and above')
    return rows
def main():
    rows=build_rows();OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    with OUTPUT.open('w',newline='',encoding='utf-8') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    print(f'Wrote {len(rows)} rows to {OUTPUT.relative_to(ROOT)}')
if __name__=='__main__':main()
