# =============================================================================
# 
# Clustering algorithm is applied in cluster.R
# Results are stored in clust_out folder
# We show here the results
# 
# =============================================================================

from skinner_setup import *

clust_data = pd.read_csv('\\out_data\\clust_out\\clust_means.txt', sep=" ")

# %%

plt.figure(figsize=(12,7))
plt.plot(pfact_data[0], pfact, 'o-', color='black', label='Real')
plt.plot(pfact_data[0][1:], clust_data['V1'], 'o-', label='Cluster 1', alpha=0.5)
plt.plot(pfact_data[0][1:], clust_data['V2'], 'o-', label='Cluster 2', alpha=0.5)
plt.plot(pfact_data[0][1:], clust_data['V3'], 'o-', label='Cluster 3', alpha=0.5)
plt.plot(pfact_data[0][1:], clust_data['V4'], 'o-', label='Cluster 4', alpha=0.5)
plt.plot(pfact_data[0][1:], clust_data['V5'], 'o-', label='Cluster 5', alpha=0.5)
plt.plot(pfact_data[0][1:], clust_data['V6'], 'o-', label='Cluster 6', alpha=0.5)
plt.plot(pfact_data[0][1:], clust_data['V7'], 'o-', label='Cluster 7', alpha=0.5)
plt.plot(pfact_data[0][1:], clust_data['V8'], 'o-', label='Cluster 8', alpha=0.5)
plt.grid(linestyle=':')
plt.legend()

# %%
