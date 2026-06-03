import sys 
import pandas as pd
print("Hello Pipeline") 

# print("arguements", sys.argv)

# month = int(sys.argv[1]) 

# print(f"Month: {month}") 

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(df)

df.to_parquet(f"output_day_{sys.argv[1]}.parquet")

month = int(sys.argv[1])

df['month'] = month 
print(df) 