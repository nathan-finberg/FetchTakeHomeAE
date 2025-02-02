import json
import pandas as pd

data = []

with open('users.json') as f:
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


# ENSURE STATES ARE VALID
states_territories_code_list = [
  "AL","AK","AZ","AR","CA","CZ","CO","CT","DE","DC","FL","GA","GU","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO",
  "MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","PR","RI","SC","SD","TN","TX","UT","VT","VI","VA","WA","WV","WI","WY"
]

all_valid_states = df[df["state"].isnull() == False]["state"].isin(states_territories_code_list).all()
print("ALL STATES AND TERRITORIES ARE VALID: {}\n\n".format(all_valid_states))


# ENSURE ROLE DATA IS CORRECT
unique_values = df["role"].unique()
print("UNIQUE ROLES: {}\n\n".format(unique_values))


# ENSURE DATES LOOK APPROPRIATE
date_cols = ["createdDate","lastLogin"]
has_errors = 0

print("DATE COLUMN CHECK:")

for key in date_cols:
    full_key = "{}.$date".format(key)
    try:
        df[full_key] = pd.to_datetime(df[full_key], unit='ms')
    except:
        has_errors = True
    
    max_date = df[full_key].max()
    min_date = df[full_key].min()
    print("COL: {0} MIN: {1} MAX: {2} ERRORCOUNT: {3}\n".format(full_key,min_date,max_date,has_errors))

    has_errors = False


