"""
Action for converting source raw data to RFM model schema
Inputs:
    - data: Source data in the form of Dataframe
    -physiographic_column_info: List of screens in the form of dataframe

Output:
    - Dataframe in the form of RFM model schema
"""
import traceback
import pandas as pd
from dft.base_execution_handler import BaseExecutionHandler


class ExecutionHandler(BaseExecutionHandler):
    def execute(self, data, physiographic_column_info):

        try:
            table = data
            print(table.shape[0])
            physiographic_columns = physiographic_column_info['Personality Trait']
            for old, new in zip(table.columns[1:], physiographic_columns):
                table.rename({old: new}, axis=1, inplace=True)
            print(table.shape[0])
            for col in table.columns[1:]:
                table[col] = table[col].map(lambda x: 'Disagree' if x <= 2 else ('Neutral' if x == 3 else 'Agree'))
            print(table.shape[0])
            return table
        except Exception as e:
            print(e)
            print(traceback.format_exc())