import sys
import pyarrow.parquet as pq
from pyarrow import csv
import pandas as pd
from time import perf_counter
def total_precip(table):
    df = table.to_pandas()
    total = df[df['parameterId'] == 'precip_past10min']['value'].sum()
    return total

# def reduce_dmi_df(df):
#     df['parameterId'] = df['parameterId'].astype('category')
#     return df

if __name__ == '__main__':
    
    fname = sys.argv[1]

    pqc = pq.ParquetFile(fname)
    total = 0
    for i in range(pqc.num_row_groups):
        row_group = pqc.read_row_group(i)
        total += total_precip(row_group)
    print(total)
    # Start = perf_counter()
    # print(total_precip(dfc))
    # print(perf_counter()-Start)
    # pq.write_table(table, "file.parquet")