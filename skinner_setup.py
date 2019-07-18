# =============================================================================
# 
# Reference data are here organised in pandas dataframes
# Data are visualised
# 
# =============================================================================

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pfact_data = pd.read_csv('test_data\\ref.pfact', sep=" ", header=None)
pfact = pfact_data[1]

sequence = open('test_data\\test.seq','r')  
if sequence.mode == 'r':
    seq = sequence.read()    

peptides = pd.read_csv('test_data\\test.list', sep=" ", header=None)
peptides.columns = ["peptide","start_res","stop_res","sequence"]

kint = pd.read_csv('test_data\\test.kint', header=None, sep='\t')
kint.columns = ["residue","k_int"]
# last value has been changed (it has been multiplied *100)

exp_data = pd.read_csv('test_data\\test.Dexp', sep=" ", header=None)

# %%

# """ This block is useful to visualize data """
# fig, (ax1,ax2) = plt.subplots(2, 1, figsize=[6, 7])
# 
# ax1.plot(pfact_data[0],pfact,'o-',color='black')
# ax1.grid(linestyle=':')
# 
# for i in range(0,len(peptides["peptide"])):
#     ax2.hlines(y=peptides["peptide"][i], xmin=peptides["start_res"][i], xmax=peptides["stop_res"][i],
#                linestyles='-')
# ax2.grid(linestyle=':')

# %%