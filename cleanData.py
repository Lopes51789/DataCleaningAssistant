import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
import dataclasses


class DataFrame:
    def __init__(self, filepath: str = None, df: pd.DataFrame = None):
        if df is not None and filepath is None:
            self.df = df
        
        elif filepath is not None and df is None:
            temp_filepath = filepath.split(".")
            if temp_filepath[1] == "csv":
                self.df = pd.read_csv(filepath)
            elif temp_filepath[1] == "json":
                self.df = pd.read_json(filepath)
            elif temp_filepath[1] == "xlsx":
                self.df = pd.read_excel(filepath)
            elif temp_filepath[1] == "parquet":
                self.df = pd.read_parquet(filepath)
            elif temp_filepath[1] == "sql":
                self.df = pd.read_sql(filepath)
            else:
                raise ValueError("Invalid file format")
            
        else:
            raise ValueError("Either filepath or df must be provided, not both")

    def get_duplicates(self):
        return self.df.duplicated()

    def get_amount_duplicates(self):
        return self.df.duplicated().sum()
    
    def get_which_missing_values(self):
        return self.df.isnull().sum()
    
    def get_amount_missing_values(self):
        return self.df.isnull().sum().sum()
    
    def get_stats(self):
        return self.df.describe()
    
    def get_info(self):
        return self.df.info()
    
    def get_data_report(self):
        print(self.get_info())

    def get_correlation(self):
        return self.df.corr()
    
    def get_features_datatypes(self):
        return self.df.dtypes

def test():
    filepath2 = "testjson\\banksdata.json"
    df2 = DataFrame(filepath2)
    print(df2.get_duplicates())
    print(df2.get_amount_duplicates())
    print(df2.get_which_missing_values())
    print(df2.get_amount_missing_values())
    print(df2.get_stats())
    print(df2.get_info())
    print(df2.get_features_datatypes())

if __name__ == "__main__":
    test()