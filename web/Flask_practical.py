

from flask import Flask, render_template, jsonify,g,abort
import functools
import json
import sqlalchemy as sqla
from sqlalchemy import create_engine, text
import traceback
import glob
import os
from pprint import pprint
import json
import requests
import time
from IPython.display import display
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime, timedelta
import pymysql
pymysql.install_as_MySQLdb()

#from jinjia2 import Template
#from flask_sqlalchemy import SQLAlchemy
#from flask_mysqldb import MySQL
# app=Flask(__name__)


app=Flask(__name__, static_url_path='')
#app.config.from_object('config')

url = "dbikes.cznzccwi0urk.us-east-1.rds.amazonaws.com"
user = "admin"
database= "dbikes"
port = "3306"
password = "Foryiuxing18!"

#engine = create_engine(f"mysql+mysqldb://{user}:{password}@{url}:{port}/{database}", echo=True)
#engine = create_engine(f"mysql+mysqldb://{user}:{password}@{url}:{port}/{database}", echo=True)

def connect_to_database():
    
    #return engine = create_engine("mysql://{user}:{password}@{url}:{port}/{database}".format(config.USER, config.PASSWORD, config.URI, config.PORT, config.DB), echo=True)
    #engine = create_engine("mysql://{user}:{password}@{url}:{port}/{database}".format(user, password, url, port, database), echo=True)
    #engine = create_engine(f"mysql+mysqldb://{user}:{password}@{url}:{port}/{database}", echo=True)
    engine = create_engine(f"mysql+mysqldb://{user}:{password}@{url}:{port}/{database}", echo=True)
    return engine
    
def get_db(): 
    db = getattr(g, '_database', None) 
    if db is None: 
        db = g._database = connect_to_database() 
    return db

def get_db_raw(): 
    db2 = getattr(g, '_database', None) 
    if db2 is None: 
        db2 = g._database = connect_to_database().raw_connection() 
    return db2

@app.teardown_appcontext 
def close_connection(exception): 
    db = getattr(g, '_database', None) 
    if db is not None: 
        db.close() 
 


@app.route("/stations")
@functools.lru_cache(maxsize=128)
def get_stations():
    engine = get_db()
    sql = "select * from station ;"
    try:
        with engine.connect() as conn:
            rows = conn.execute(text(sql)).fetchall()
            print('#found {} stations', len(rows), rows)
            # use this formula to turn the rows into a list of dicts
            return jsonify([row._asdict() for row in rows])
    except:
        print(traceback.format_exc())
        return "error in get_stations", 404
    
    
@app.route("/availability")
@functools.lru_cache(maxsize=128)
def get_availability():
    engine = get_db()
    sql = "SELECT * FROM availability;"
    try:
        with engine.connect() as conn:
            rows = conn.execute(text(sql)).fetchall()
            print('Found {} availability entries', len(rows), rows)
            return jsonify([row._asdict() for row in rows])
    except:
        print(traceback.format_exc())
        return "error in get_availability", 404
    
    
    
    



# @app.route("/availability")
# @functools.lru_cache(maxsize=128)
# def get_availability():
#     engine = get_db()
#     sql = "SELECT * FROM availability;"
#     try:
#         with engine.connect() as conn:
#             rows = conn.execute(text(sql)).fetchall()
#             print('Found {} availability entries', len(rows), rows)

#             # 转换时间戳为分秒格式
#             formatted_rows = []
#             for row in rows:
#                 row_dict = row._asdict()
#                 row_dict['last_update'] = datetime.utcfromtimestamp(row_dict['last_update']).strftime('%M:%S')
#                 formatted_rows.append(row_dict)

#             return jsonify(formatted_rows)
#     except:
#         print(traceback.format_exc())
#         return "error in get_availability", 404

    
    
    
    
# @app.route("/occupancy/<int:station_id>")
# def get_occupancy(station_id):
#     engine = get_db_raw()
    

#     df = pd.read_sql_query("select * from availability_log where number = %(number)s", engine, params={"number": station_id})
    
