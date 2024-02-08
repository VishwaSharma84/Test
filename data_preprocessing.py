from data_extarction import extract_data

def cat_to_num(df, c_var):
    for i in c_var:
        uniques_value = df[i].unique()
        df[i].replace(uniques_value, [0, 1], inplace=True)

    for i in ['Property_Area']:
        uniques_value = df[i].unique()
        df[i].replace(uniques_value, [0, 1, 3], inplace=True)
      
def data_preprocessing():
  data = extract_data()
  df = data.copy()
  df = df.drop(['Loan_ID'], axis=1)
  df['Gender'] = df['Gender'].fillna(df['Gender'].mode().iloc[0])
  df['Self_Employed'] = df['Self_Employed'].fillna(df['Self_Employed'].mode().iloc[0])
  df['Loan_Amount_Term'] = df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode().iloc[0]).astype(int)
  df['Credit_History'] = df['Credit_History'].fillna(df['Credit_History'].mode().iloc[0]).astype(int)

  df['Dependents'] = df['Dependents'].replace(['0', '1', '2', '3+'], [0,1,2,3,])
  df['Dependents'] = df['Dependents'].fillna(df['Dependents'].mode().iloc[0])

  df['CoapplicantIncome'] = df['CoapplicantIncome'].astype(int)
  df['LoanAmount'] = df['LoanAmount'].astype(int)
  
  c_variables = ['Gender', 'Married', 'Education', 'Education','Self_Employed', 'Loan_Status']
  cat_to_num(df, c_variables)

data_preprocessing()
