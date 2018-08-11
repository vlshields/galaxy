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

def bottom3(reg1,reg2,reg3):

    ps = "|p < 0.01 ***| p < 0.05 **| p < 0.1 *| p > 0.1 .|"
    
    print('{:-^80}'.format(''))
    print('{:^80}'.format(ps))
    print('{:-^80}'.format(''))

    print("{:<}: {:>22}{:>20}{:>20}".format('Observations',round(reg1.nobs),
        round(reg2.nobs), round(reg3.nobs)))

    print("{:<}: {:>25}{:>20}{:>20}".format('R squared',round(reg1.rsquared,3),
        round(reg2.rsquared,3), round(reg3.rsquared,3)))

    print("{:<}: {:>20}{:>21}{:>20}".format('Adj. Rsquared',round(reg1.rsquared_adj,3),
        round(reg2.rsquared_adj,3), round(reg3.rsquared_adj,3)))
    
    print('{:<}: {:>27}{}{:>18}{}{:>18}{}'.format('F Stat',round(reg1.fvalue,3),get_ending(reg1.f_pvalue),
        round(reg2.fvalue,3),get_ending(reg2.f_pvalue),round(reg3.fvalue,3),get_ending(reg3.f_pvalue)))
    print('{:-^80}'.format(''))

def bottom2(reg1,reg2):

    ps = "|p < 0.01 ***| p < 0.05 **| p < 0.1 *| p > 0.1 .|"
    
    print('{:-^80}'.format(''))
    print('{:^80}'.format(ps))
    print('{:-^80}'.format(''))

    print("{:<}: {:>22}{:>20}".format('Observations',round(reg1.nobs),
        round(reg2.nobs)))

    print("{:<}: {:>25}{:>20}".format('R squared',round(reg1.rsquared,3),
        round(reg2.rsquared,3)))

    print("{:<}: {:>20}{:>21}".format('Adj. Rsquared',round(reg1.rsquared_adj,3),
        round(reg2.rsquared_adj,3)))

    print('{:<}: {:>27}{}{:>18}{}'.format('F Stat',round(reg1.fvalue,3),get_ending(reg1.f_pvalue),
        round(reg2.fvalue,3),get_ending(reg2.f_pvalue)))
    print('{:-^80}'.format(''))

def bottom(reg1):

    ps = "|p < 0.01 ***| p < 0.05 **| p < 0.1 *| p > 0.1 .|"
    
    print('{:-^80}'.format(''))
    print('{:^80}'.format(ps))
    print('{:-^80}'.format(''))

    print("{:<}: {:>22}".format('Observations',round(reg1.nobs)))

    print("{:<}: {:>25}".format('R squared',round(reg1.rsquared,3)))

    print("{:<}: {:>20}".format('Adj. Rsquared',round(reg1.rsquared_adj,3)))

    print('{:<}: {:>27}{}'.format('F Stat',round(reg1.fvalue,3),get_ending(reg1.f_pvalue)))
    print('{:-^80}'.format(''))

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

        bottom3(reg1,reg2,reg3)
        
        
    
    elif reg2 and not reg3:

        print('{:-^80}\n{:>35}{:>20}'.format(table_name,names[0],names[1]))
        print('{:-^80}\n'.format(''))

        for index,param,se in zip(reg1.params.index,reglist1,reg1.bse):

            index = clean_boolean(index)
            reg1format(index,param,se)

        for index,param,se in zip(reg2.params.index,reglist2,reg2.bse):

            index = clean_boolean(index)
            reg2format(index,param,se)
            
        bottom2(reg1,reg2)
    
    elif not reg2 and not reg3:

        print('{:-^80}\n{:>35}'.format(table_name,names[0]))
        print('{:-^80}\n'.format(''))

        for index,param,se in zip(reg1.params.index,reglist1,reg1.bse):

            index = clean_boolean(index)
            reg1format(index,param,se)
        
        bottom(reg1)
           

def main():
    
    data = get_data()

    reg1 = sm.ols('ppvt~momage', data=data).fit()
    reg2 = sm.ols('ppvt~momage + educ_cat', data = data).fit()
    reg3 = sm.ols('ppvt~momage + educ_cat + college + momage:college', data = data).fit()

    Galaxy(reg1,reg2,table_name='Table 1',names=['reg1','reg2','reg3'])


if __name__ == '__main__':
    main()



















