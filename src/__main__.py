from scraper_base import *
from analysis import *
import time
from multiprocessing import Pool
from automated_report import generate_report

start_time = time.time()

if __name__ == "__main__":

    W = webscraper()
    with Pool() as pool:
        Radiation = pool.apply_async(W.field_data_radiation, ("Solarstrahlung",))
        Sunhours = pool.apply_async(W.field_data_sunhours, ("Sonnenscheindauer",))

        # Get the results
        df_radiation = Radiation.get()  # get the return value from field_data_radiation
        df_sunhours = Sunhours.get()  # get the return value from field_data_sunhours

    print(df_radiation)
    print(df_sunhours)

    A = analysis()
    area = A.get_area()
    df_production = A.monthly_production(df_radiation, df_sunhours, area)
    A.plot_monthly_production(df_production)
    A.yearly_return(df_production)

    generate_report("sd", "sd")



