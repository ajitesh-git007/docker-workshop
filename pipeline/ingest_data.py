import pandas as pd
from sqlalchemy import create_engine 
from tqdm.auto import tqdm

year=2021
month=1


url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_{year}-{month:02d}.csv.gz'

df = pd.read_csv(url)

dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

df = pd.read_csv(
    url,
    dtype=dtype,
    parse_dates=parse_dates
)

# df.head()

# uv install sqlalchemy



def run():

    user = "root"
    host = "localhost"
    port = 5432
    db = "ny_taxi"
    password="root"

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")



    # before making table in the database, first we can check the schema of what we are going to push
    # print(pd.io.sql.get_schema(df, name='ny_taxi_dataset', con=engine))

    # here still we have'nt pushed the data, we have only pushed the schema -> df.head[0]
    # df.head(0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')


    #instead of pushing all the data into the db at once, we push chunk wise.
    chunksize=100000
    df_iter = pd.read_csv(
        url,
        dtype=dtype,
        parse_dates=parse_dates,    
        iterator=True,
        chunksize=chunksize,
    )

    first = True
    #pushing into the DB chunk-wise
    for df_chunk in tqdm(df_iter):
        if first == True:
            df.head(0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')
            
            first = False

        df_chunk.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')


if __name__ == '__main__':
    run()

