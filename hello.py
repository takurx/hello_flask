from flask import Flask, render_template
import pymysql

app = Flask(__name__)

@app.route('/')
def hello():
    #db setting
    db = pymysql.connect(
            host='localhost',
            user='dbtest',
            password='root',
            db='testdb',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
        )
    
    cur = db.cursor()
    sql = "select * from testdb.members"
    cur.execute(sql)
    members = cur.fetchall()

    cur.close()
    db.close()
    
    name = "Hoge"
    return render_template('hello.html', title='flask test', members=members)

@app.route('/good')
def good():
    name = "Good"
    return name

## おまじない
if __name__ == "__main__":
    app.run(debug=True)