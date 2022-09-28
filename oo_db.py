import sqlite3

__DATABASE_NAME = "actress_oo.db"
__DEFAULT_TABLE = "actress"

def __init__(self):
    global database = sqlite3.connect(__DATABASE_NAME)
    global cursor = database.cursor()
    db_table_create()


def db_table_create(self, table_name = __DEFAULT_TABLE):
    """
        Legt die Tabelle an; achtet darauf, dass diese nur einmal vorkommt.
        Funktion kann also immer aufgerufen werden.
    """
    cursor.execute("CREATE TABLE IF NOT EXISTS {?} (vorname varchar, nachname varchar, gebdatum date, heart INTEGER)", table_name)


def crud_insert(self, table_name = __DEFAULT_TABLE):
    """
        INSERT INTO auf Basis eines einzelnen vollständigen Datensatzes.
    """
    self.table_name = table_name
    # insert into
    database.commit()


def crud_select(self, order_by, table_name = __DEFAULT_TABLE):
    """
        'SELECT ROWID, *' der übergebenen Tabelle sortiert ASC
    """
    self.table_name = table_name
    self.order_by = order_by
    # selcet
    # return als Liste


def crud_update(self, id, table_name = __DEFAULT_TABLE):
    """
        UPDATE eines einzelnen Datensatzes auf Basis der ROWID
        in der übergebenen Tabelle
    """
    self.id = id
    self.table_name = table_name
    #
    database.commit()



def crud_delete(self, id):
    """
        Löschung eines einzelnen Datensatzes auf Basis der übergebenen ID
    """
    self.id = id
    #
    database.commit()


def crud_insert_many(self, insert_list, table_name = __DEFAULT_TABLE):
    self.insert_list = insert_list
    self.table_name = table_name
    #
    database.commit()
