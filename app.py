from server import get_cursor
from flask import Flask

cursor = get_cursor()


app = Flask(__name__)

@app.route('/companies')
def getAllCompanies():
    cursor.execute("SELECT * FROM companies")
    columns = [desc[0] for desc in cursor.description]
    records = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return records


@app.route('/companies/<id>')
def getCompany(id):
    cursor.execute(f"SELECT id, name, sector FROM companies WHERE id = '{id}'")    
    columns = [desc[0] for desc in cursor.description]
    records = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return records

if __name__ == '__main__':
    app.run(debug=True, port=5000)