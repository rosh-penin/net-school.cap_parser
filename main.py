# from requests_html import HTMLSession
# from bs4 import BeautifulSoup
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


things = {
    'provinces': False,
    'cities': False,
    'funcs': False,
    'schools': False,
}


def clear_lists():
    for key, val in things.items():
        val = False


def delete_first(lof):
    del lof[0]

    return lof


def get_elements(driver, value):
    element = driver.find_element(by=By.ID, value=value)
    if ('Выберите' not in element.text and value != 'schools'):
        if element.is_displayed():
            raise Exception('YOUR EMPTINESS.')
        else:
            return element, None

    list_of_things = (delete_first(element.text.split('\n')))

    return element, list_of_things


def click_elements(driver, value):
    driver.find_element(by=By.XPATH, value=f"//*[contains(text(), '{value}')]").click()


def select_second(driver, choice):
    el, lst = get_elements(driver, choice)
    if lst is None:
        things[choice] = True
        return

    while True:
        print('Type number you need to select:')
        s_choice = int(input(', '.join([f'{enum}: {val}' for enum, val in enumerate(lst)]) + ': '))
        if s_choice in range(len(lst)):
            click_elements(el, lst[s_choice])
            things[choice] = True
            return
        else:
            print('YOUR SECOND CHANCE IS SLIPPING AWAY.')


def select_first():
    lst = []
    for key, value in things.items():
        lst.append(key)
        if value == False:
            break

    if lst == []:
        raise Exception('couldnt set list for inputs')

    while True:
        print('Type number you need to select:')
        choice = int(input(', '.join([f'{enum}: {val}' for enum, val in enumerate(lst)]) + ': '))
        if choice in range(len(lst)):
            return lst[choice]
        else:
            print('FOOL TURN ROUND AND AROUND.')


def submain(driver):
    while True:
        try:
            time.sleep(2)
            select_second(driver, select_first())
            time.sleep(1)
        except Exception as e:
            print(e)
            break
        else:
            print('success?')


def main(driver):
    while True:
        try:
            driver.get('https://net-school.cap.ru/')
            clear_lists()
        except Exception as e:
            print(e)
            time.sleep(3)
        else:
            submain(driver)
        finally:
            if input('Continue? Type "y" for yes: ') != 'y':
                break


if __name__ == '__main__':
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    main(driver)
    driver.quit()







# usag = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0"
# qtext = "александровское ставропольский край население"
# headers = {"userAgent":usag}
# url1 = "https://net-school.cap.ru/"

# session = HTMLSession()
# r = session.get(url1)
# script = """
# function() {
#   return sendAjaxRequest($(this));
# }
# """
# r.html.render(script=script)

# for i in r.html.find('.select-main select'):
#     name = i.attrs.get('id')
#     if name == 'provinces':
#         provinces = i
#         break
#     elif name == 'schools':
#         schools = i

# print(provinces.text)
# print(provinces.full_text)

# r.close()