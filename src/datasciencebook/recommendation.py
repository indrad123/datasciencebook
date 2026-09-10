"""Recommendation and ranking helpers for Chapter 43."""
import numpy as np

def interaction_matrix(values):
    x=np.asarray(values,float)
    if x.ndim!=2 or min(x.shape)<2 or not np.isfinite(x).all() or np.any(x<0):raise ValueError("interactions must be a non-negative finite matrix")
    return x

def popularity_scores(values):return interaction_matrix(values).sum(0)

def latent_scores(values,factors=2):
    x=interaction_matrix(values)
    if not isinstance(factors,int) or not 1<=factors<min(x.shape):raise ValueError("invalid factor count")
    u,s,vt=np.linalg.svd(x,full_matrices=False);return (u[:,:factors]*s[:factors])@vt[:factors]

def rank_unseen(scores,seen,k):
    s=np.asarray(scores,float);mask=np.asarray(seen,bool)
    if s.ndim!=1 or mask.shape!=s.shape or not np.isfinite(s).all() or not isinstance(k,int) or not 1<=k<=int((~mask).sum()):raise ValueError("invalid scores seen mask or k")
    adjusted=s.copy();adjusted[mask]=-np.inf;return np.argsort(-adjusted,kind="stable")[:k]

def precision_recall_at_k(relevant,ranked,k):
    rel=set(relevant);r=list(ranked)
    if not rel or not isinstance(k,int) or not 1<=k<=len(r):raise ValueError("invalid relevance or k")
    hits=sum(i in rel for i in r[:k]);return hits/k,hits/len(rel)

def ndcg_at_k(relevant,ranked,k):
    rel=set(relevant);r=list(ranked)
    if not rel or not 1<=k<=len(r):raise ValueError("invalid relevance or k")
    dcg=sum((1 if item in rel else 0)/np.log2(pos+2) for pos,item in enumerate(r[:k]));ideal=sum(1/np.log2(pos+2) for pos in range(min(k,len(rel))));return float(dcg/ideal)
