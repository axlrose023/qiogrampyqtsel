import random

from selenium import webdriver
import time
import pickle
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# s = Service("chromedriver/chromedriver.exe")
# driver = webdriver.Chrome(service=s)
# driver.get("https://www.instagram.com")
# time.sleep(1)
# username = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
# username.send_keys("sloboda276@gmail.com")
# time.sleep(1)
# password = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
# password.send_keys("qwerty0192", Keys.ENTER)
# time.sleep(3)
# with open("cocks.pkl", "wb") as file:
#     pickle.dump(driver.get_cookies(), file)
# time.sleep(1)
# driver.close()


class InstaBOT:
    options = Options()
    options.headless = True
    url = "https://www.instagram.com/"
    s = Service("chromedriver/chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=options)

    def __init__(self):
        url = self.url
        driver = self.driver
        try:
            driver.get(url=url)
            time.sleep(1)
            for coockie in pickle.load(open("cocks.pkl", "rb")):
                driver.add_cookie(coockie)
            driver.implicitly_wait(1)
            driver.refresh()
        except Exception as ex:
            print(ex)

    def set_likes(self, person):
        driver = self.driver
        url = self.url
        url = url + person
        driver.get(url=url)
        time.sleep(1)
        post_urls = []
        pers = driver.find_element(By.XPATH, "/html")
        time.sleep(1)
        for i in range(5):
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pers)
            i += 1
            time.sleep(1)
        hrefs = driver.find_elements(By.TAG_NAME, "a")
        hrefs = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]
        time.sleep(3)
        for href in hrefs:
            post_urls.append(href)
        print(post_urls)
        with open(f"{person}_urls.txt", 'w') as file:
            file.write("\n".join(post_urls))
        time.sleep(1)
        with open(f"{person}_urls.txt", 'r') as file:
            for line in file:
                driver.get(line)
                time.sleep(1)
                driver.find_element(By.CLASS_NAME, "fr66n").find_element(By.CLASS_NAME, "wpO6b  ").click()
                time.sleep(1)
        driver.close()

    def get_subs(self, person):
        driver = self.driver
        url = self.url
        url = url + person
        try:
            driver.get(url=url)
            time.sleep(1)
            try:
                driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
                driver.implicitly_wait(2)
                ss = driver.find_element(By.CLASS_NAME, "_1XyCr  ").find_element(By.CLASS_NAME, "isgrP")
                time.sleep(3)

                for i in range(10):
                    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", ss)
                    time.sleep(1)
                hrefslist = []
                hrefs = ss.find_elements(By.TAG_NAME, "li")
                for href in hrefs:
                    href = href.find_element(By.TAG_NAME, "a").get_attribute("href")
                    hrefslist.append(href)
                print(hrefslist)
                random.shuffle(hrefslist)
                with open(f"{person}_fol.txt", 'w') as file:
                    file.write("\n".join(hrefslist))


                with open(f"{person}_fol.txt", 'r') as file:
                        for line in file:
                            try:
                                driver.get(line)
                                time.sleep(2)
                                driver.find_element(By.XPATH,\
                "/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div").click()
                                time.sleep(30)
                            except Exception as ex:
                                print(ex)
                                driver.close()

                # for href in hrefs:
                #     href = href.find_element(By.CLASS_NAME, "enpQJ").find_element(By.CLASS_NAME, "Jv7Aj mArmR MqpiF  ")
                #     href = href.get_attribute("href")
                #     hrefslist.append(href)
                # print(hrefslist)
                # a = [hrefslist.append(href.get_attribute("href")) for href in hrefs]
                # print(a)
            except Exception as ex:
                print(ex)
                driver.close()
        except Exception as ex:
            print(ex)
            driver.close()
        finally:
            driver.close()
            driver.quit()


john = InstaBOT()
john.get_subs("k.satans")
