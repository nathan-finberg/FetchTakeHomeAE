import json
import pandas as pd

data = []

with open('brands.json') as f:
    for line in f:
        json_line = json.loads(line)
        data.append(json_line)
        
df = pd.json_normalize(data)

row_count = len(df)


# CHECK COLUMNS WHERE NULLS EXIST
null_counts = df.isnull().sum()
print("NULL COUNTS BY COLUMN CHECK: \n\n{}\n\n".format(null_counts))


# CHECK UNIQUENESS OF PK
unique_id_count = df["_id.$oid"].nunique()
print("THERE ARE {0} ROWS IN THIS DATA SET OF WHICH {1} HAVE UNIQUE IDS\n\n".format(row_count,unique_id_count))


# ENSURE DATA TYPES LOOK APPROPRIATE
data_types = df.dtypes
print("DATA TYPES CHECK: \n\n{}\n\n".format(data_types))


# ENSURE ALPHANUMERIC FIELDS LOOK APPROPRIATE
df_copy = df.fillna(0)
is_alphanumeric = df_copy.apply(lambda col: col.str.isalnum().all())
print("ALPHANUMERIC FIELDS LOOK GOOD:\n{}".format(is_alphanumeric))
