# =============================================================================
# 
# Statistical Analysis of data obtained in skinner_pfact.py
# Median and interquantile range are calculated for each residue
#
# =============================================================================

from skinner_setup import *
from scipy.stats import iqr

''' Format: last column is cost function '''
pep15 = pd.read_csv('out_data\pep15_N5000_Nrep200.txt', sep=" ", header=None)
pep1235 = pd.read_csv('out_data\pep1235_N5000_Nrep200.txt', sep=" ", header=None)
pepALL = pd.read_csv('out_data\pep1234567_N5000_Nrep200.txt', sep=" ", header=None)

# %%

''' Choose the data to be analyzed '''
data = pepALL
low_cost = 2e-5    # set lowest value the cost function can assume

plt.figure(figsize=(12,7))
plt.plot(pfact_data[0], pfact, 'o-', color='black', alpha=0.8)
for i in range(0,len(data)):
    # consider only sets for which lowest cost functions
    if (data.iloc[i][15] <= low_cost):
        plt.scatter(pfact_data[0][1:], data.iloc[i][1:15], marker='x', color='red')
plt.xlabel("Residue",fontsize=18); plt.ylabel("ln(P)",fontsize=18)
plt.grid(linestyle=':')
plt.text(14,2,'A',fontsize=25)


# %%

''' For each residue, calculate median and interquantile range '''
med = []; interq = []
for i in range(1,15):
    med.append(np.median(data[i]))
    interq.append(iqr(data[i]))
    
# %%

plt.figure(figsize=(12,7))
plt.plot(pfact_data[0], pfact, 'o-', color='black')
for i in range(0,len(med)):
    plt.errorbar(i+2,med[i],yerr=0.5*interq[i],fmt='o-',color='red',ms=5)
plt.xlabel("Residue",fontsize=18); plt.ylabel("ln(P)",fontsize=18)
plt.grid(linestyle=':')
plt.text(14,2,'C',fontsize=25)

# %%