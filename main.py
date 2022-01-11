from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from tkinter import *
from tkinter import messagebox

name = None


def get_repo_name():
    global name
    name = repo_name.get()
    if len(name) == 0:
        messagebox.showwarning(title="Missing info",
                               message="Type the name of the repo first")
    else:
        return name


def start():
    global name

    if get_repo_name():

        driver = webdriver.Chrome("./chromedriver.exe")

        driver.get("https://github.com/")

        menu = driver.find_element_by_xpath(
            '/html/body/div[1]/header/div/div[2]/div[2]/div[2]/a')
        menu.click()

        username_input = driver.find_element_by_xpath('//*[@id="login_field"]')
        username_input.click()
        username_input.send_keys("miladbannourah@outlook.com")

        password_input = driver.find_element_by_xpath('//*[@id="password"]')
        password_input.click()
        password_input.send_keys("Miladmilo2002")

        sign_in_button = driver.find_element_by_xpath(
            '//*[@id="login"]/div[4]/form/div/input[12]')
        sign_in_button.click()

        time.sleep(1)
        new_repository = driver.find_element_by_xpath(
            '//*[@id="repos-container"]/h2/a')
        new_repository.click()

        repository_name = driver.find_element_by_xpath(
            '//*[@id="repository_name"]')
        repository_name.click()
        repository_name.send_keys(name)

        add_readme_file = driver.find_element_by_xpath(
            '//*[@id="repository_auto_init"]')
        add_readme_file.click()

        time.sleep(1)
        create_repo = driver.find_element_by_xpath(
            '//*[@id="new_repository"]/div[4]/button')
        create_repo.click()

        # wait for the page to load then exeute the rest of the code
        try:
            my_element = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//*[@id="repo-content-pjax-container"]/div/div[2]/div[1]/div[2]/details/summary/span[1]')))
            print("element is ready")
        except TimeoutException:
            print("took too long")

        else:
            add_file = driver.find_element_by_xpath(
                '//*[@id="repo-content-pjax-container"]/div/div[2]/div[1]/div[2]/details/summary/span[1]')
            add_file.click()

        time.sleep(0.5)
        upload_files = driver.find_element_by_xpath(
            '//*[@id="repo-content-pjax-container"]/div/div[2]/div[1]/div[2]/details/div/ul/li[3]/a')
        upload_files.click()
    else:
        print("didn't type repo name")


###################################################################
window = Tk()
window.minsize(width=500, height=500)

button = Button(text="Create repository", font=(
    "Arial", 14, "bold"), command=start)
button.place(x=170, y=200)

repo_name = Entry(width=30, font=("Arial", 14, "bold"))
repo_name.place(x=100, y=280)

window.mainloop()
