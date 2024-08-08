#git config --global user.email "bangaru.bhavyasree@diggibyte.com"
#git config --global user.name "BhavyaSreeBangaru"
import pandas as pd
def add_column(df: pd.DataFrame, column_name: str, data: list) -> pd.DataFrame:
    df[column_name] = data
    return df
def remove_column(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    df = df.drop(columns=[column_name])
    return df
def filter_rows(df: pd.DataFrame, condition: str) -> pd.DataFrame:
    df = df.query(condition)
    return df
def rename_columns(df: pd.DataFrame, columns_dict: dict) -> pd.DataFrame:
    df = df.rename(columns=columns_dict)
    return df
def sum_column(df: pd.DataFrame, column_name: str) -> float:
    return df[column_name].sum()

def filter_by_col(df, col_name, val):
    return df[df[col_name] == val]