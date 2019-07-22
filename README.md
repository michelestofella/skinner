# skinner

The repository contains the algorithm to estimate protection factors from HDX-MS data. 
The current repository aims to reproduce the analysis performed in the paper by [Skinner](https://www.sciencedirect.com/science/article/pii/S0006349519301651) (2019).

Starting from test data, provided by Skinner and here contained in the **test_data** folder, the method of Skinner is applied. 

We give here a short description of the content of each file.

To generate sets of protection factors starting from HDX-MS data, the following programs (languages: Python) were used:

* **skinner_setup.py** imports the test data contained in the **test_data** folder as pandas dataframes;
* **skinner.py** contains the function for the evaluation of the theoretical deuterium uptake;
* **skinner_cost.py** contains the definition of the cost function to be minimized;
* **skinner_pfact.py** contains the algorithm to estimate protection factors starting from experimental data. The results are saved as *.txt* files in the **out_data** folder;
* **skinner_pfact_func.py** contains the functions needed by **skinner_pfact.py**.

The estimated protection factors are then statistically analyzed with the following files (languages: Python and R):

* **skinner_stat.py** calculates median and interquantile ranges for the estimated protection factors;
* **clust.R** performs the model-based clustering approach (using the [Mclust package](https://cran.r-project.org/web/packages/mclust/index.html) implemented in R) and writes the results of the analysis in files contained in the folder **out_data/clust_out**.
* **skinner_clust.py**
