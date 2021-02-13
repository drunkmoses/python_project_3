import pymysql
from datetime import datetime

def insert_db(user_id,user_name):
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='Z5Ujjt1fJM', passwd='DPJb1mhSaL', db='Z5Ujjt1fJM')
    conn.autocommit(True)
    cursor = conn.cursor()
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    insert_query = "INSERT into Z5Ujjt1fJM.users (user_id, user_name, creation_date) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (user_id, user_name, dt_string))

    cursor.close()
    conn.close()

def update_db(user_id, user_name):
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='Z5Ujjt1fJM', passwd='DPJb1mhSaL', db='Z5Ujjt1fJM')
    conn.autocommit(True)
    cursor = conn.cursor()
    update_query = "UPDATE Z5Ujjt1fJM.users SET user_name = %s WHERE user_id = %s"
    cursor.execute(update_query, (user_name, user_id))

    cursor.close()
    conn.close()

def delete_db(user_id):
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='Z5Ujjt1fJM', passwd='DPJb1mhSaL', db='Z5Ujjt1fJM')
    conn.autocommit(True)
    cursor = conn.cursor()
    delete_query = "DELETE FROM Z5Ujjt1fJM.users WHERE user_id = %s;"
    cursor.execute(delete_query, user_id)
    cursor.close()
    conn.close()

def select_db(user_id):
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='Z5Ujjt1fJM', passwd='DPJb1mhSaL', db='Z5Ujjt1fJM')
    conn.autocommit(True)
    cursor = conn.cursor()
    select_query = "SELECT * FROM Z5Ujjt1fJM.users WHERE user_id = %s;"
    cursor.execute(select_query, user_id)
    row = None
    if cursor.rowcount > 0:
        for item in cursor:
            row = item[1]

    cursor.close()
    conn.close()
    return row