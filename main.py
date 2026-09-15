from pathlib import Path
import csv, numpy as np
import matplotlib.pyplot as plt
from pdac_model.core import phi_death
from pdac_model.sensitivity import lhs,prcc,bootstrap_prcc,sobol_jansen
from pdac_model.spatial import stroma_map,diffuse_2d
from pdac_model.dynamics import simulate_ode,simulate_sde
from pdac_model.optimization import optimize_schedule
from pdac_model.calibration import fit_weights,predict,metrics
OUT=Path(__file__).parent/'outputs'; OUT.mkdir(exist_ok=True)
BOUNDS=[(5e-9,40e-9),(10e-9,80e-9),(.01,.8),(10.,90.),(5.,50.)]
NAMES=['r_H','xi','GPX4','ROS','Fe2']
def model(M): return np.array([phi_death(g,r,f,rh,xi) for rh,xi,g,r,f in M])
def run():
    X=lhs(BOUNDS,1500,42); y=model(X); pc,pv=prcc(X,y); lo,hi=bootstrap_prcc(X,y,250,43)
    s1,st=sobol_jansen(model,BOUNDS,4096,44)
    with open(OUT/'sensitivity_results.csv','w',newline='') as f:
        w=csv.writer(f); w.writerow(['parameter','PRCC','CI95_low','CI95_high','p_value','Sobol_S1','Sobol_ST'])
        for row in zip(NAMES,pc,lo,hi,pv,s1,st): w.writerow(row)
    x,Xg,Yg,xi,D=stroma_map(); conc,sim_s=diffuse_2d(D,steps=400,dx_um=x[1]-x[0])
    t=np.linspace(0,7,281); ode=simulate_ode(t); sde=simulate_sde(t)
    doses,obj,ok=optimize_schedule()
    rng=np.random.default_rng(7); C=np.c_[rng.uniform(.05,.5,120),rng.uniform(20,80,120),rng.uniform(10,40,120)]
    true=(1.5,.8,1.2); from pdac_model.core import ferroptosis_score,death_probability
    yy=death_probability(np.array([ferroptosis_score(*row,true) for row in C]),75,15)+rng.normal(0,.02,120); yy=np.clip(yy,0,1)
    tr=np.arange(80); te=np.arange(80,120); ww,mse,success=fit_weights(C[tr],yy[tr]); mm=metrics(yy[te],predict(C[te],ww))
    with open(OUT/'benchmark_metrics.csv','w',newline='') as f:
        w=csv.writer(f); w.writerow(['benchmark','value']); w.writerow(['synthetic_calibration_only',1]); w.writerow(['fit_success',int(success)]); w.writerow(['train_mse',mse]); [w.writerow([k,v]) for k,v in mm.items()]
    fig,ax=plt.subplots(2,2,figsize=(13,10))
    im=ax[0,0].imshow(D,extent=[0,100,0,100],origin='lower'); ax[0,0].set(title='A. Heterogeneous stromal diffusion',xlabel='x (µm)',ylabel='y (µm)'); fig.colorbar(im,ax=ax[0,0],label='D_eff (µm²/s)')
    z=np.arange(5); width=.38; ax[0,1].bar(z-width/2,s1,width,label='S1'); ax[0,1].bar(z+width/2,st,width,label='ST'); ax[0,1].set_xticks(z,NAMES); ax[0,1].set(title='B. Computed Sobol sensitivity',ylabel='Sobol index'); ax[0,1].legend(); ax[0,1].axhline(0,lw=.7)
    ax[1,0].plot(t,ode[:,2],label='ODE LPO'); ax[1,0].plot(t,sde[:,2],alpha=.8,label='SDE LPO'); ax[1,0].set(title='C. Ferroptosis dynamics',xlabel='Time (days)',ylabel='Lipid peroxidation state'); ax[1,0].legend()
    ax[1,1].bar(np.arange(1,8),doses); ax[1,1].set(title=f'D. Optimized schedule (success={ok})',xlabel='Day',ylabel='Dose (model units)')
    fig.tight_layout(); fig.savefig(OUT/'v4_integrated_analysis.png',dpi=300); plt.close(fig)
    fig,ax=plt.subplots(figsize=(6,5)); im=ax.imshow(conc,extent=[0,100,0,100],origin='lower'); fig.colorbar(im,ax=ax,label='Normalized concentration'); ax.set(title=f'2-D diffusion-reaction prototype, t={sim_s:.2f} s',xlabel='x (µm)',ylabel='y (µm)'); fig.tight_layout(); fig.savefig(OUT/'spatial_concentration.png',dpi=300); plt.close(fig)
    return pc,s1,st,doses,mm
if __name__=='__main__':
    pc,s1,st,doses,mm=run(); print('PRCC',pc); print('Sobol S1',s1); print('Sobol ST',st); print('doses',doses); print('synthetic holdout',mm)
