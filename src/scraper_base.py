from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from selenium.webdriver.chrome.options import Options

class webscraper():

    def __init__(self):
        self.header_radiation = ["Strahlung Jahr", "Strahlung Sommer","Strahlung Winter"]
        self.df_radiation = pd.DataFrame(columns = self.header_radiation)

        self.header_sunhours = ["Sonnenschein Jahr" , "Sonnenschein Januar", "Sonnenschein Feber", "Sonnenschein März", "Sonnenschein April", "Sonnenschein Mai", "Sonnenschein Juni", "Sonnenschein Dezember"]
        self.df_sunhours = pd.DataFrame(columns = self.header_sunhours)


    def field_data_radiation(self, Dropdownfield, df_radiation = True, zero = [47.2863,11.4729], one = [47.2863,11.4795], two = [47.2891,11.4795], three = [47.2891,11.4729]):
        if df_radiation:
            df_radiation = self.df_radiation

        north_zero = zero[0]
        east_zero = zero[1]
        north_one = one[0]
        east_one = one[1]
        north_two = two[0]
        east_two = two[1]
        north_three = three[0]
        east_three = three[1]


        base_ulr = "https://www.tirolsolar.at/#15/"
        url = base_ulr + str(north_zero) + "/" + str(east_zero)

        current_ew_url = east_zero
        x_offset = 0
        i = 0

        while current_ew_url < east_one:

            y_offset = 0
            base_ulr = "https://www.tirolsolar.at/#15/"
            url = base_ulr + str(north_zero) + "/" + str(east_zero)

            options = Options()
            options.add_argument("--headless=new")  # Run in headless mode
            driver = webdriver.Chrome(options=options)
            #driver = webdriver.Chrome()
            driver.get(url)

            dropdown_element = driver.find_element(by=By.ID, value="dropdownMenuEditOpener")
            dropdown_element.click()

            option = driver.find_element(By.XPATH, f'//a[contains(text(), "{Dropdownfield}")]')

            option.click()

            current_url = driver.current_url

            url_values = current_url.split("/", 6)
            current_ns_url = float(url_values[4])
            current_ew_url = float(url_values[5])

            while current_ns_url < north_two:

                actions = ActionChains(driver)
                actions.move_to_element_with_offset(driver.find_element(By.TAG_NAME, 'body'), 0, 0)
                actions.move_by_offset(x_offset, -1.5 * y_offset).click().perform()

                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//tr[td="Solarstrahlung Jahr"]/td[2]'))
                )
                ssj_ = driver.find_element(By.XPATH, '//tr[td="Solarstrahlung Jahr"]/td[2]')
                ssj = ssj_.text
                sss_ = driver.find_element(By.XPATH, '//tr[td="Solarstrahlung Apr-Sep"]/td[2]')
                sss = sss_.text
                ssw_ = driver.find_element(By.XPATH, '//tr[td="Solarstrahlung Okt-Mrz"]/td[2]')
                ssw = ssw_.text

                df_radiation.loc[i, "Strahlung Jahr"] = ssj
                df_radiation.loc[i, "Strahlung Jahr"] = float(df_radiation.loc[i, "Strahlung Jahr"].replace(" kWh/m\u00B2", ""))

                df_radiation.loc[i, "Strahlung Sommer"] = sss
                df_radiation.loc[i, "Strahlung Sommer"] = float(df_radiation.loc[i, "Strahlung Sommer"].replace(" kWh/m\u00B2", ""))

                df_radiation.loc[i, "Strahlung Winter"] = ssw
                df_radiation.loc[i, "Strahlung Winter"] = float(df_radiation.loc[i, "Strahlung Winter"].replace(" kWh/m\u00B2", ""))

                y_offset += 1
                i += 1


                current_url = driver.current_url
                url_values = current_url.split("/", 6)
                current_ns_url = float(url_values[4])
                current_ew_url = float(url_values[5])

            east_zero += 0.003



        averageJahr = round(df_radiation["Strahlung Jahr"].mean(),1)
        averageSommer = round(df_radiation["Strahlung Sommer"].mean(),1)
        averageWinter = round(df_radiation["Strahlung Winter"].mean(),1)


        return df_radiation

    def field_data_sunhours(self, Dropdownfield, df_sunhours = True, zero = [47.2863,11.4729], one = [47.2863,11.4795], two = [47.2891,11.4795], three = [47.2891,11.4729]):
        if df_sunhours:
            df_sunhours = self.df_sunhours

        north_zero = zero[0]
        east_zero = zero[1]
        north_one = one[0]
        east_one = one[1]
        north_two = two[0]
        east_two = two[1]
        north_three = three[0]
        east_three = three[1]


        base_ulr = "https://www.tirolsolar.at/#15/"
        url = base_ulr + str(north_zero) + "/" + str(east_zero)

        current_ew_url = east_zero
        x_offset = 0
        i = 0

        while current_ew_url < east_one:

            y_offset = 0
            base_ulr = "https://www.tirolsolar.at/#15/"
            url = base_ulr + str(north_zero) + "/" + str(east_zero)

            options = Options()
            options.add_argument("--headless=new")  # Run in headless mode
            driver = webdriver.Chrome(options=options)
            #driver = webdriver.Chrome()
            driver.get(url)

            dropdown_element = driver.find_element(by=By.ID, value="dropdownMenuEditOpener")
            dropdown_element.click()

            option = driver.find_element(By.XPATH, f'//a[contains(text(), "{Dropdownfield}")]')

            option.click()

            current_url = driver.current_url

            url_values = current_url.split("/", 6)
            current_ns_url = float(url_values[4])
            current_ew_url = float(url_values[5])

            while current_ns_url < north_two:

                actions = ActionChains(driver)
                actions.move_to_element_with_offset(driver.find_element(By.TAG_NAME, 'body'), 0, 0)
                actions.move_by_offset(x_offset, -1.5 * y_offset).click().perform()

                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//tr[td="Sonnenscheindauer Jahr"]/td[2]'))
                )
                ssj_ = driver.find_element(By.XPATH, '//tr[td="Sonnenscheindauer Jahr"]/td[2]')
                ssj = ssj_.text

                ss_januar = driver.find_element(By.XPATH, '//tr[td="Sonnenscheindauer 21. Jänner"]/td[2]')
                ss_januar = ss_januar.text

                ss_februar_ = driver.find_element(By.XPATH, '//tr[td="Sonnenscheindauer 21. Feber"]/td[2]')
                ss_februar = ss_februar_.text

                ss_marz_ = driver.find_element(By.XPATH, '//tr[td="Sonnenscheindauer 21. März"]/td[2]')
                ss_marz = ss_marz_.text

                ss_april_ = driver.find_element(By.XPATH, '//tr[td="Sonnenscheindauer 21. April"]/td[2]')
                ss_april = ss_april_.text

                ss_mai_ = driver.find_element(By.XPATH, '//tr[td="Sonnenscheindauer 21. Mai"]/td[2]')
                ss_mai = ss_mai_.text

                ss_juni_ = driver.find_element(By.XPATH, '//tr[td="Sonnenscheindauer 21. Juni"]/td[2]')
                ss_juni = ss_juni_.text

                ss_dezember_ = driver.find_element(By.XPATH, '//tr[td="Sonnenscheindauer 21. Dez"]/td[2]')
                ss_dezember = ss_dezember_.text

                df_sunhours.loc[i, "Sonnenschein Jahr"] = ssj
                df_sunhours.loc[i, "Sonnenschein Jahr"] = float(df_sunhours.loc[i, "Sonnenschein Jahr"].replace(",0 h", "")) * 1000

                df_sunhours.loc[i, "Sonnenschein Januar"] = ss_januar
                df_sunhours.loc[i, "Sonnenschein Januar"] = float(df_sunhours.loc[i, "Sonnenschein Januar"].replace(" h", "").replace(",", "."))

                df_sunhours.loc[i, "Sonnenschein Feber"] = ss_februar
                df_sunhours.loc[i, "Sonnenschein Feber"] = float(df_sunhours.loc[i, "Sonnenschein Feber"].replace(" h", "").replace(",", "."))

                df_sunhours.loc[i, "Sonnenschein März"] = ss_marz
                df_sunhours.loc[i, "Sonnenschein März"] = float(df_sunhours.loc[i, "Sonnenschein März"].replace(" h", "").replace(",", "."))

                df_sunhours.loc[i, "Sonnenschein April"] = ss_april
                df_sunhours.loc[i, "Sonnenschein April"] = float(df_sunhours.loc[i, "Sonnenschein April"].replace(" h", "").replace(",", "."))

                df_sunhours.loc[i, "Sonnenschein Mai"] = ss_mai
                df_sunhours.loc[i, "Sonnenschein Mai"] = float(df_sunhours.loc[i, "Sonnenschein Mai"].replace(" h", "").replace(",", "."))

                df_sunhours.loc[i, "Sonnenschein Juni"] = ss_juni
                df_sunhours.loc[i, "Sonnenschein Juni"] = float(df_sunhours.loc[i, "Sonnenschein Juni"].replace(" h", "").replace(",", "."))

                df_sunhours.loc[i, "Sonnenschein Dezember"] = ss_dezember
                df_sunhours.loc[i, "Sonnenschein Dezember"] = float(df_sunhours.loc[i, "Sonnenschein Dezember"].replace(" h", "").replace(",", "."))

                y_offset += 1
                i += 1


                current_url = driver.current_url
                url_values = current_url.split("/", 6)
                current_ns_url = float(url_values[4])
                current_ew_url = float(url_values[5])

            east_zero += 0.003



        averageJahr = round(df_sunhours["Sonnenschein Jahr"].mean(),1)
        averageSommer = round(df_sunhours["Sonnenschein Feber"].mean(),1)
        averageWinter = round(df_sunhours["Sonnenschein Juni"].mean(),1)

        return df_sunhours












