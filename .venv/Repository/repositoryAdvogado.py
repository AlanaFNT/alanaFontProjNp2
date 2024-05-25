import mysql.connector

class AdvogadoRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='juridico_np2'
        )
        self.cursor = self.connection.cursor()


    def cadastrar_advogado(self, advogado):
        self.cursor.execute("INSERT INTO advogado (nome, especialidade, escritorio, salario) VALUES (%s, %s, %s, %s)",
                            (advogado.nome, advogado.especialidade, advogado.escritorio, advogado.salario))
        self.connection.commit()
        return True


    def buscar_advogados(self): 
        self.cursor.execute("SELECT * FROM advogado")
        advogados = self.cursor.fetchall()
        return advogados


    def buscar_advogado_por_id(self, id):
        self.cursor.execute("SELECT * FROM advogado WHERE id = %s", (id,))
        advogado = self.cursor.fetchone()
        return advogado


    def editar_advogado(self, id, advogado):
        if not self.verificar_id_existente(id):
            return None  # Retorna None se o ID nao existe
        else:
            self.cursor.execute("UPDATE advogado SET nome = %s, especialidade = %s, escritorio = %s, salario = %s WHERE id = %s",
                                (advogado.nome, advogado.especialidade, advogado.escritorio, advogado.salario, id))
            self.connection.commit()
            return True

    def verificar_id_existente(self, id):
        self.cursor.execute("SELECT id FROM advogado WHERE id = %s", (id,))
        result = self.cursor.fetchone()
        return result is not None

    def excluir_advogado(self, id):
        if self.advogado_existe(id):
            self.cursor.execute("DELETE FROM advogado WHERE id = %s", (id,))
            self.connection.commit()
            return True
        else:
            return False


    def advogado_existe(self, id):
        self.cursor.execute("SELECT COUNT(*) FROM advogado WHERE id = %s", (id,))
        result = self.cursor.fetchone()
        return result[0] > 0


    def __del__(self):
        self.cursor.close()
        self.connection.close()
