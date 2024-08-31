import pandas as pd
import psycopg2
from sqlalchemy import create_engine

def process_data(engine):
    conn = engine.connect()

    data = pd.read_sql("select * from employees", conn)
    return data


if __name__ == "__main__":
    db_user = 'postgres'
    db_password = 'password'
    db_host = 'db'
    db_port = '5432'
    db_name = 'kuntsev_task2'

    engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

    result = process_data(engine)
    df = pd.DataFrame(result)
    print("Employees:")
    for row in result.itertuples():
        print(f"ID: {getattr(row, 'id')}, Name: {getattr(row, 'name')}, Age: {getattr(row, 'age')}, Department: {getattr(row, 'department')}")
    

