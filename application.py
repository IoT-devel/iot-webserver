from collections import namedtuple

from flask import Flask, render_template, request, url_for
import MySQLdb
from flask import jsonify

from constants import *

app = Flask(__name__)
app.jinja_env.globals['static'] = (lambda filename: url_for('static', filename=filename))

DataItem = namedtuple('DataItem', ['iid', 'temperature', 'datetime'])


@app.route('/')
def temper():
    return render_template('temperature.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/rest/new_data', methods=['GET'])
def temp():
    db = MySQLdb.connect(DB_HOST, DB_USERNAME, DB_PASSWORD, DB_DATABASE)
    cursor = db.cursor()
    data = None

    try:
        cursor.execute(SELECT_ONE_DATA)
        data = cursor.fetchone()
    except:
        pass
    finally:
        db.close()

    import datetime
    # data[2] = datetime.datetime.now()
    iid = data[0] + 1
    return jsonify(DataItem(iid=data[0], temperature=(float(data[1])/10), datetime=str(data[2]))._asdict())


@app.route('/rest/old_data', methods=['GET'])
def last_temps():
    db = MySQLdb.connect(DB_HOST, DB_USERNAME, DB_PASSWORD, DB_DATABASE)
    cursor = db.cursor()
    items = {}
    count = request.args.get('count', 100)

    try:
        cursor.execute(SELECT_LAST_TEN_DATA.format(count=count))
        data_all = cursor.fetchall()
    except:
        pass
    finally:
        db.close()

    for _index, data in enumerate(reversed(data_all)):
        items[_index] = DataItem(iid=data[0], temperature=(float(data[1])/10), datetime=str(data[2]))._asdict()

    return jsonify(items)


if __name__ == '__main__':
    app.debug = False
    app.run()
    #app.run(host='0.0.0.0', port=8100)
