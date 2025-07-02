import sys
import pyarrow.parquet as pq
from pyarrow import csv
import pandas as pd
from time import perf_counter
def total_precip(df):
    total = 0.0
    # df_index = df.set_index('parameterId')
    # df_index = df_index.sort_index()
    # df_ten = df_index.loc['precip_past10min']
    # total = df_ten['value'].sum()

    # total = df.apply(lambda row: row['value'] if row['parameterId'] == 'precip_past10min' else 0, axis=1).sum()
    for i in range(len(df)):
        row = df.iloc[i]
        if row['parameterId'] == 'precip_past10min':
            total += row['value']
    return total

def reduce_dmi_df(df):
    df['parameterId'] = df['parameterId'].astype('category')
    return df

if __name__ == '__main__':
    
    fname = sys.argv[1]
    

    table =csv.read_csv(fname)
    df = table.to_pandas()
    reduce_dmi_df(df)
    # print(total_precip(df))
    Start = perf_counter()
    print(total_precip(df.sample(n=100000, random_state=1)))
    print(perf_counter()-Start)
    # pq.write_table(table, "file.parquet")