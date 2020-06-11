import sqlite3

class DatabaseUtil:
    DB_LOCATION = 'database.db'

    def __init__(self):
        # Init Attributes
        self.conn = sqlite3.connect(DatabaseUtil.DB_LOCATION)
        # Set returned results to be in list instead of tuple
        self.conn.row_factory = lambda cursor, row: list(row)
        self.cur = self.conn.cursor()
        self.createTable()

    def createTable(self):
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS 
        employee(
            id TEXT PRIMARY KEY,
            login TEXT NOT NULL UNIQUE, 
            name TEXT NOT NULL, 
            salary REAL NOT NULL
            );''')

    def getEmployeeDashboardCount(self, params, sorting):
        # Can't seem to parameterize the column name and ASC DESC correctly, resorting to this in the meantime
        self.cur.execute('''
        SELECT COUNT(1) FROM employee WHERE salary >= ? AND salary <= ? ORDER BY ''' + sorting + ''' LIMIT ? OFFSET ?;''', params)
        return self.cur.fetchall()

    def getEmployeeDashboard(self, params, sorting):
        # Can't seem to parameterize the column name and ASC DESC correctly, resorting to this in the meantime
        self.cur.execute('''
        SELECT * FROM employee WHERE salary >= ? AND salary <= ? ORDER BY ''' + sorting + ''' LIMIT ? OFFSET ?;''', params)
        return self.cur.fetchall()
    
    def getAllEmployeeLogins(self):
        self.cur.execute('''
        SELECT id, login FROM employee;''')
        return self.cur.fetchall()

    def insertEmployees(self, employeeList):
        try:
            self.cur.executemany('''
            INSERT OR REPLACE INTO employee ('id', 'login', 'name', 'salary') 
            VALUES (?, ?, ?, ?);''', employeeList)
            self.conn.commit()
            return 1
        except Exception as e:
            self.conn.rollback()
            print(e)
            return 0

    def close(self):
        self.cur.close()
        self.conn.close()