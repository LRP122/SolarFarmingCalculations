## Agrivoltaics Tirol

This repository contains the code for the Agrivoltaics Tirol project.
The project aims to investigate the potential of agrivoltaics in the region of Tirol, Austria. The data used in this project 
is web scraped from the [TirolSolar](https://www.tirolsolar.at/#10/47.1900/11.5700) map. The data is then used to calculate the potential of agrivoltaics.

If you are interested in the prospect of agrivoltaics, the [Frauenhofer APV-Guidline](https://www.ise.fraunhofer.de/en/publications/studies/agrivoltaics-opportunities-for-agriculture-and-the-energy-transition.html) 
is a good reference point.

# How to use this project

To use this project to find the potential of agrivoltaics on your farm, you need to follow the steps below:

1. Clone the repository to your local machine.
2. Install the required packages by running the following command in the terminal:
```bash
pip install -r requirements.txt
```
3. Enter the coordinates of your farm in the __main__.py file.
4. Run the __main__.py file create data and calculations of agrivoltaics on your farm. Run the following command in the terminal:
```bash
python3 src\__main__.py
```
5. Run the following command to create the report and download it from the report folder:
```bash
./reporting/create_pdf.sh
```

# Future Increments

The project is still in the early stages of development. The following increments are planned for the future:

1. Add a user interface to make it easier for users to input their farm coordinates.
2. Add possibility for different types of farms, agriculture, and solar panels to create more individualized reports.
3. Deploy the project as a web application to make it more accessible to users.