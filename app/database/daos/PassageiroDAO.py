import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from mysql.connector import IntegrityError

from app.database.entities.Passageiro import Passageiro
from app.database.db import create_connection

class PassageiroDAO:

    @staticmethod
    def login(nome_usuario, senha):
        try:
            passageiro = Passageiro()

            query = """
            SELECT id, nome_usuario, nome, cpf, rg, data_nasc, genero, tipo, endereco
            FROM passageiro
            WHERE nome_usuario = %s and senha = sha2(%s, 512)
            """

            record_tuple = (nome_usuario, senha)

            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(query, record_tuple)

            result_set = cursor.fetchall()

            for row in result_set:
                passageiro.id = row[0]
                passageiro.nome_usuario = row[1]
                passageiro.nome = row[2]
                passageiro.cpf = row[3]
                passageiro.rg = row[4]
                passageiro.data_nascimento = row[5]
                passageiro.genero = row[6]
                passageiro.tipo = row[7]
                passageiro.endereco = row[8]

            connection.commit()
            return passageiro

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

    @staticmethod
    def delete(passageiro):
        try:
            query = """
            DELETE FROM passageiro
            WHERE id = {0}
            """.format(passageiro.id)

            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()

        except mysql.connector.Error as error:
            raise error

        except TypeError:
            raise TypeError

        except AttributeError:
            raise AttributeError

        except mysql.connector.IntegrityError as error:
            raise error

        except mysql.connector.ProgrammingError as error:
            raise error

        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()

    @staticmethod
    def select(passageiro_id):
        try:
            passageiro = Passageiro()

            query = """
            SELECT id, nome_usuario, nome, cpf, rg, data_nasc, genero, tipo, endereco, senha
            FROM passageiro
            WHERE id = {}
            """.format(passageiro_id)

            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(query)

            result_set = cursor.fetchall()

            for row in result_set:
                passageiro.id = row[0]
                passageiro.nome_usuario = row[1]
                passageiro.nome = row[2]
                passageiro.cpf = row[3]
                passageiro.rg = row[4]
                passageiro.data_nascimento = row[5]
                passageiro.genero = row[6]
                passageiro.tipo = row[7]
                passageiro.endereco = row[8]
                passageiro.senha = row[9]

            connection.commit()
            return passageiro

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

    @staticmethod
    def select_all():
        try:
            payload = []

            query = """
            SELECT nome, cpf, rg, data_nasc, genero, tipo, endereco, id
            FROM passageiro
            """

            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(query)

            result_set = cursor.fetchall()

            for row in result_set:
                passageiro = PassageiroModel()

                passageiro.nome = row[0]
                passageiro.cpf = row[1]
                passageiro.rg = row[2]
                passageiro.data_nascimento = row[3]
                passageiro.genero = row[4]
                passageiro.tipo = row[5]
                passageiro.endereco = row[6]
                passageiro.id = row[7]

                payload.append(passageiro)

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
                return payload

    @staticmethod
    def update(passageiro):
        try:
            query = """
            UPDATE passageiro
            SET 
            nome = %s,
            nome_usuario = %s,
            cpf = %s,
            rg = %s,
            data_nasc = %s,
            genero = %s,
            tipo = %s,
            endereco = %s,
            senha = sha2(%s , 512)
            WHERE 
            id = %s
            """
            record_tuple = (
                passageiro.nome,
                passageiro.nome_usuario,
                passageiro.cpf,
                passageiro.rg,
                passageiro.data_nascimento,
                passageiro.genero,
                passageiro.tipo,
                passageiro.endereco,
                passageiro.senha,
                passageiro.id
            )

            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(query, record_tuple)
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

    @staticmethod
    def create(passageiro):
        try:
            query = """
                INSERT INTO
                passageiro(nome, nome_usuario, cpf, rg, data_nasc,
                           genero, tipo, endereco, senha)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, SHA2(%s, 512))
                """
            record_tuple = (
                passageiro.nome,
                passageiro.nome_usuario,
                passageiro.cpf,
                passageiro.rg,
                passageiro.data_nascimento,
                passageiro.genero,
                passageiro.tipo,
                passageiro.endereco,
                passageiro.senha,
            )

            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(query, record_tuple)
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
