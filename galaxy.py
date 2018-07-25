import pandas as pd
import numpy as np
import statsmodels.formula.api as sm

def get_data():
    data = pd.read_csv('/Users/vincentshields/Desktop/hello/output.csv')
    data['college'] = data['educ_cat'] > 3
    return data



def galaxy(reg1,reg2=None,reg3=None, table_name='Regression Table', names=None):
    
    reglist1 = []
    for i in list(range(len(reg1.pvalues))):
        if reg1.pvalues[i] <= 0.01:
            reglist1.append(str(round(reg1.params[i],3))+'***')
        elif 0.05 >= reg1.pvalues[i] > 0.01:
            reglist1.append(str(round(reg1.params[i],3)) + '**')
        elif 0.1 >= reg1.pvalues[i] > 0.05:
            reglist1.append(str(round(reg1.params[i],3)) + '*')
        else:
            reglist1.append(str(round(reg1.params[i],3)) + '.')
    if reg2:
        reglist2 = []
        for i in list(range(len(reg2.pvalues))):
            if reg2.pvalues[i] <= 0.01:
                reglist2.append(str(round(reg2.params[i],3))+'***')
            elif 0.05 >= reg2.pvalues[i] > 0.01:
                reglist2.append(str(round(reg2.params[i],3)) + '**')
            elif 0.1 >= reg2.pvalues[i] > 0.05:
                reglist2.append(str(round(reg2.params[i],3)) + '*')
            else:
                reglist2.append(str(round(reg2.params[i],3)) + '.')
    if reg3:
        reglist3 = []
        for i in list(range(len(reg3.pvalues))):
            if reg3.pvalues[i] <= 0.01:
                reglist3.append(str(round(reg3.params[i],3))+'***')
            elif 0.05 >= reg3.pvalues[i] > 0.01:
                reglist3.append(str(round(reg3.params[i],3)) + '**')
            elif 0.1 >= reg3.pvalues[i] > 0.05:
                reglist3.append(str(round(reg3.params[i],3)) + '*')
            else:
                reglist3.append(str(round(reg3.params[i],3)) + '.')
    names.append(table_name)
    print("""


                        {3}
-------------------------------------------------------
{0}                        {1}                   {2}

        """.format(*names))

    for i in list(range(len(reglist1))):
        print("""{}: {}\n {}""".format(reg1.params.index[i],reglist1[i],round(reg1.bse[i],4)))
    print()

    for i in list(range(len(reglist2))):
        print("""             {}: {}\n                      {}""".format(reg2.params.index[i],reglist2[i],round(reg2.bse[i],4)))

    for i in list(range(len(reglist3))):
        print("""                                  {}: {}\n                                   {}""".format(reg3.params.index[i],reglist3[i],round(reg3.bse[i],4)))

    print("""
------------------------------------------------------
|p < 0.01 ***| p < 0.05 **| p < 0.1 *| p > 0.1 .|
------------------------------------------------------
          """)

def main():
    
    data = get_data()

    reg1 = sm.ols('ppvt~momage', data=data).fit()
    reg2 = sm.ols('ppvt~momage + educ_cat', data = data).fit()
    reg3 = sm.ols('ppvt~momage + educ_cat + college + momage:college', data = data).fit()

    galaxy(reg1,reg2,reg3, 'Table 1',['reg1', 'reg2', 'reg3'])


if __name__ == '__main__':
    main()



















