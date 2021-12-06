import sqlite3
import os.path
from pathlib import Path
import datetime


class DbInquiries:

    def __init__(self):
        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.db_path = os.path.join(self.BASE_DIR, "nutual_db.sqlite3")
        self.conexion = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cursor = self.conexion.cursor()

    def open_conexion(self):
        self.conexion = sqlite3.connect(self.db_path)
        self.cursor = self.conexion.cursor()

    def close_conexion(self):
        if self.cursor:
            self.cursor.close()

        self.conexion.commit()

        if self.conexion:
            self.conexion.close()
            print("conexion close")

    # This method inserts flats data into DB
    def insert_data(self, response):
        try:
            self.delete_nutual_db()
            self.open_conexion()

            for id in response:
                flat_id = id["id"]
                row = self.cursor.execute("SELECT * from nutual_app_pisos where id = ? ", str(flat_id)).fetchone()

                if not row:
                    date_time_str = id["valuation_date"]
                    id["valuation_date"] = datetime.datetime.strptime(date_time_str, '%d/%m/%Y')
                    register = tuple(id.values())
                    self.cursor.execute("INSERT INTO nutual_app_pisos VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", register)

        except Exception as e:
            print("Failed insert data", e)

        finally:
            self.close_conexion()

    # This method returns all flats data registered in DB
    def get_data_nutal_bd(self):
        try:
            self.open_conexion()
            get_all_flats_query = self.cursor.execute("SELECT * from nutual_app_pisos")

            # Turn sql obj into a list
            flat_rows = get_all_flats_query.fetchall()
            return flat_rows

        except Exception as e:
            print("Failed get data", e)

        finally:
            self.close_conexion()

    # Just in case we want to delete all data from DB
    def delete_nutual_db(self):
        self.open_conexion()
        self.cursor.execute("DELETE from nutual_app_pisos")
        self.close_conexion()
