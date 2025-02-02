import json
import pandas as pd

data = []

with open('receipts.json') as f:
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


# CHECK VALUES OF PK
non_alphanumerics = len(df[df["_id.$oid"].str.isalnum() == False]["_id.$oid"])
print("NON-ALPHANUMERIC IDS: {}\n\n".format(non_alphanumerics))


# ENSURE DATA TYPES LOOK APPROPRIATE
data_types = df.dtypes
print("DATA TYPES CHECK: \n\n{}\n\n".format(data_types))


# ENSURE DATES LOOK APPROPRIATE
date_cols = ['createDate','dateScanned','modifyDate','finishedDate','pointsAwardedDate','purchaseDate']
has_errors = False

print("DATE COLUMN CHECK:")

for key in date_cols:
    full_key = "{}.$date".format(key)
    try:
        df[full_key] = pd.to_datetime(df[full_key], unit='ms')
    except:
        has_errors = True
    
    max_date = df[full_key].max()
    min_date = df[full_key].min()
    print("COL: {0} MIN: {1} MAX: {2} ERRORS: {3}\n\n".format(full_key,min_date,max_date,has_errors))

    has_errors = False
    

# ENSURE NUMERIC FIELDS LOOK APPROPRIATE
print("NUMERIC FIELD CHECK:\n")
num_cols = ['bonusPointsEarned','pointsEarned','purchasedItemCount','totalSpent']

for key in num_cols:
    df[key] = df[key].fillna(0)
    df[key] = pd.to_numeric(df[key], errors='coerce')
    has_non_numeric = df[key].isnull().any()
    has_positive_values = df[key].ge(0).all()
    print("{0} HAS NON-NUMERIC VALUES? {1}\nHAS ALL POSITIVE VALUES? {2}\n".format(key,has_non_numeric,has_positive_values))


# LOOK INSIDE RECEIPT ITEMS
print("RECEIPT ITEMS:\n\n")
df_explode = df.explode("rewardsReceiptItemList")["rewardsReceiptItemList"]
receipt_item_df = pd.json_normalize(df_explode)
print("COLUMNS: {}".format(receipt_item_df.columns))

