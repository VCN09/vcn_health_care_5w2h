import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tarefas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            what VARCHAR(255),
            why VARCHAR(255),
            wher VARCHAR(255),
            whe VARCHAR(255),
            who VARCHAR(255),
            how VARCHAR(255),
            how_much VARCHAR(255),
            priority VARCHAR(255),
            statu VARCHAR(255)
        )''')

    def insert_task(self, tarefa):
        sql = '''INSERT INTO tarefas (what, why, where, when, who, how, how_much, priority, status) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        values = (tarefa.what, tarefa.why, tarefa.wher, tarefa.whe, tarefa.who, tarefa.how, tarefa.how_much,
                  tarefa.priority, tarefa.statu)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def fetch_tasks(self):
        self.cursor.execute("SELECT * FROM tarefas")
        return self.cursor.fetchall()
