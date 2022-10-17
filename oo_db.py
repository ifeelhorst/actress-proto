import sqlite3

class DefaultDatabase():

    _DATABASE_NAME = "actress_oo.db"
    _DEFAULT_TABLE = "actress"
    connection = None
    cursor = None

    def __init__(self, db_name = _DATABASE_NAME):
        self.db_name = db_name
        self.connection= sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()


    def db_table_create(self, table_name = _DEFAULT_TABLE):
        """
            Legt die Tabelle an; achtet darauf, dass diese nur einmal vorkommt.
            Funktion kann also immer aufgerufen werden.
        """
        self.table_name = table_name
        sql_query = "CREATE TABLE IF NOT EXISTS " + table_name + " (vorname varchar, nachname varchar, gebdatum date, heart INTEGER)"
        self.cursor.execute(sql_query)


    def crud_insert(self, table_name = _DEFAULT_TABLE):
        """
            INSERT INTO auf Basis eines einzelnen vollständigen Datensatzes.
        """
        self.table_name = table_name
        # insert into
        connection.commit()


    def crud_select(self, order_by, table_name = _DEFAULT_TABLE):
        """
            'SELECT ROWID, *' der übergebenen Tabelle sortiert ASC
        """
        self.table_name = table_name
        self.order_by = order_by
        # selcet
        # return als Liste


    def crud_update(self, id, table_name = _DEFAULT_TABLE):
        """
            UPDATE eines einzelnen Datensatzes auf Basis der ROWID
            in der übergebenen Tabelle
        """
        self.id = id
        self.table_name = table_name
        #
        connection.commit()



    def crud_delete(self, id):
        """
            Löschung eines einzelnen Datensatzes auf Basis der übergebenen ID
        """
        self.id = id
        #
        connection.commit()


    def crud_insert_many(self, insert_list, table_name = _DEFAULT_TABLE):
        self.insert_list = insert_list
        self.table_name = table_name
        #
        connection.commit()
