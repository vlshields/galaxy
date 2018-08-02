
## Galaxy: A way to Print Pretty Regression Tables
************

A small side project aiming to use python for printing regression tables similar to the Stargazer library in R. It is not nearly finished yet, but its on its way. It currently can only take 3 regression models, but the plan for now is to scale it up to 9 regression models.

### Why use Galaxy?

##### Logistics

In econometrics, it is often useful to print the parameters of more than one regression model on the same table to see how adjusting for one predictor may influence the coefficient of another predictor. Statsmodels.formula.api.ols has great support for ols, but calling ```model.summary()``` will only print the results of one regression model. 

##### Its an ongoing project

The galaxy project is ongoing, and will constantly be updated and improved upon. The goal of galaxy is to print regression tables worthy of academic publications, and in its first version it is already looking very promising. As far as I know, there is no other module in python that can print these types of regression tables, especially one that is constantly being updated. Galaxy is an open source project, and anyone can contribute.


### Installation

Install directly from GitHub through pip:

```
pip install git+https://github.com/vlshields/galaxy.git
```

### Installing dependencies

You most likely have the required dependencies, but if you do not then run this command:

```
pip install -r requirements.txt
```

### Usage
**************

#### Example with one regression model


```python
import pandas as pd
from statsmodels.formula.api import ols
from galaxy import Galaxy

data = pd.read_csv('./galaxy/test_data.csv')
model = ols('ppvt~momage', data=data).fit()

Galaxy(model, table_name='Example Table 1', names = ['one input'])
```

    --------------------------------Example Table 1---------------------------------
                              one input
    --------------------------------------------------------------------------------
    
    Intercept:                 67.783***
                                (8.688)
    
    momage:                   0.840**
                               (0.3786)
    
    --------------------------------------------------------------------------------
                   |p < 0.01 ***| p < 0.05 **| p < 0.1 *| p > 0.1 .|                
    --------------------------------------------------------------------------------


#### Example with 3 regression models


```python
data['college'] = data['educ_cat'] > 3 # Galaxy will automatically strip the [T.True] when creating a boolean

model = ols('ppvt~momage', data=data).fit()
model2 = ols('ppvt~momage + educ_cat', data = data).fit()
model3 = ols('ppvt~momage + educ_cat + college + momage:college', data = data).fit()

Galaxy(model,model2,model3, table_name='Example Table 2', names = ['one input', 'two inputs', 'three inputs'])
```

    --------------------------------Example Table 2---------------------------------
                              one input          two inputs        three inputs
    --------------------------------------------------------------------------------
    
    Intercept:                 67.783***
                                (8.688)
    
    momage:                   0.840**
                               (0.3786)
    
    Intercept:                                     69.155***
                                                   (8.5706)
    
    momage:                                        0.343.
                                                   (0.3981)
    
    educ_cat:                                      4.711***
                                                   (1.3165)
    
    Intercept:                                                         67.392***
                                                                       (9.1782)
    
    colleg:                                                           56.438.
                                                                      (48.0256)
    
    momage:                                                            0.442.
                                                                       (0.4111)
    
    momage:colleg:                                                      -2.162.
                                                                       (1.8573)
    
    educ_cat:                                                          4.461***
                                                                       (1.6227)
    
    --------------------------------------------------------------------------------
                   |p < 0.01 ***| p < 0.05 **| p < 0.1 *| p > 0.1 .|                
    --------------------------------------------------------------------------------

