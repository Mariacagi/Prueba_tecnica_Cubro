import pandas as pd
# from varname import nameof
# from varname.helpers import Wrapper

def changing_dates(df, name_column): 
    """Changing the date type to datatime"""
    df[name_column] = df[name_column].astype('datetime64[ns]')


def split_column(df, column, separation_object, times):
    """Split a column of a dataframe"""
    df[column] = df[column].str.split(separation_object, n=times, expand=True)


def check_dupli_nan(df_name, df):
    """Checkinf if there is any duplicate or any null"""
    print(df_name, "duplicates", "---->", df.duplicated().values.any())
    print(df_name, "null",  "---->", df.isnull().values.any())
    print("-------------------------- \n")