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
N = 1000                    # number of random lists to be generated
pep_list = [1,3,5]  # peptides to be considered
N_repeat = 10                # number of times the procedure should be repeated

p_factors = []
for i in range(0,N_repeat):
    print('Calculating: ',i*100/N_repeat,' %')
    p_set = generate_rand_pfact_sets(N,seq)
    initial_guess = select_best_pfact_set(p_set,pep_list,peptides,kint,exp_data)
    least_sq = least_squares(cost_fun,initial_guess,args=(pep_list,peptides,kint,exp_data))
    p_factors.append(least_sq.x)
print('Done: 100 %')

# %%

plt.plot(pfact_data[0], pfact, 'o-', color='black')
for i in range(0,N_repeat):
    plt.scatter(pfact_data[0][1:], p_factors[i][1:], marker='x', color='red')
plt.grid(linestyle=':')

# %%