import mysql.connector

class DefensorRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='juridico_np2'
        )
        self.cursor = self.connection.cursor()


    def cadastrar_defensor(self, defensor):
        self.cursor.execute("INSERT INTO defensor (nome, especialidade, vara, salario) VALUES (%s, %s, %s, %s)",
                            (defensor.nome, defensor.especialidade, defensor.vara,defensor.salario))
        self.connection.commit()
        return True


    def buscar_defensores(self):
        self.cursor.execute("SELECT * FROM defensor")
        defensores = self.cursor.fetchall()
        return defensores


    def buscar_defensor_por_id(self, id):
        self.cursor.execute("SELECT * FROM defensor WHERE id = %s", (id,))
        defensor = self.cursor.fetchone()
        return defensor


    def editar_defensor(self, id, defensor):
        if not self.verificar_id_existente(id):
            return None  # Retorna None se o ID nao existe
        else:
            self.cursor.execute("UPDATE defensor SET Nome = %s, especialidade = %s, vara = %s, salario = %s WHERE id = %s",
                                (defensor.nome, defensor.especialidade, defensor.vara, defensor.salario, id))
            self.connection.commit()
            return True

    def verificar_id_existente(self, id):
        self.cursor.execute("SELECT id FROM defensor WHERE id = %s", (id,))
        result = self.cursor.fetchone()
        return result is not None

    def excluir_defensor(self, id):
        if self.defensor_existe(id):
            self.cursor.execute("DELETE FROM defensor WHERE id = %s", (id,))
            self.connection.commit()
            return True
        else:
            return False


    def defensor_existe(self, id):
        self.cursor.execute("SELECT COUNT(*) FROM defensor WHERE id = %s", (id,))
        result = self.cursor.fetchone()
        return result[0] > 0


    def __del__(self):
        self.cursor.close()
        self.connection.close()