#     df['last_update_date'] = pd.to_datetime(df.last_update, unit='ms')
#     df.set_index('last_update_date', inplace=True)
    
    
#     res = df['available_bike_stands'].resample('1w').mean()
#     #res['dt'] = df.index
    
    
#     print(res)
#     return jsonify(data=json.dumps(list(zip(map(lambda x: x.isoformat(), res.index), res.values))))


@app.route("/occupancy/<int:station_id>")
def get_occupancy(station_id):
    engine = get_db_raw()
    

    df = pd.read_sql_query("select * from availability_log where number = %(number)s", engine, params={"number": station_id})
    
    df['last_update_date'] = pd.to_datetime(df.last_update, unit='ms')
    df.set_index('last_update_date', inplace=True)
    
    end_date = df.index.max()
    start_date = end_date - timedelta(days=6)
    res = df.loc[start_date:end_date]['available_bike_stands'].resample('1D').mean()
    
    #res = df['available_bike_stands'].resample('1D').mean()
    #res['dt'] = df.index
    res = res.dropna()  # 过滤掉 NaN 值
    print(res)
    
    # return jsonify(data=json.dumps(list(zip(map(lambda x: x.isoformat(), res.index), res.values))))
    return jsonify(data=json.dumps(list(zip(map(lambda x: x.strftime('%Y-%m-%d'), res.index), res.values))))

    # print(res)
    # return jsonify(data=json.dumps(list(zip(map(lambda x: x.isoformat(), res.index), res.values))))   


@app.route("/occupancy2/<int:station_id>/<string:date>")
def get_occupancy2(station_id, date):
    engine = get_db_raw()

    df = pd.read_sql_query("select * from availability_log where number = %(number)s", engine, params={"number": station_id})

    df['last_update_date'] = pd.to_datetime(df.last_update, unit='ms')
    df.set_index('last_update_date', inplace=True)

    input_date = pd.to_datetime(date)  # 将输入的日期字符串转换为 datetime 对象
    start_date = input_date.replace(hour=0, minute=0, second=0)  # 设置开始时间为输入日期的凌晨 00:00:00
    end_date = input_date.replace(hour=23, minute=59, second=59)  # 设置结束时间为输入日期的晚上 23:59:59

    res = df.loc[start_date:end_date]['available_bike_stands'].resample('1H').mean()

    res = res.dropna()  # 过滤掉 NaN 值
    print(res)

    return jsonify(data=json.dumps(list(zip(map(lambda x: x.strftime('%Y-%m-%d %H:%M:%S'), res.index), res.values))))
    


   

    
    


# @app.route('/page')
# def page():
#     #return app.send_static_file('index.html')#only use in the static files
#     #return "Hello!!!!cat!!!!"
#     return render_template('test_part.html')
@app.route('/page')
def page():
    engine = create_engine(f"mysql+mysqldb://{user}:{password}@{url}:{port}/{database}", echo=True)
    sql = """
    select temp, description from weather_newest order by dt desc limit 1;
    """
    weatherInfo = engine.execute(sql).fetchall()
    icon = engine.execute("select icon from weather_newest order by dt desc limit 1;").fetchone()
    icon_src = "http://openweathermap.org/img/w/" + str(icon[0]) + ".png"
    return render_template('test2.html', weatherInfo=weatherInfo, icon_src=icon_src)

@app.route('/sample')
def index():
      return render_template('index.html')
  
# @app.route('/mapsample')
# def index():
#       return render_template('Page-9.html')

#這句話要放在最後才能運作整個程序
if __name__=="__main__":
    app.run(debug=True)
    


# @app.route('/')
# def contact():
#     return app.send_static_file('/sample/index.html')

# @app.route('/contact')
# def contact():
#     return app.send_static_file('/sample/index.html')

# @app.route('/stations')
# def stations():
#     return list of stations

# @app.route('/station/<int:station_id>')
# def station(station_id):
#     return 'Retrieving info for Station: {}'.format(station_id)