import pandas as pd
import numpy as np
import statsmodels.formula.api as sm

"""A way to print pretty regression tables in python. Useful for econometrics
and social research."""

def get_data():
    
    data = pd.read_csv('test_data.csv')
    data['college'] = data['educ_cat'] > 3
    return data

def get_ending(pvalue):
    
    if pvalue <= 0.01:
        return '***'
    elif 0.05 >= pvalue > 0.01:
        return '**'
    elif 0.1 >= pvalue > 0.05:
        return '*'
    else:
        return '.'

def clean_boolean(index):
    
    if '[T.True]' in str(index):
        return str(index.strip('[T.True]'))
    else:
        return index

def reg3format(index,param,se):

    if len(index) > 12:
        print("{:<}: {:>60}\n{:>75}\n".format(index,param,'('+str(round(se,4))+')'))
    else:
        print("{:<}: {:>65}\n{:>75}\n".format(index,param,'('+str(round(se,4))+')'))

def reg2format(index,param,se):

    if len(index) > 12:
        print("{:<}: {:>40}\n{:>55}\n".format(index,param,'('+str(round(se,4))+')'))
    else:
        print("{:<}: {:>45}\n{:>55}\n".format(index,param,'('+str(round(se,4))+')'))

def reg1format(index,param,se):

    if len(index) > 12:
        print("{:<}: {:>20}\n{:>35}\n".format(index,param,'('+str(round(se,4))+')'))
    else:
        print("{:<}: {:>25}\n{:>35}\n".format(index,param,'('+str(round(se,4))+')'))




def Galaxy(reg1,reg2=None,reg3=None, table_name='Regression Table', names=None):

    """a function to print out a nice-looking regression table"""

    reglist1 = [
'{:.3f}{}'.format(param, get_ending(pvalue)) for param,pvalue in zip(reg1.params,reg1.pvalues)
    ]
    
  
    if reg2:
        reglist2 = [
'{:.3f}{}'.format(param, get_ending(pvalue)) for param,pvalue in zip(reg2.params,reg2.pvalues)
    ]
    
    if reg3:
        reglist3 = [
'{:.3f}{}'.format(param, get_ending(pvalue)) for param,pvalue in zip(reg3.params,reg3.pvalues)
    ]
    
    bottom = "|p < 0.01 ***| p < 0.05 **| p < 0.1 *| p > 0.1 .|"
              
    
    if reg2 and reg3:

        print('{:-^80}\n{:>35}{:>20}{:>20}'.format(table_name,names[0],names[1],names[2]))
        print('{:-^80}\n'.format(''))

        for index,param,se in zip(reg1.params.index,reglist1,reg1.bse):

            index = clean_boolean(index)
            reg1format(index,param,se)

        for index,param,se in zip(reg2.params.index,reglist2,reg2.bse):

            index = clean_boolean(index)
            reg2format(index,param,se)
            
        for index,param,se in zip(reg3.params.index,reglist3,reg3.bse):

            index = clean_boolean(index)
            reg3format(index,param,se)
        
        print('{:-^80}'.format(''))
        print('{:^80}'.format(bottom))
        print('{:-^80}'.format(''))
    
    elif reg2 and not reg3:

        print('{:-^80}\n{:>35}{:>20}'.format(table_name,names[0],names[1]))
        print('{:-^80}\n'.format(''))

        for index,param,se in zip(reg1.params.index,reglist1,reg1.bse):

            index = clean_boolean(index)
            reg1format(index,param,se)

        for index,param,se in zip(reg2.params.index,reglist2,reg2.bse):

            index = clean_boolean(index)
            reg2format(index,param,se)
            
        print('{:-^80}'.format(''))
        print('{:^80}'.format(bottom))
        print('{:-^80}'.format(''))
    
    elif not reg2 and not reg3:

        print('{:-^80}\n{:>35}'.format(table_name,names[0]))
        print('{:-^80}\n'.format(''))

        for index,param,se in zip(reg1.params.index,reglist1,reg1.bse):

            index = clean_boolean(index)
            reg1format(index,param,se)
        
        print('{:-^80}'.format(''))
        print('{:^80}'.format(bottom))
        print('{:-^80}'.format(''))
        

   

def main():
    
    data = get_data()

    reg1 = sm.ols('ppvt~momage', data=data).fit()
    reg2 = sm.ols('ppvt~momage + educ_cat', data = data).fit()
    reg3 = sm.ols('ppvt~momage + educ_cat + college + momage:college', data = data).fit()

    galaxy(reg1, reg2,reg3, table_name='Table 1',names=['reg1','reg2','reg3'])


if __name__ == '__main__':
    main()



















