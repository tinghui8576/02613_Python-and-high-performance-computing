import sys
import pyarrow.parquet as pq
from pyarrow import csv
import pandas as pd
from time import perf_counter
def total_precip(dfc):
    total = 0.0
    

    for df in dfc:
        df_index = df.set_index('parameterId')
        df_index = df_index.sort_index()
        df_ten = df_index.loc['precip_past10min']
        total += df_ten['value'].sum()

    return total

# def reduce_dmi_df(df):
#     df['parameterId'] = df['parameterId'].astype('category')
#     return df

import pyarrow as pa
if __name__ == '__main__':
    
    fname = sys.argv[1]
    chunk = sys.argv[2]

    dfc =pd.read_csv(fname, chunksize=int(chunk))
    first = True
    for df in pd.read_csv(fname, chunksize=int(chunk)):
        table = pa.Table.from_pandas(df)
        if first:
            writer = pq.ParquetWriter("file.parquet", table.schema)
            first = False
        writer.write_table(table)

    # reduce_dmi_df(df)
    # print(total_precip(df))
    # Start = perf_counter()
    # print(total_precip(dfc))
    # # print(perf_counter()-Start)
    # pq.write_table(table, "file.parquet")