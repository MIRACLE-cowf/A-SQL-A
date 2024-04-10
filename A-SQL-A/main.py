from Util.db_loader import load_db

if __name__ == '__main__':
    db_name = input("Enter database name that conversation with LLM: ")
    db = load_db(db_name)
    if db is None:
        exit(1)

    print(db.get_usable_table_names())