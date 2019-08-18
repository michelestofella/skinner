# =============================================================================
# 
# Deuterium Uptake
# Function to evaluate deuterium uptake is implemented
# Evaluated deuterium uptake is shown in plot and compared with experimental data
#
# =============================================================================

from skinner_setup import *

def deut_uptake(peptides, peptide_no, kint, pfact, t):
    '''
    Evaluates the deuterium uptake of a certain peptide
    
    Input parameters
    ----------------
    peptides: pandas dataframe, format ['peptide','start_res','stop_res']
    peptide_no: number of the peptide to be analyzes, raw of the peptides dataframe
    kint: pandas dataframe, format ['residue','k_int']
    pfact: set of protection factors protection factors
    t: time interval over which deuterium uptake should be evaluated
    
    Ouput
    ----------------
    deut_uptake: deuterium uptake calculated at time t
    '''
    j = peptide_no
    start = peptides['start_res'][j]
    stop = peptides['stop_res'][j]
    
    deut_partial = 0; namide = 0
    for i in range(start, stop):
        k_int = kint['k_int'][i]
        p_fact = np.exp(pfact[i])
        k = 60*k_int/p_fact
        if k_int >= 0:
            namide += 1
            deut_partial += np.exp(-k*t)
    deut_uptake = (namide-deut_partial)/namide
 
    return deut_uptake
 
# %%
    
''' Generate experimental data '''
filename = 'test_data/exp_data.txt'

exp_times = [0.00083, 0.83330, 277.78000]
exp_deut = []

with open(filename,"w") as f:
    for time in exp_times:
        f.write('%5.5f ' % time)
        for i in range(0,len(peptides)):
             f.write('%5.10f ' % deut_uptake(peptides,i,kint,pfact,time))
        f.write("\n")
f.close

# %%

exp_data = pd.read_csv('test_data\\exp_data.txt', sep=" ", header=None)

# =============================================================================
# time = np.logspace(-6,4,1000)
# plt.figure(figsize=(10,6))
# for i in range(0,7):
#     plt.plot(time, deut_uptake(peptides, i, kint, pfact, time),
#              label='peptide'+str(i+1))
# plt.legend()
# for i in range(0,7):
#     plt.scatter(exp_data[0],exp_data[i+1])
# plt.xlim(1e-6,1e4); plt.ylim(0.0,1.0)
# plt.xlabel('Time (hours)',fontsize=18)
# plt.ylabel('Deuterium Uptake (D)', fontsize=18)
# plt.xscale('log')
# plt.grid(linestyle=':')
# 
# =============================================================================
# %%