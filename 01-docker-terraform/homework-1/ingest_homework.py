#!/usr/bin/env python
# coding: utf-8

import click
import pandas as pd
from sqlalchemy import create_engine

GREEN_TAXI_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet"
TAXI_ZONES_URL = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv"

def ingest_file(url, engine, table_name):
    print(f"--- Processing {url} to table '{table_name}' ---")
    
    if url.endswith('.parquet'):
        df = pd.read_parquet(url)
    elif url.endswith('.csv'):
        df = pd.read_csv(url)
    else:
        print(f"Skipping {url}: Format not supported.")
        return

    # Insert to SQL
    df.to_sql(name=table_name, con=engine, if_exists='replace')
    print(f"Suceed! {len(df)} rows inserted to table '{table_name}'.\n")


@click.command()
@click.option('--user', default='root', help='Postgres User')
@click.option('--password', default='root', help='Postgres Password')
@click.option('--host', default='localhost', help='Postgres Host')
@click.option('--port', default='5432', help='Postgres Port')
@click.option('--db', default='ny_taxi', help='Postgres Database name')
def main(user, password, host, port, db):
    
    # Setup Koneksi
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    print(f"Connected to database: {db} at localhost:{port}")

    # 1. Ingest Green Taxi (Parquet)
    ingest_file(GREEN_TAXI_URL, engine, 'green_taxi_data')

    # 2. Ingest Zones (CSV)
    ingest_file(TAXI_ZONES_URL, engine, 'taxi_zones')

    print("All data received!")

if __name__ == '__main__':
    main()