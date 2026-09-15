"""Template only: calibrate on one processed cohort and validate on another."""
import numpy as np
from pdac_model.human_data import load_processed_csv
from pdac_model.calibration import fit_weights,predict,metrics
train=load_processed_csv('data/calibration_cohort.csv')
test=load_processed_csv('data/external_validation_cohort.csv')
cols=['GPX4_proxy','ROS_proxy','Fe2_proxy']
Xtr=train[cols].to_numpy(float); ytr=train['death_fraction'].to_numpy(float)
Xte=test[cols].to_numpy(float); yte=test['death_fraction'].to_numpy(float)
w,_,ok=fit_weights(Xtr,ytr)
if not ok: raise RuntimeError('calibration failed')
print('locked weights:',w)
print('external metrics:',metrics(yte,predict(Xte,w)))
