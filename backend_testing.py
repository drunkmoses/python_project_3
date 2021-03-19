import requests
import pymysql

# post test: asks user for id, and posts it with 'test' user_name to DB

new_user_id = 4
url = "http://127.0.0.1:5000/users/%s" % new_user_id


post_test = requests.post(url, json={"user_name":"Test"})
if post_test.ok:
   print(post_test.json())

# gets the posted id and sends confirmation it was posted

get_test = requests.get(url)
if get_test.ok:
    print(get_test.json())

# retrieves the values from the DB

conn = pymysql.connect(host='remotemysql.com', port=3306, user='Z5Ujjt1fJM', passwd='DPJb1mhSaL', db='Z5Ujjt1fJM')
conn.autocommit(True)
cursor = conn.cursor()
select_query = "SELECT * FROM Z5Ujjt1fJM.users WHERE user_id = %s;"
cursor.execute(select_query, new_user_id)
for item in cursor:
    print(item)

cursor.close()
conn.close()
