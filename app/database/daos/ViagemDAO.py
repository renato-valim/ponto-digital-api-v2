from app.database.entities.Ponto import Ponto
from app.database.db import create_connection

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from mysql.connector import IntegrityError

class ViagemDAO:

    @staticmethod
    def create(viagem):
        try:
            query = """
                INSERT INTO
                viagem (id_passageiro, data, id_ponto_origem, id_ponto_destino, status)
                VALUES (%s, %s, %s, %s, %s)
                """
            record_tuple = (
                viagem._passageiro.id,
                viagem._data,
                viagem._origem.id,
                viagem._destino.id,
                viagem._status
            )

            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(query, record_tuple)
            viagem._id = cursor.lastrowid
            connection.commit()

            return viagem

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