import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression


class DataFrame:
    def __init__(self, filepath: str = None, df: pd.DataFrame = None):
        """
        __init__ constructor for DataFrame class.

        Parameters
        ----------
        filepath : str, optional
            The path to the file containing the data. The default is None.
        df : pd.DataFrame, optional
            The DataFrame containing the data. The default is None.

        Raises
        ------
        ValueError
            If both filepath and df are provided or neither is provided.

        Returns
        -------
        None
        """
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
        """
        Returns a boolean Series denoting duplicate rows.

        Returns
        -------
        Series of bool
            For each element in the DataFrame, True if the row is a duplicate and
            False otherwise.
        """
        return self.df.duplicated()

    def get_amount_duplicates(self):
        """
        Returns the number of duplicate rows in the DataFrame.

        Returns
        -------
        int
            The number of duplicate rows in the DataFrame.
        """
        return self.df.duplicated().sum()
    
    def get_missing_value(self):
        """
        Returns a Series with counts of missing values in each column.

        Returns
        -------
        Series
            A Series with the count of missing values in each column.
        """
        return self.df.isnull().sum()
    
    def get_amount_missing_values(self):
        """
        Returns the total number of missing values in the DataFrame.

        Returns
        -------
        int
            The total count of missing values across all columns in the DataFrame.
        """
        return self.df.isnull().sum().sum()
    
    def get_columns_missing_values(self):
        """
        Returns a list of column names that contain missing values.

        Returns
        -------
        list
            A list of column names that contain missing values.
        """
        return list(self.df.columns[self.df.isnull().any()])
    
    def get_general_stats(self):
        return self.df.describe(include='all')
    
    def get_info(self):
        return self.df.info()
    
    def get_data_report(self):
        return self.get_info(), self.get_stats(), self.get_missing_value(), self.get_amount_missing_values(), self.get_duplicates(), self.get_amount_duplicates()

    def get_correlation(self):
        return self.df.corr()
    
    def get_features_datatypes(self):
        return self.df.dtypes
    
    def categorical_to_numeric(self):
        labelencoder = LabelEncoder()
        onehotencoder = OneHotEncoder()

        for col in self.df.columns:
            if self.df[col].dtype == 'object':
                self.df[col] = labelencoder.fit_transform(self.df[col])
            elif self.df[col].dtype == 'bool':
                self.df[col] = onehotencoder.fit_transform(self.df[col])

        return [labelencoder, onehotencoder]
    
    def fill_column_missing_values(self, column, method="mean"):
        if method == "mean":
            self.df[column] = self.df[column].fillna(self.df[column].mean())
        elif method == "median":
            self.df[column] = self.df[column].fillna(self.df[column].median())
        elif method == "delete":
            self.df[column] = self.df[column].dropna()
        
    


def test():
    filepath2 = "testcsv\\tb_lobby_stats_player.csv"
    df2 = DataFrame(filepath2)
    df2.categorical_to_numeric()
    for col in df2.get_columns_missing_values():
        df2.fill_column_missing_values(col, method="median")
    print(df2.get_general_stats())

    



if __name__ == "__main__":
    test()