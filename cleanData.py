import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
import math
from dateutil.parser import parse

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
        return self.get_info(), self.get_missing_value(), self.get_amount_missing_values(), self.get_duplicates(), self.get_amount_duplicates()

    def get_correlation(self):
        """
        Writes the correlation between columns in the DataFrame to a csv file.

        The correlation between columns in the DataFrame is computed using the corr() method.
        The result is then written to a csv file named "correlation.csv".

        Returns
        -------
        None
        """
        
        return self.df.corr().to_csv("correlation.csv")
    
    def get_features_datatypes(self):
        return self.df.dtypes
    
    def is_DateTime(self, column):
        try:
            parse(self.df[column][0])
            return True
        except ValueError:
            return False
    
    def removeFormatting(self):
        for col in self.df.columns:
            if self.df[col].dtype == 'object':
                #Date and Time
                if self.is_DateTime(col):
                    self.df[col] = self.df[col].astype('datetime64[ns]')
                
                #Money
                elif not self.df[col].str.contains('[a-zA-Z]').any():
                    self.df[col] = self.df[col].str.replace(',', '').astype(float)

                else:
                    #General Strings
                    self.df[col] = self.df[col].str.lower()
                    self.df[col] = self.df[col].str.replace(" ", "")

            
            
    
    def categorical_to_numeric(self):
        """Converts categorical and boolean columns in the DataFrame to numeric values using encoding.

        This function identifies columns with 'object' or 'bool' data types and applies:
        - Label Encoding for categorical columns, replacing categories with integer labels.
        - One-Hot Encoding for boolean columns, converting them into binary integer arrays.
        
        The mappings of original values to numeric representations are stored in a dictionary
        and saved as a JSON file named 'categoricalFeaturesConversion.json'.

        Returns
        -------
        dict
            A dictionary containing the mappings of original categorical and boolean values
            to their respective encoded numeric values for each column."""


        categorical_dict = {}
        for col in self.df.columns:
            labelencoder = LabelEncoder()
            onehotencoder = OneHotEncoder()
            if self.df[col].dtype == 'object':
                #storing the mapping
                unique_values = self.df[col].unique()
                encoded_values = labelencoder.fit_transform(unique_values)
                integer_values = [int(label) for label in encoded_values]
                categorical_dict[col] = dict(zip(unique_values, integer_values))

                #transform categorical features into inetegers using label encoding
                self.df[col] = labelencoder.fit_transform(self.df[col])

            elif self.df[col].dtype == 'bool':
                #storing the mapping
                unique_values = self.df[col].unique()
                encoded_values = onehotencoder.fit_transform(unique_values.reshape(-1, 1))
                categorical_dict[col] = dict(zip(unique_values, encoded_values.astype(int)))

                #transform categorical features into inetegers using label encoding
                self.df[col] = onehotencoder.fit_transform(self.df[col])

        with open("categoricalFeaturesConversion.json", "w") as f:
            json.dump(categorical_dict, f, indent=4)

        return categorical_dict
    
    def fill_column_missing_values(self, column, method="mean"):
        """
        Fills missing values in a specified column using a selected method.

        Parameters
        ----------
        column : str
            The name of the column in which missing values are to be filled.
        method : str, optional
            The method to use for filling missing values ('mean' or 'median').
            The default is 'mean'.

        Notes
        -----
        This function only fills missing values for columns with numeric data types.
        If the column is of object type, no action is taken.
        """

        if self.df[column].dtype == 'object':
            pass
        if method == "mean" and self.df[column].dtype != 'object':
            self.df[column] = self.df[column].fillna(self.df[column].mean())
        elif method == "median" and self.df[column].dtype != 'object':
            self.df[column] = self.df[column].fillna(self.df[column].median())

    def removeDuplicates(self):
        self.df.drop_duplicates(inplace=True)

    def removeNaN(self):
        self.df.dropna(inplace=True)

    
    def generate_sample_size(self, population = 100, confidence_level=0.95, margin_of_error=0.05) -> int:
        """
        Calculates the ideal sample size based on Simple Random Sampling.
        
        Parameters
        ----------
        population : float, optional
            proportion of the population with the characteristic of interest. The default is 100.
        confidence_level : float, optional
            The desired confidence level. The default is 0.95.
        margin_of_error : float, optional
            The desired margin of error. The default is 0.05.
        
        Returns
        -------
        int
            The ideal sample size.
        """
        if population <= 0 or (confidence_level <= 0 or confidence_level >= 1) or (margin_of_error <= 0 or margin_of_error >= 1):
            raise ValueError("All inputs must be greater than 0")
        

        confidence_level =  1-(1-confidence_level)/2
        with open("randomSample.json", "r") as f:
            data = json.load(f)
        
        temp_confidence_level = data["values"][str(confidence_level)]
        equation = (((temp_confidence_level**2) * 0.5 * (1-0.5))/(margin_of_error**2))/(1+((temp_confidence_level**2 * 0.5 *(1-0.5)))/(margin_of_error**2*population))
        
        return math.ceil(equation)
        
    def check_df_size(self, population = 100, confidence_level=0.95, margin_of_error=0.05) -> bool:
        return self.generate_sample_size(population, confidence_level, margin_of_error) < self.df.shape[0]
    
    def validate_data(self) -> bool:
        """- Types of data validation
        Data type - Check that the data matches the data type defined for a field.

        Data range - Check that the data falls within an acceptable range of values defined for the field.

        Data constraints -  Check that the data meets certain conditions or criteria for a field

        Data consistency -  Check that the data meets certain conditions or criteria for a field

        Data Structure - Check that the data follows or conforms to a set structure

        Code validation - Check that the application code systematically performs any of the previously mentioned validations during user data input."""
        
        #Datatype
        for col in self.df.columns:
            if self.df[col].dtype == 'object':
                self.df[col] = self.df[col].astype(str)
            
            elif self.df[col].dtype == 'bool':
                self.df[col] = self.df[col].astype(int)

        #Data range

        #Data constraints

        #Data consistency

        #Data Structure


        return True
    
    def getSample(self):
        return self.df.sample()

    def getHead(self, n = 5):
        return self.df.head(n)

    def toCsv(self, filename):
        return self.df.to_csv(filename)
    
    def to_Xlsx(self, filename):
        return self.df.to_excel(filename)


def test():
    filepath2 = "testcsv\\tb_lobby_stats_player.csv"
    filepath3 = "testjson\\banksdata.json"

    df2 = DataFrame(filepath2)
    df2.get_data_report()
    df2.removeFormatting()
    df2.removeDuplicates()
    for col in df2.get_columns_missing_values():
        df2.fill_column_missing_values(col, method="median")

    df2.categorical_to_numeric()
    df2.get_data_report()

    print(df2.get_correlation())

if __name__ == "__main__":
    test()