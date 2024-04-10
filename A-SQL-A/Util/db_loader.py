import os
import pandas as pd
from sqlalchemy import create_engine
from langchain_community.utilities.sql_database import SQLDatabase

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def create_dot_db_from_csv(_csv_file_path: str, _db_name: str) -> None:
    df = pd.read_csv(_csv_file_path)
    engine = create_engine(f"sqlite:///" + os.path.join(parent_dir, 'src/db', f'{_db_name}.db'))
    df.to_sql(_db_name, engine, index=False)


def load_db(db_name: str) -> SQLDatabase | None:
    db_path = os.path.join('src/db/', f'{db_name}.db')
    if not os.path.exists(db_path):
        csv_file_name = input('Enter the only "csv" file "name" to convert into database: ')
        csv_file_path = os.path.join('src/csv', f'{csv_file_name}.csv')
        if os.path.exists(csv_file_path):
            create_dot_db_from_csv(csv_file_path, db_name)
            print(f"Successfully converted {csv_file_name}.csv into {db_name}.db!")
        else:
            print(f"File {csv_file_name}.csv does not exist!")
            return None

    print(f"Load {db_name}.db successfully!")
    return SQLDatabase.from_uri(f"sqlite:///" + os.path.join(parent_dir, "src/db", f"{db_name}.db"))