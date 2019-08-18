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

# %%

# =============================================================================
# fig = plt.figure(figsize=[12, 7])
# plt.plot(pfact_data[0],pfact,'o-',color='black')
# plt.grid(linestyle=':')
# plt.xlabel('Residue', fontsize=18)
# plt.ylabel('ln(P)',fontsize=18)
#  
# # %%
# 
# fig = plt.figure(figsize=[12, 7])
# for i in range(0,len(peptides["peptide"])):
#     plt.hlines(y=peptides["peptide"][i], xmin=peptides["start_res"][i], xmax=peptides["stop_res"][i],
#                linestyles='-')
# plt.grid(linestyle=':')
# plt.xlabel('Residue',fontsize=18); plt.ylabel('Peptide',fontsize=18)
# 
# =============================================================================
# %%