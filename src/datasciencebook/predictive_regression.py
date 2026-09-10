"""Small linear and logistic regression utilities for Chapter 36."""
from __future__ import annotations
import math


def _matrix(rows):
    x=[list(map(float,r)) for r in rows]
    if not x or not x[0] or any(len(r)!=len(x[0]) for r in x): raise ValueError("features must be a non-empty rectangular matrix")
    return x


def standardize_fit(rows):
    x=_matrix(rows); n=len(x); p=len(x[0])
    means=[sum(r[j] for r in x)/n for j in range(p)]
    scales=[]
    for j in range(p):
        s=(sum((r[j]-means[j])**2 for r in x)/n)**0.5
        scales.append(s if s>0 else 1.0)
    return means,scales


def standardize_apply(rows,means,scales):
    x=_matrix(rows)
    if len(means)!=len(x[0]) or len(scales)!=len(x[0]) or any(s<=0 for s in scales): raise ValueError("invalid standardization parameters")
    return [[(v-means[j])/scales[j] for j,v in enumerate(r)] for r in x]


def linear_fit(rows,target,learning_rate=0.05,steps=2000,l2=0.0):
    x=_matrix(rows); y=list(map(float,target))
    if len(x)!=len(y) or not y or learning_rate<=0 or steps<=0 or l2<0: raise ValueError("invalid fitting inputs")
    n,p=len(x),len(x[0]); w=[0.0]*p; b=sum(y)/n
    for _ in range(steps):
        e=[b+sum(w[j]*r[j] for j in range(p))-a for r,a in zip(x,y)]
        b-=learning_rate*2*sum(e)/n
        for j in range(p): w[j]-=learning_rate*(2*sum(e[i]*x[i][j] for i in range(n))/n+2*l2*w[j])
    return b,w


def linear_predict(rows,intercept,coefficients):
    x=_matrix(rows)
    if len(coefficients)!=len(x[0]): raise ValueError("coefficient count does not match")
    return [intercept+sum(c*v for c,v in zip(coefficients,r)) for r in x]


def logistic(value):
    if value>=0:
        z=math.exp(-value); return 1/(1+z)
    z=math.exp(value); return z/(1+z)


def logistic_fit(rows,target,learning_rate=0.1,steps=2500,l2=0.0):
    x=_matrix(rows); y=list(target)
    if len(x)!=len(y) or not y or not set(y)<={0,1,False,True} or learning_rate<=0 or steps<=0 or l2<0: raise ValueError("invalid fitting inputs")
    n,p=len(x),len(x[0]); w=[0.0]*p; prevalence=sum(y)/n; b=math.log((prevalence+1e-6)/(1-prevalence+1e-6))
    for _ in range(steps):
        pr=[logistic(b+sum(w[j]*r[j] for j in range(p))) for r in x]
        e=[pr[i]-y[i] for i in range(n)]
        b-=learning_rate*sum(e)/n
        for j in range(p): w[j]-=learning_rate*(sum(e[i]*x[i][j] for i in range(n))/n+l2*w[j])
    return b,w


def probability_predict(rows,intercept,coefficients):
    return [logistic(v) for v in linear_predict(rows,intercept,coefficients)]


def mean_absolute_error(actual,predicted):
    a=list(actual); p=list(predicted)
    if len(a)!=len(p) or not a: raise ValueError("inputs must have equal non-zero length")
    return sum(abs(float(x)-float(y)) for x,y in zip(a,p))/len(a)


def log_loss(actual,probabilities,epsilon=1e-15):
    y=list(actual); p=list(probabilities)
    if len(y)!=len(p) or not y or not set(y)<={0,1,False,True} or any(v<0 or v>1 for v in p): raise ValueError("invalid probability inputs")
    return -sum(a*math.log(min(max(q,epsilon),1-epsilon))+(1-a)*math.log(1-min(max(q,epsilon),1-epsilon)) for a,q in zip(y,p))/len(y)
