"""Tree-ensemble helpers used by Chapter 37."""
from __future__ import annotations
import numpy as np
from sklearn.base import clone
from sklearn.inspection import permutation_importance
from sklearn.metrics import mean_absolute_error, roc_auc_score


def validate_xy(features, target):
    x=np.asarray(features,dtype=float); y=np.asarray(target)
    if x.ndim!=2 or len(x)==0 or len(x)!=len(y): raise ValueError("features and target must align")
    if not np.isfinite(x).all(): raise ValueError("features must be finite")
    return x,y


def fit_with_seed(model, features, target, seed=37):
    x,y=validate_xy(features,target); fitted=clone(model)
    if "random_state" in fitted.get_params(): fitted.set_params(random_state=seed)
    return fitted.fit(x,y)


def regression_report(model, features, target):
    x,y=validate_xy(features,target); pred=model.predict(x)
    return {"mae":float(mean_absolute_error(y,pred)),"prediction_min":float(np.min(pred)),"prediction_max":float(np.max(pred))}


def classification_report(model, features, target, threshold=.5):
    x,y=validate_xy(features,target)
    if not 0<=threshold<=1 or not set(np.unique(y))<={0,1}: raise ValueError("binary target and valid threshold required")
    p=model.predict_proba(x)[:,1]; hat=p>=threshold
    tp=int(np.sum((y==1)&hat)); fp=int(np.sum((y==0)&hat)); fn=int(np.sum((y==1)&~hat)); tn=int(np.sum((y==0)&~hat))
    return {"roc_auc":float(roc_auc_score(y,p)),"tn":tn,"fp":fp,"fn":fn,"tp":tp,"alerts":int(hat.sum())}


def permutation_scores(model, features, target, scoring, repeats=5, seed=37):
    x,y=validate_xy(features,target)
    if repeats<=0: raise ValueError("repeats must be positive")
    result=permutation_importance(model,x,y,scoring=scoring,n_repeats=repeats,random_state=seed)
    return result.importances_mean.tolist()


def leaf_profile(model):
    if not hasattr(model,"tree_"): raise ValueError("model is not a fitted single decision tree")
    tree=model.tree_; leaves=tree.children_left==tree.children_right
    return {"depth":int(model.get_depth()),"leaves":int(model.get_n_leaves()),"smallest_leaf":int(tree.n_node_samples[leaves].min())}
