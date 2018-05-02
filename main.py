#! python2
from flask import Flask, render_template
import mysql.connector
from mysql.connector import errorcode

app = Flask(__name__)

# connection = mysql.connector.connect(user='admin',
#                                      password= 'admin',
#                                      host='127.0.0.1',
#                                      port='3306',
#                                      database = 'multivender_test')
# cursor = connection.cursor()

@app.route("/")
def main():
    return render_template('index.html')

# @app.route("/get_data", methods=['POST', 'GET'])
# def get_data():
#     console.log("clicked")
#     sql = ('select * from volume_dicominfo');
#     cursor.execute(sql)
#     rows = cursor.fetchone()
#     return render_template('index.html', message=rows)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
