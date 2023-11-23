from flask import Flask, render_template
from flask import request, redirect, url_for
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
        db = 'datadb',
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

#menambah data baru
@app.route('/add/')
def add():
    return render_template('add.html')

#proses menambah data baru
@app.route('/proses_add/', methods=['POST'])
def proses_add():
    nim = request.form['nim']
    nama = request.form['nama']
    kelas = request.form['kelas']
    prodi = request.form['prodi']
    cur = db.cursor()
    cur.execute('INSERT INTO datakel4 (nim, nama, kelas, prodi) VALUES (%s, %s, %s, %s)', (nim, nama, kelas, prodi))
    db.commit()
    return redirect(url_for('add'))

#menhapus data
@app.route('/delete/')
def delete():
    return render_template('delete.html')

#proses menghapus data
@app.route('/proses_delete/', methods=['POST'])
def proses_delete():
    nim = request.form['nim']
    cur = db.cursor()
    cur.execute('DELETE FROM datakel4 WHERE nim=%s', (nim,))
    db.commit()
    return redirect(url_for('delete'))

#result data
@app.route('/result/')
def result():
    cursor = db.cursor()
    cursor.execute('select * from datakel4')
    res = cursor.fetchall()
    cursor.close()
    return render_template('result.html',hasil = res)

if __name__ == '__main__':
    app.run(debug=True)
