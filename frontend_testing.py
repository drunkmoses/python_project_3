from selenium import webdriver

def webd():
    return webdriver.Firefox(executable_path=f"D:\Stuff\Python\geckodriver.exe")

fe_test = webd()
fe_test.get("http://127.0.0.1:5001/users/get_user_data/3")
try:
    id_action = fe_test.find_element_by_id("user")
except:
    raise Exception("test failed")
finally:
    fe_test.close()