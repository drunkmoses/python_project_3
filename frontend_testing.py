from selenium import webdriver

def webd(): # define function to shorten code
    return webdriver.Chrome(executable_path=f"chromedriver")

fe_test = webd()
fe_test.get("http://127.0.0.1:5001/users/get_user_data/1444")
try:
    id_action = fe_test.find_elements_by_id('a')
    if not id_action:
        raise Exception("test failed")
    else:
        for element in id_action:
            print(element.text)
finally:
    fe_test.close()

