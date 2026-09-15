"""Human-data adapters.

No patient-level controlled data are bundled. This module accepts processed,
non-identifying tables exported from approved public repositories.
"""
import pandas as pd
REQUIRED=('GPX4_proxy','ROS_proxy','Fe2_proxy','death_fraction')
def load_processed_csv(path):
    df=pd.read_csv(path); missing=[c for c in REQUIRED if c not in df.columns]
    if missing: raise ValueError(f"missing columns: {missing}")
    return df

def robust_scale_train_test(train,test,cols=('GPX4_proxy','ROS_proxy','Fe2_proxy')):
    a=train.copy(); b=test.copy()
    for c in cols:
        med=a[c].median(); q=a[c].quantile(.75)-a[c].quantile(.25); q=q if q>0 else 1.
        a[c]=(a[c]-med)/q; b[c]=(b[c]-med)/q
    return a,b
