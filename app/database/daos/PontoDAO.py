from app.database.entities.Ponto import Ponto
from app.database.db import create_connection

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from mysql.connector import IntegrityError

class PontoDAO:

    @staticmethod
    def select(cod):
        try:
            ponto = Ponto()

            query = """
            SELECT id, cod, nome, lat, lng
            FROM ponto
            WHERE cod = {0}
            """.format(cod)

            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(query)

            result_set = cursor.fetchall()

            for row in result_set:
                ponto.id = row[0]
                ponto.cod = row[1]
                ponto.nome = row[2]
                ponto.lat = row[3]
                ponto.lng = row[4]

            connection.commit()
        except mysql.connector.Error as error:
            raise error
        except TypeError:
            raise TypeError
        except AttributeError:
            raise AttributeError
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                return ponto
