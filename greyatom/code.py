# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
#Reading file
bank_data = pd.read_csv(path)
bank=pd.read_csv(path)
print(type(bank))
categorical_var=bank.select_dtypes(include = 'object')
print(categorical_var)
#Code starts here
numerical_var=bank.select_dtypes(include = 'number')
print(numerical_var)

# code ends here


# --------------
# code starts here

#From the dataframe bank, drop the column Loan_ID to create a new dataframe banks
banks=bank.drop(['Loan_ID'],axis=1)
print(banks.isnull().sum())
bank_mode=banks.mode(axis=1)
print(type(bank_mode))
#banks=banks.fillna(banks.mode(axis=1)[0],inplace=True)
banks['Gender'].fillna(banks['Gender'].mode()[0], inplace=True) 
banks['Married'].fillna(banks['Married'].mode()[0], inplace=True) 
banks['Dependents'].fillna(banks['Dependents'].mode()[0], inplace=True) 
banks['Self_Employed'].fillna(banks['Self_Employed'].mode()[0], inplace=True) 
banks['LoanAmount'].fillna(banks['LoanAmount'].mode()[0], inplace=True) 
banks['Loan_Amount_Term'].fillna(banks['Loan_Amount_Term'].mode()[0], inplace=True) 
banks['Credit_History'].fillna(banks['Credit_History'].mode()[0], inplace=True)

#code ends here


# --------------
# Code starts here
#print(banks.isnull().sum().values.sum(),banks.shape)
avg_loan_amount=pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc = np.mean)
#print(avg_loan_amount['LoanAmount'][1],2)




# code ends here



# --------------
# code starts here
#loan_approved_se=banks[banks['Self_Employed'] == 'Yes' & banks['Loan_Status']=='Y'].value_counts()
#l=banks[['Self_Employed']=='Yes']
#print(l)

##loan_approved_se= len(banks[banks['Self_Employed']=='Yes'] and banks[banks['Loan_Status']=='Y'])
filt1=(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')
filt2=(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')

##loan_approved_se=banks[banks["Self_Employed"]=='Yes'].count()["Loan_Status"] and banks[banks["Loan_Status"]=='Y'].count()["Self_Employed"]
loan_approved_se=banks.loc[filt1]['Loan_Status'].value_counts()
#print(loan_approved_se)
loan_approved_nse=banks.loc[filt2]['Loan_Status'].value_counts()
#print(loan_approved_nse)
##print(banks['Loan_status'].value_counts())
##loan_approved_nse=banks[banks["Self_Employed"]=='No'].count()["Loan_Status"] and banks[banks["Loan_Status"]=='Y'].count()["Self_Employed"]
#print(banks['Loan_Status'].count())#loan_approved_nse)
percentage_se = (loan_approved_se * 100 / 614)
percentage_se=percentage_se[0]
percentage_nse = (loan_approved_nse * 100 / 614)
percentage_nse=percentage_nse[0]
print(percentage_se)
print(percentage_nse)



# code ends here


# --------------
# code starts here
##print(banks['Loan_Amount_Term'].head(5))
loan_term = banks['Loan_Amount_Term'].apply(lambda x : int(x)/12) 
#print(type(loan_term))
filt3=loan_term >=25
big_loan_term=loan_term.loc[filt3].value_counts().sum()
print(big_loan_term)




# code ends here


# --------------
# code starts here
loan_groupby=banks.groupby('Loan_Status')
loan_groupby=loan_groupby['ApplicantIncome', 'Credit_History']
mean_values=loan_groupby.mean()
print(mean_values.iloc[1,0], 2)




# code ends here


