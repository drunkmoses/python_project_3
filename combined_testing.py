import requests
import pymysql
from selenium import webdriver
import time

# post test: asks user for id, and posts it with 'test' user_name to DB

new_user_id = input("Enter a new user id: ")
url = "http://127.0.0.1:5000/users/%s" % new_user_id
app_url = "http://127.0.0.1:5001/users/get_user_data/%s" % new_user_id # added to allow variables in user_id during frontend testing
try:
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

except:
    raise Exception("test failed!")

# switch to selenium testing

def webd(): # define function to shorten code
    return webdriver.Chrome(executable_path=f"chromedriver")

fe_test = webd()
print(url)
fe_test.get(app_url)
id_action = fe_test.find_elements_by_id('a')
if not id_action:
    raise Exception("test failed")
else:
    for element in id_action:
        print(element.text)

fe_test.close() # close done

