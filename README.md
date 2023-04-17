# U.S. Flight Delay and Cancellation Prediction
This analytics project is the final requirement for the Computation Data Analytics (ISYE 6740) course for the Master of Science in Analytics degree at Georgia Institute of Technology.

### Problem Statement
Flight delays and cancellations is a significant problem for both travelers and airline companies. For travelers, it can cause inconvenience and missed events. For airline companies, it may cause profit loss and reputation damage. Predicting flight delays and cancellation is challenging due to various situations or events that can happen before the flight such as weather problems, aircraft downtime/mechanical problems, queuing issues, system problems, crew scheduling issues, and air traffic congestion. The goal of this project is to help address this problem, and improve an airline’s ability to cancel flights in advance in order to improve:
1. Customer experience: Canceling flights 4 hours before the flight, allows customers to avoid traveling to the airport only to find their flights canceled or moved.  It also enables customers to rebook flights earlier, and find better routes.
2. Planning of route recovery: By being more intentional on the flights/routes that are canceled, airlines can better plan how to get back to 100% operational capacity, with the least amount of delays.

The study focuses on the 10 busiest U.S. airports - LAX, ORD, ATL, DEN, DFW, SFO, SEA, MCO, EWR, and BOS. The team performed data analysis to find patterns or trends in flight results such as cancellation, slight delay, moderate delay, long delay, and on time. Moreover, the team explored classification models such as k-nearest neighbors, naive bayes, random forest, and decision trees to predict flight results. Hyperparameter experimentation was performed, and various feature engineering techniques discussed in the class was explored to find the optimal feature combination that should be used in the model.

### Data Source
The data used for this project is the [Airline On-Time Performance](https://www.transtats.bts.gov/TableInfo.asp?gnoyr_VQ=FGJ&QO_fu146_anzr=b0-gvzr&V0s1_b0yB=D) dataset which is created and maintained by the Bureau of Transportation Statistics. The data contains the United States domestic flight information from 1987 to 2023 and has multiple features such as airline carrier, airport departure and destination, arrival time, delay times, cancellation information, etc. In addition to flight data, the team also used the airport's local weather data from [National Centers for Environmental Information](https://www.ncei.noaa.gov/cdo-web/datatools/lcd) (NCEI). 

The Airline On-Time Performance dataset is used to get information about the flights and filtered to only the top 10 busiest U.S airports. The dataset was then merged with weather data to obtain weather information such as altimeter, dry bulb temperature, precipitation, sea level pressure, station pressure, wet bulb temperature, wind direction, wind speed, dew point temperature, humidity, and visibility on the specific airport. 

Several data cleaning processes such as removing irrelevant data, removing null data, fixing feature data type, and grouping some of the columns to make the final dataset ready for analysis.

### Methodology
To achieve the objective of finding patterns and trends and predicting flight results (on-time, delay, and cancelled), the following steps were performed:

1. Data acquisition and cleaning: The flight and weather datasets were downloaded, and the necessary data cleaning process was performed. The two datasets were merged to add weather information to the flight dataset.
2. Exploratory data analysis: The dataset was explored using descriptive statistics, data visualization, and other techniques to identify patterns and trends.
3. Data preprocessing: The categorical data was converted to dummy variables, and the data was standardized to have a range of 0-1.
4. Dimensionality reduction: Principal Component Analysis (PCA) was performed to reduce the dimensionality of the dataset and to identify the most important features.
5. Model development: Four classification models, namely K-Nearest Neighbors, Naive Bayes, Decision Trees, and Random Forest, were developed to predict the flight results. The hyperparameters of each model were experimented with to find the optimal hyperparameters.
6. Model evaluation: The classification models were compared based on their accuracy, precision, recall, and F1-score to determine the optimal model that best predicts the flight results.

### Evaluation and Result
TBD

