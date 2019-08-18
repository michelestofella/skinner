# =============================================================================
# 
# Cost function to be minimized
# 
# =============================================================================

# from skinner_setup import *
from skinner import deut_uptake

def cost_fun(pfact, pep_list, peptides, kint, exp_data):
    # we are neglecting weigths
    cost = 0
    for j in pep_list:
        peptide_no = j-1
        
        for k in range(0,len(exp_data[0])):
            tk = exp_data[0][k]
            d_pred = deut_uptake(peptides,peptide_no,kint,pfact,tk)
            d_exp = exp_data[j][k]
        
            cost += (d_pred-d_exp)**2
    return cost

# pep_list = [1,3,5]
# p_set = 20*rand(len(seq))    
# cost_fun(p_set,pep_list,peptides,kint,exp_data)

# %%