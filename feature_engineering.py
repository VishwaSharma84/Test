from data_preprocessing import data_preprocessing

def feature_engineering():
  data = data_preprocessing()
  data.to_csv('loan_data_cleansed.csv', index=False)
    return data
