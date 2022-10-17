from oo_db import DefaultDatabase
from oo_actress import Actress

def main():
    db_instanz = DefaultDatabase()
    db_instanz.db_table_create()


if __name__ == '__main__':
    main()
