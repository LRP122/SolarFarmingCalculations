import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class analysis():

    def __init__(self):

        self.energy_price = 0.12
        self.power_module = 0.25

    def get_area(self,zero = [47.2863,11.4729], one = [47.2863,11.4795], two = [47.2891,11.4795], three = [47.2891,11.4729]):
        north_zero = zero[0]
        east_zero = zero[1]
        north_one = one[0]
        east_one = one[1]
        north_two = two[0]
        east_two = two[1]
        north_three = three[0]
        east_three = three[1]

        dist_north = 110000
        dist_east = 70000

        area = abs(((north_one - north_three) * dist_north)  * ((east_one - east_zero) * dist_east))
        print(f"Die Fläche beträgt {area} m²")
        print(f"Die Fläche beträgt {area / 10000} ha")
        return area

    # Stromerzeugung pro Monat in kWh als barchart

    def monthly_production(self, df_radiation, df_sunhours, area):
        Strahlung_Sommer = df_radiation["Strahlung Sommer"].mean()
        Strahlung_Winter = df_radiation["Strahlung Winter"].mean()
        StrahlungJahr = df_radiation["Strahlung Jahr"].mean()
        Sonnenstunden_Januar = df_sunhours["Sonnenschein Januar"].mean()
        Sonnenstunden_Februar = df_sunhours["Sonnenschein Feber"].mean()
        Sonnenstunden_März = df_sunhours["Sonnenschein März"].mean()
        Sonnenstunden_April = df_sunhours["Sonnenschein April"].mean()
        Sonnenstunden_Mai = df_sunhours["Sonnenschein Mai"].mean()
        Sonnenstunden_Juni = df_sunhours["Sonnenschein Juni"].mean()
        Sonnenstunden_Dezember = df_sunhours["Sonnenschein Dezember"].mean()

        Monate = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Dezember"]
        Strahlung = [Strahlung_Winter, Strahlung_Winter, Strahlung_Winter, Strahlung_Sommer, Strahlung_Sommer, Strahlung_Sommer, Strahlung_Winter]
        Sonnenstunden = [Sonnenstunden_Januar, Sonnenstunden_Februar, Sonnenstunden_März, Sonnenstunden_April, Sonnenstunden_Mai, Sonnenstunden_Juni, Sonnenstunden_Dezember]

        Stromerzeugung = []

        for i in range(len(Monate)):
            Stromerzeugung.append((Sonnenstunden[i] * area) * self.power_module * 0.3)
        
        df = pd.DataFrame({"Monate": Monate, "Stromerzeugung": Stromerzeugung})
        
        return df
    
    def plot_monthly_production(self, df):
        colors = ['r', 'g', 'b', 'y', 'c', 'm', 'k']
        
        Monate = df["Monate"]
        Stromerzeugung = df["Stromerzeugung"].astype(float) * 0.3

        plt.ticklabel_format(style="plain")
        plt.bar(Monate, Stromerzeugung, color=colors, edgecolor="black", linewidth=2, alpha=0.7, capsize=5)

        plt.xlabel("Monate")
        plt.ylabel("[kWh]")
        plt.title("Stromerzeugung pro Monat in Mio. kWh")

        plt.savefig("../reporting/images/Stromerzeugung_pro_Monat.png", dpi=600)
        plt.clf()

    def yearly_return(self, df):

        returns = df["Stromerzeugung"].sum() * self.energy_price

        cost = 100000

        years = np.arange(2025, 2051)

        accumulated_return = [returns * (1 + 0.02) ** (year - 2024) for year in years]

        plt.plot(years, accumulated_return ,color="blue", marker="o", linestyle="--", linewidth=2, markersize=10)
        plt.axhline(y=cost, color="red", linestyle="--", linewidth=2)
        plt.xlabel("Jahre")
        plt.ylabel("[€]")
        plt.title("Akkumulierter Ertrag in €")

        plt.savefig("../reporting/images/Akkumulierter_Ertrag.png", dpi=600)






      
        
        


















