"""Decision utilities for assessing deep-learning proposals."""
def annual_value(cases,baseline_error,candidate_error,value_per_correct):
 if cases<0 or not 0<=candidate_error<=1 or not 0<=baseline_error<=1 or value_per_correct<0: raise ValueError("invalid value inputs")
 return float(cases*(baseline_error-candidate_error)*value_per_correct)
def annual_cost(training_runs,training_cost,inferences,inference_cost,engineering_cost):
 vals=[training_runs,training_cost,inferences,inference_cost,engineering_cost]
 if any(v<0 for v in vals): raise ValueError("cost inputs cannot be negative")
 return float(training_runs*training_cost+inferences*inference_cost+engineering_cost)
def net_value(value,cost): return float(value-cost)
def readiness_score(data,baseline,operations,governance):
 vals=[data,baseline,operations,governance]
 if any(not 0<=v<=1 for v in vals): raise ValueError("readiness dimensions must be in [0,1]")
 return float(min(vals))
def recommend(net_incremental_value,readiness,minimum_readiness=.6):
 return "pilot" if net_incremental_value>0 and readiness>=minimum_readiness else "simpler-baseline"
