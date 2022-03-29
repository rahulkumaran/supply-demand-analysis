# %%
# Import libraries
import glob
import pandas as pd

# %%
# Import data from files
path        = r'./DATA'
filename    = glob.glob(path + "/*.csv")

allDF       = []
for name in filename:
    allDF.append(pd.read_csv(name))

df          = pd.concat(allDF, ignore_index = True)

# %%
# Data inspection
print(df.head(3))

# %%
# Rename columns in data
cols = []
for col in df.columns:
    cols.append("_".join(col.split()))
df.columns  = cols
print(df.columns)

# %%
print(df.describe())

# %%
# Drop NA/Null values from data
print("Records before dropping NA/null values:", df.shape[0])
df = df.dropna()
print("Records after dropping NA/null values:", df.shape[0])

# %%
# Convert string features to classes
factorMap = {}

strCols     = ["start_station_name", "end_station_name", "usertype"]
datCols     = ["starttime", "stoptime"]
for col in strCols:
    encoded_data, mapping_index = pd.Series(df[col]).factorize()
    factorMap[col] = mapping_index
    df[col] = encoded_data
for col in datCols:
    df[col]= pd.to_datetime(df[col])

# %%
dfNormal = (df - df.min()) / (df.max() - df.min())
print(dfNormal.describe())

# %%
