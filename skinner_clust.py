# =============================================================================
# 
# Clustering algorithm is applied in cluster.R
# Results are stored in clust_out folder
# We show here the results
# 
# =============================================================================

from skinner_setup import *

clust_data = pd.read_csv('out_data\clust_out\clust_means.txt', sep=" ")

# %%

plt.figure(figsize=(12,7))
plt.plot(pfact_data[0], pfact, 'o-', color='black', label='Real')
for i in range(1,len(clust_data.iloc[0])):
    plt.plot(pfact_data[0][1:], clust_data['V'+str(i)], 'o-', label='Cluster'+str(i), alpha=0.5)
plt.grid(linestyle=':')
plt.legend()

# %%