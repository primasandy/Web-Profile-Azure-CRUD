from flask import Flask, render_template
import pymysql
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

try :
    db = pymysql.connect(
        host = 'sqlkel4demo.mysql.database.azure.com',
        user = 'sqlkel4demo',
        password = 'primajr1234@_#',
        db = 'kel4',
        ssl = {'ca' :os.getenv("SSL")}
    )
    print('berhasil konek ke database')
    print(os.getenv('DB_NAME'))
except Exception as err:
    print(f'gagal konek ke database, error: {err}')

#home
@app.route('/')
def home():
    return render_template('intro.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/portofolio')
def portofolio():
    return render_template('portofolio.html')

@app.route('/result/')
def result():
    cursor = db.cursor()
    cursor.execute('select * from kelompok4')
    res = cursor.fetchall()
    cursor.close()
    return render_template('result.html',hasil = res)

if __name__ == '__main__':
    app.run(debug=True)
