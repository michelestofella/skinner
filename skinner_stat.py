# =============================================================================
# 
# Statistical Analysis of data obtained in skinner_pfact.py
# Median and interquantile range are calculated for each residue
#
# =============================================================================

from skinner_setup import *
from scipy.stats import iqr

# Old format data
# pep15 = pd.read_csv("pep15_N5000_Nrep100.txt", sep=" ", header=None)
# pep135 = pd.read_csv('pep135_N5000_Nrep100.txt', sep=" ", header=None)
# pepALL = pd.read_csv('pepALL_N5000_Nrep100.txt', sep=" ", header=None)

''' Format: last column is cost function '''
pep1235 = pd.read_csv('out_data\pep1235_N5000_Nrep100.txt', sep=" ", header=None)

# %%
''' Choose the data to be analyzed '''
data = pep1235

N_repeat = 100

plt.plot(pfact_data[0], pfact, 'o-', color='black', alpha=0.4)
for i in range(0,N_repeat):
    # consider only sets for which lowest cost functions
    if (data.iloc[i][15] <= 0.005):
        plt.scatter(pfact_data[0][1:], data.iloc[i][1:15], marker='x', color='red')
plt.grid(linestyle=':')

# %%

''' For each residue, calculate median and interquantile range '''
med = []; interq = []
for i in range(1,15):
    med.append(np.median(data[i]))
    interq.append(iqr(data[i]))
    
# %%

plt.plot(pfact_data[0], pfact, 'o-', color='black')
for i in range(0,len(med)):
    plt.errorbar(i+2,med[i],yerr=0.5*interq[i],fmt='o-',color='red',ms=5)
plt.grid(linestyle=':')

# %%