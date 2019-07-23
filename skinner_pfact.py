# =============================================================================
# 
# Determine protection factors from experimental data
# through minimization of a cost function
#
# =============================================================================

from skinner_setup import *
from skinner_pfact_func import *

from skinner_cost import cost_fun
from scipy.optimize import least_squares

# %%

''' Generate N random protection factor lists '''
N = 5000                    # number of random lists to be generated
pep_list = [1,2,3,5]  # peptides to be considered
N_repeat = 200                # number of times the procedure should be repeated

p_factors = []; cost = []
for i in range(0,N_repeat):
    print('Calculating: ',i*100/N_repeat,' %')
    p_set = generate_rand_pfact_sets(N,seq)
    initial_guess = select_best_pfact_set(p_set,pep_list,peptides,kint,exp_data)
    least_sq = least_squares(cost_fun,initial_guess,
                             args=(pep_list,peptides,kint,exp_data),
                             bounds=[0,20])
    p_factors.append(least_sq.x)
    # take note of the cost function associated to each set of protection factors    
    cost.append(cost_fun(least_sq.x, pep_list, peptides, kint, exp_data))    
print('Done: 100 %')

# %%

''' Save data in a .txt file '''
filename = "out_data\pep1235_N5000_Nrep200.txt"
''' Format: [p1, p2, ..., p15, cost] '''

with open(filename,"w") as f:
    for i in range(0,len(p_factors)):
        for j in range(0,len(seq)):
            f.write('%5.10f ' % p_factors[i][j])
        f.write('%5.10f' % cost[i])
        f.write("\n")
f.close

# %%