from flask import render_template, url_for, redirect, g, request
from app import app
from .forms import TaskForm
import json

#now we will import our rethinkdb
import rethinkdb as rdb
from rethinkdb.errors import RqlRuntimeError, RqlDriverError

r = rdb.RethinkDB()

rdbhost = "localhost"
rdbport = 28015
dbname = "todo"

def dbSetup():
    connection = r.connect(host=rdbhost, port=rdbport)
    try:
        r.db_create(dbname).run(connection)
        r.db(dbname).table_create('todo').run(connection)
        print('Set up for DataBase complete')
    except RqlRuntimeError:
        print("Database alread exists.")
    finally:
        connection.close()
dbSetup()

# open connection before each request
@app.before_request
def before_request():
    try:
        g.rdb_conn = r.connect(host=rdbhost, port=rdbport, db=dbname)
    except:
        abort(503, "Database conection couldn't be established, please try again.")

# close the connection after each request
@app.teardown_request
def teardown_request(exception):
    try:
        g.rdb_conn.close()
    except AttributeError:
        pass

@app.route('/', methods=['GET','POST'])
def index():
    form = TaskForm()
    if form.validate_on_submit():
        r.table('todo').insert({"name": form.label.data}).run(g.rdb_conn)
        return redirect(url_for('index'))
    selection = list(r.table('todo').run(g.rdb_conn))
    return render_template('index.html', form = form, tasks = selection)

