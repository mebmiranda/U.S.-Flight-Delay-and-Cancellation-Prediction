# Data Folder Readme
### Overview
This folder contains information about the datasets used in this project. The data is related to the United States domestic flight information and weather data for U.S. airports.

### Data Sources
The following data sources were used in this project:
- [Bureau of Transportation Statistics - Airline On-Time Performance](https://www.transtats.bts.gov/TableInfo.asp?gnoyr_VQ=FGJ&QO_fu146_anzr=b0-gvzr&V0s1_b0yB=D): The dataset contains flight information from 1987 to 2023, including airline carrier, airport departure and destination, arrival time, delay times, and cancellation information.
- [National Centers for Environmental Information](https://www.ncei.noaa.gov/cdo-web/datatools/lcd) (NCEI) Weather Data: The dataset contains hourly and daily weather information for each U.S. airport, including altimeter, temperature, precipitation, pressure, wind direction and speed, humidity, and visibility.

### Files
The following files are included in this folder:
- Lookup Tables Folder: This folder contains lookup tables for Flight Data.
- Flight Data.md: This file contains link to the raw flight dataset.
- Weather Data.md: This file contains link to the raw weather dataset.
- flight_final.csv.zip: This file contains the cleaned flight dataset.
- weather_final.csv: This file contains the cleaned weather dataset.
- Merged Dataset (Final Dataset).md: This file contains link to the final dataset, which is a merge of the cleaned flight and weather datasets.
- Flight.ipynb: This Jupyter notebook contains Python code used to clean the Flight Data.
- Weather.ipynb: This Jupyter notebook contains Python code used to clean the Weather Data.
- Merged.ipynb: This Jupyter notebook contains Python code used to merge the cleaned weather_final.csv and flight_final.csv datasets.

### Conclusion
This readme file provides an overview of the data used in this project, including its sources and the files included in this folder. The data files have been cleaned and merged to create a final dataset, which is used for analysis and modeling. The accompanying Jupyter notebooks contain Python code used to clean and merge the data.
