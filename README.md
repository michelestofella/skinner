# skinner

The repository contains the algorithm to estimate protection factors from HDX-MS data. 
The current repository aims to reproduce the analysis performed in the paper by [Skinner](https://www.sciencedirect.com/science/article/pii/S0006349519301651) (2019).

Starting from test data, provided by Skinner and here contained in the **test_data** folder, the method of Skinner is applied. 

We give here a short description of the content of each file:

* **skinner_setup.py** imports the test data contained in the **test_data** folder as pandas dataframes;
* **skinner.py** contains the function for the evaluation of the theoretical deuterium uptake;
* **skinner_cost.py** contains the definition of the cost function to be minimized;
* **skinner_pfact.py** contains the algorithm to estimate protection factors starting from experimental data;
* **skinner_pfact_func.py** contains the functions needed by **skinner_pfact.py**.
