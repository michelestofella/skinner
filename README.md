# skinner

**Estimating potection factors from HDX-MS data**

Starting from *in silico* data generated from a fictitious sequence, 
we reproduce the analysis performed by [Skinner](https://www.sciencedirect.com/science/article/pii/S0006349519301651) (2019).

We give here a description of the repository structure:

* **Estimating_Protection_Factors_from_HDXMS_Data.pdf** contains the final report of the project;
* **scripts** is the folder containing the codes used for the analysis;
* **images** is the folder containing the images used in the report.

## scripts

The folder **scripts** contains the codes used for the analysis. 
We give here a description of the files contained in the folder. 

The *experimental* data used for the analysis are contained in the folder **test_data**:

* **ref.pfact** contains the reference protection factors used;
* **test.seq** contains the fictitious sequence;
* **test.list** contains the fragments of the polypeptide chain that have been analyzed;
* **test.kint** contains the intrinsic exchange rates associated to each residue;
* **exp_data.txt** contains the experimental data (calculated thorugh **../skinner.py**) used for the analysis.

To perform the random search, i.e. to generate random sets of protection factors starting from the data contained in **test_data**, the following programs (languages: Python) were used:

* **skinner_setup.py** imports the test data contained in the **test_data** folder as pandas dataframes;
* **skinner.py** contains the function for the evaluation of the theoretical deuterium uptake; it evaluates the deuterium uptake at three time points: these are saved in the **test_data** folder and are the experimental points used in the analysis.
* **skinner_cost.py** contains the definition of the cost function to be minimized;
* **skinner_pfact.py** contains the algorithm to estimate protection factors starting from experimental data. The results are saved as *.txt* files in the **out_data** folder;
* **skinner_pfact_func.py** contains the functions needed by **skinner_pfact.py**.

The estimated protection factors are then statistically analyzed with the following files (languages: Python and R):

* **skinner_stat.py** calculates median and interquantile ranges for the estimated protection factors;
* **clust.R** performs the model-based clustering approach (using the [Mclust package](https://cran.r-project.org/web/packages/mclust/index.html) implemented in R) and writes the results of the analysis in files contained in the folder **out_data/clust_out**.
* **skinner_clust.py** takes the results of **clust.R** and represent them graphically.

The results of the analysis are contained in the folder **out_data**:

* **pep15_N5000_Nrep200** contains the outcomes of the random search considering peptides 1 and 5;
* **pep1235_N5000_Nrep200** contains the outcomes of the random search considering peptides 1-3 and 5;
* **pep1234567_N5000_Nrep200** contains the outcomes of the random search considering all the peptides 1-7.

Note that in the previous files the last column is the cost function of the set.

* **clust_out** is the folder containing the results of the clustering method. In particular, **clust_bic.txt** contains the BIC values to determine the optimal solution, **clust_means.txt** contains the means of the clusters and **clust_var.txt** contains the variances.

