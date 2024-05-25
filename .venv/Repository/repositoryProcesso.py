import mysql.connector

class ProcessoRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='juridico_np2'
        )
        self.cursor = self.connection.cursor()


    def cadastrar_processo(self, processo):
        self.cursor.execute("INSERT INTO processo (numero, prazo, acusado, acusador) VALUES (%s, %s, %s, %s)",
                            (processo.numero, processo.prazo, processo.acusado, processo.acusador))
        self.connection.commit()
        return True


    def buscar_processos(self):
        self.cursor.execute("SELECT * FROM processo")
        processos = self.cursor.fetchall()
        return processos


    def buscar_processo_por_id(self, id):
        self.cursor.execute("SELECT * FROM processo WHERE id = %s", (id,))
        processo = self.cursor.fetchone()
        return processo


    def editar_processo(self, id, processo):
        if not self.verificar_id_existente(id):
            return None  # Retorna None se o ID nao existe
        else:
            self.cursor.execute("UPDATE processo SET numero = %s, prazo = %s, acusado = %s, acusador = %s WHERE id = %s",
                                (processo.numero, processo.prazo, processo.acusado, processo.acusador, id))
            self.connection.commit()
            return True

    def verificar_id_existente(self, id):
        self.cursor.execute("SELECT id FROM processo WHERE id = %s", (id,))
        result = self.cursor.fetchone()
        return result is not None

    def excluir_processo(self, id):
        if self.processo_existe(id):
            self.cursor.execute("DELETE FROM processo WHERE id = %s", (id,))
            self.connection.commit()
            return True
        else:
            return False


    def processo_existe(self, id):
        self.cursor.execute("SELECT COUNT(*) FROM processo WHERE id = %s", (id,))
        result = self.cursor.fetchone()
        return result[0] > 0


    def __del__(self):
        self.cursor.close()
        self.connection.close()
