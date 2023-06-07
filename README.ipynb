{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Galaxy: A way to Print Pretty Regression Tables\n",
    "************\n",
    "\n",
    "A small side project aiming to use python for printing regression tables similar to the Stargazer library in R. It is not nearly finished yet, but its on its way. It currently can only take 3 regression models, but the plan for now is to scale it up to 9 regression models.\n",
    "\n",
    "### Why use Galaxy?\n",
    "\n",
    "##### Logistics\n",
    "\n",
    "In econometrics, it is often useful to print the parameters of more than one regression model on the same table to see how adjusting for one predictor may influence the coefficient of another predictor. Statsmodels.formula.api.ols has great support for ols, but calling ```model.summary()``` will only print the results of one regression model. \n",
    "\n",
    "##### Its an ongoing project\n",
    "\n",
    "The galaxy project is ongoing, and will constantly be updated and improved upon. The goal of galaxy is to print regression tables worthy of academic publications, and in its first version it is already looking very promising. As far as I know, there is no other module in python that can print these types of regression tables, especially one that is constantly being updated. Galaxy is an open source project, and anyone can contribute.\n",
    "\n",
    "\n",
    "### Installation\n",
    "\n",
    "Install directly from GitHub through pip:\n",
    "\n",
    "```\n",
    "pip install git+https://github.com/vlshields/galaxy.git\n",
    "```\n",
    "\n",
    "### Installing dependencies\n",
    "\n",
    "You most likely have the required dependencies, but if you do not then run this command:\n",
    "\n",
    "```\n",
    "pip install -r requirements.txt\n",
    "```\n",
    "\n",
    "### Usage\n",
    "**************\n",
    "\n",
    "#### Example with one regression model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--------------------------------Example Table 1---------------------------------\n",
      "                          one input\n",
      "--------------------------------------------------------------------------------\n",
      "\n",
      "Intercept:                 67.783***\n",
      "                            (8.688)\n",
      "\n",
      "momage:                   0.840**\n",
      "                           (0.3786)\n",
      "\n",
      "--------------------------------------------------------------------------------\n",
      "               |p < 0.01 ***| p < 0.05 **| p < 0.1 *| p > 0.1 .|                \n",
      "--------------------------------------------------------------------------------\n",
      "Observations:                    400\n",
      "R squared:                     0.012\n",
      "Adj. Rsquared:                 0.01\n",
      "F Stat:                       4.926**\n",
      "--------------------------------------------------------------------------------\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from statsmodels.formula.api import ols\n",
    "from galaxy import Galaxy\n",
    "\n",
    "data = pd.read_csv('./galaxy/test_data.csv')\n",
    "model = ols('ppvt~momage', data=data).fit()\n",
    "\n",
    "Galaxy(model, table_name='Example Table 1', names = ['one input'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Example with 3 regression models"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--------------------------------Example Table 2---------------------------------\n",
      "                          one input          two inputs        three inputs\n",
      "--------------------------------------------------------------------------------\n",
      "\n",
      "Intercept:                 67.783***\n",
      "                            (8.688)\n",
      "\n",
      "momage:                   0.840**\n",
      "                           (0.3786)\n",
      "\n",
      "Intercept:                                     69.155***\n",
      "                                               (8.5706)\n",
      "\n",
      "momage:                                        0.343.\n",
      "                                               (0.3981)\n",
      "\n",
      "educ_cat:                                      4.711***\n",
      "                                               (1.3165)\n",
      "\n",
      "Intercept:                                                         67.392***\n",
      "                                                                   (9.1782)\n",
      "\n",
      "colleg:                                                           56.438.\n",
      "                                                                  (48.0256)\n",
      "\n",
      "momage:                                                            0.442.\n",
      "                                                                   (0.4111)\n",
      "\n",
      "momage:colleg:                                                      -2.162.\n",
      "                                                                   (1.8573)\n",
      "\n",
      "educ_cat:                                                          4.461***\n",
      "                                                                   (1.6227)\n",
      "\n",
      "--------------------------------------------------------------------------------\n",
      "               |p < 0.01 ***| p < 0.05 **| p < 0.1 *| p > 0.1 .|                \n",
      "--------------------------------------------------------------------------------\n",
      "Observations:                    400                 400                 400\n",
      "R squared:                     0.012               0.043               0.046\n",
      "Adj. Rsquared:                 0.01                0.038               0.037\n",
      "F Stat:                       4.926**             8.939***             4.808***\n",
      "--------------------------------------------------------------------------------\n"
     ]
    }
   ],
   "source": [
    "data['college'] = data['educ_cat'] > 3 # Galaxy will automatically strip the [T.True] when creating a boolean\n",
    "\n",
    "model = ols('ppvt~momage', data=data).fit()\n",
    "model2 = ols('ppvt~momage + educ_cat', data = data).fit()\n",
    "model3 = ols('ppvt~momage + educ_cat + college + momage:college', data = data).fit()\n",
    "\n",
    "Galaxy(model,model2,model3, table_name='Example Table 2', names = ['one input', 'two inputs', 'three inputs'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Galaxydf\n",
    "\n",
    "You can also output your results in dataframe format with Galaxydf..."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>reg1</th>\n",
       "      <th>reg2</th>\n",
       "      <th>reg3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Intercept</th>\n",
       "      <td>67.783***(8.688)</td>\n",
       "      <td>69.155***(8.571)</td>\n",
       "      <td>67.392***(9.178)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>momage</th>\n",
       "      <td>0.840**(0.379)</td>\n",
       "      <td>0.343.(0.398)</td>\n",
       "      <td>56.438.(48.026)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>educ_cat</th>\n",
       "      <td></td>\n",
       "      <td>4.711***(1.317)</td>\n",
       "      <td>0.442.(0.411)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>college[T.True]</th>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td>-2.162.(1.857)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>momage:college[T.True]</th>\n",
       "      <td></td>\n",
       "      <td></td>\n",
       "      <td>4.461***(1.623)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Observations</th>\n",
       "      <td>400.000</td>\n",
       "      <td>400.000</td>\n",
       "      <td>400.000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Rsquared</th>\n",
       "      <td>0.012</td>\n",
       "      <td>0.043</td>\n",
       "      <td>0.046</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Adj. Rsquared</th>\n",
       "      <td>0.010</td>\n",
       "      <td>0.038</td>\n",
       "      <td>0.037</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Fstat</th>\n",
       "      <td>4.926**</td>\n",
       "      <td>8.939***</td>\n",
       "      <td>4.808***</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                    reg1              reg2              reg3\n",
       "Intercept               67.783***(8.688)  69.155***(8.571)  67.392***(9.178)\n",
       "momage                    0.840**(0.379)     0.343.(0.398)   56.438.(48.026)\n",
       "educ_cat                                   4.711***(1.317)     0.442.(0.411)\n",
       "college[T.True]                                               -2.162.(1.857)\n",
       "momage:college[T.True]                                       4.461***(1.623)\n",
       "Observations                     400.000           400.000           400.000\n",
       "Rsquared                           0.012             0.043             0.046\n",
       "Adj. Rsquared                      0.010             0.038             0.037\n",
       "Fstat                            4.926**          8.939***          4.808***"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from galaxy import Galaxydf\n",
    "from galaxy import get_data\n",
    "\n",
    "data = pd.read_csv('./galaxy/test_data.csv')\n",
    "data['college'] = data['educ_cat'] > 3\n",
    "\n",
    "reg1 = ols('ppvt~momage', data=data).fit()\n",
    "reg2 = ols('ppvt~momage + educ_cat', data = data).fit()\n",
    "reg3 = ols('ppvt~momage + educ_cat + college + momage:college', data = data).fit()\n",
    "\n",
    "Galaxydf(reg1,reg2,reg3,names=['reg1','reg2','reg3'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
