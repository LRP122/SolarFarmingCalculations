from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

class webscraper():

    def __init__(self):
        self.header = ["Hofname", "Strahlung Jahr", "Strahlung Sommer","Strahlung Winter","Position"]
        self.df = pd.DataFrame(columns = self.header)

        self.big_df = pd.DataFrame(columns = self.header)

    def field_data(self, df = True, ns_field_coordinate = 47.2743, ew_field_coordinate=11.4686, hofname = "Huberts Eierhof"):
        if df:
            df = self.df

        driver = webdriver.Chrome()
        base_ulr = "https://www.tirolsolar.at/#21/"
        url = base_ulr + str(ns_field_coordinate) + "/" + str(ew_field_coordinate)
        driver.get(url)

        dropdown_element = driver.find_element(by=By.ID, value="dropdownMenuEditOpener")
        dropdown_element.click()

        option = driver.find_element(By.XPATH, '//a[contains(text(), "Solarstrahlung")]')
        option.click()

        for i in range(15):
            actions = ActionChains(driver)
            actions.move_by_offset(0, 0).click().perform()
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//tr[td="Solarstrahlung Jahr"]/td[2]'))
            )
            ssj_ = driver.find_element(By.XPATH, '//tr[td="Solarstrahlung Jahr"]/td[2]')
            ssj = ssj_.text
            sss_ = driver.find_element(By.XPATH, '//tr[td="Solarstrahlung Apr-Sep"]/td[2]')
            sss = sss_.text
            ssw_ = driver.find_element(By.XPATH, '//tr[td="Solarstrahlung Okt-Mrz"]/td[2]')
            ssw = ssw_.text
            pos_ = driver.find_element(By.XPATH, '//tr[td="Position WGS 84"]/td[2]')
            pos = pos_.text
            df.loc[i, "Hofname"] = hofname

            df.loc[i, "Strahlung Jahr"] = ssj
            df.loc[i, "Strahlung Jahr"] = float(df.loc[i, "Strahlung Jahr"].replace(" kWh/m\u00B2",""))

            df.loc[i, "Strahlung Sommer"] = sss
            df.loc[i, "Strahlung Sommer"] = float(df.loc[i, "Strahlung Sommer"].replace(" kWh/m\u00B2",""))

            df.loc[i, "Strahlung Winter"] = ssw
            df.loc[i, "Strahlung Winter"] = float(df.loc[i, "Strahlung Winter"].replace(" kWh/m\u00B2",""))

            df.loc[i, "Position"] = pos

        averageJahr = df["Strahlung Jahr"].mean()
        averageSommer = df["Strahlung Sommer"].mean()
        averageWinter = df["Strahlung Winter"].mean()

        print(df)



