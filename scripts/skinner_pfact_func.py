# =============================================================================
# 
# Functions needed for skinner_pfact.py,
# i.e. to extract protection factors from experimental data
# 
# =============================================================================

from skinner_setup import *
from skinner_cost import cost_fun
from numpy.random import rand 

# %%

''' Function to generate N sets of protection factors '''
def generate_rand_pfact_sets(N, sequence):
    sequence_length = len(sequence)
    
    p_set = []
    for i in range(0,N):
        random_set = 20*rand(sequence_length) # uniform distribution between 0 and 20
        p_set.append(random_set)
    
    return p_set

# %%

''' For each set of protection factors, evaluate the cost function
    and choose the set that minimizes it '''
def select_best_pfact_set(p_set, pep_list, peptides, kint, exp_data):
    
    set_no = []; set_cost = []   
    for i in range(0,len(p_set)):
        set_no.append(i)
        cost = cost_fun(p_set[i], pep_list, peptides, kint, exp_data)
        set_cost.append(cost)

    index = np.argmin(set_cost)
    best_pfact = p_set[index]
    
    return best_pfact

# %%
