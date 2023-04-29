# U.S. Flight Delay and Cancellation Prediction
### Introduction
This project is the final requirement for the Computation Data Analytics (ISYE 6740) course for the Master of Science in Analytics degree at Georgia Institute of Technology. The objective of this project is to predict flight delays and cancellations for the 10 busiest U.S. airports, and to improve an airline's ability to cancel flights in advance.

### Problem Statement
Flight delays and cancellations are a significant problem for both travelers and airline companies. Predicting flight delays and cancellation is challenging due to various situations or events that can happen before the flight such as weather problems, aircraft downtime/mechanical problems, queuing issues, system problems, crew scheduling issues, and air traffic congestion. The goal of this project is to help address this problem and improve an airline's ability to cancel flights in advance to enhance customer experience and route recovery planning.
1. Customer experience: Canceling flights 4 hours before the flight, allows customers to avoid traveling to the airport only to find their flights canceled or moved.  It also enables customers to rebook flights earlier, and find better routes.
2. Planning of route recovery: By being more intentional on the flights/routes that are canceled, airlines can better plan how to get back to 100% operational capacity, with the least amount of delays.

### Data Source
The data used for this project is the [Airline On-Time Performance](https://www.transtats.bts.gov/TableInfo.asp?gnoyr_VQ=FGJ&QO_fu146_anzr=b0-gvzr&V0s1_b0yB=D) dataset, which is created and maintained by the Bureau of Transportation Statistics. The team filtered the dataset to only include the top 10 busiest U.S airports and merged it with local weather data from the [National Centers for Environmental Information](https://www.ncei.noaa.gov/cdo-web/datatools/lcd) (NCEI).

### Methodology
The team performed the following steps to achieve the project objective:

1. Data acquisition and cleaning: The flight and weather datasets were downloaded, and the necessary data cleaning process was performed.
2. Exploratory data analysis: The dataset was explored using descriptive statistics, data visualization, and other techniques to identify patterns and trends.
3. Data preprocessing: The categorical data was converted to dummy variables, and the data was standardized to have a range of 0-1.
4. Dimensionality reduction: Principal Component Analysis (PCA) was performed to reduce the dimensionality of the dataset and to identify the most important features.
5. Model development: Four classification models, namely K-Nearest Neighbors, Naive Bayes, Decision Trees, and Random Forest, were developed to predict the flight results. The hyperparameters of each model were experimented with to find the optimal hyperparameters.
6. Model evaluation: The classification models were compared based on their accuracy, precision, recall, and F1-score to determine the optimal model that best predicts the flight results.

### Evaluation and Result
Initially, the plan was to predict flight results as either On Time/Early, Slight Delay, Moderate Delay, Long Delay, or Cancelled. However, upon observing the data, it became apparent that there was no significant differentiation between the various delay categories and On Time/Early. Consequently, it was decided to simplify the scenario by classifying flight results as either Arrived or Cancelled, combining On Time/Early, Slight Delay, Moderate Delay, and Long Delay into the Arrived category.

To assess each model's performance, various classification measures were utilized, such as accuracy, precision, F1 score, and recall. Please refer to the actual paper for more information. The table below presents the accuracy of each model for different scenarios:

Scenario 1: Flight Results - On Time/Early, Slight Delay, Moderate Delay, Long Delay, or Cancelled

| Model         | Accuracy | Features Used                                                       |
|---------------|----------|----------------------------------------------------------------------|
| KNN           | 61.99%   | PCA ; components = 2                                                |
| Naive Bayes   | 61.13%   | PCA ; components = 2                                                |
| Decision Tree | 62.09%   | Relative Humidity, Dry Bulb Temp, Visibility, Sea Level Temp, Wind Direction |
| Random Forest | 57.07%   | Relative Humidity, Wet Bulb Temp, Precipitation, Sea Level Temp, Wind Direction |

Scenario 2: Flight Results - Arrived or Cancelled
| Model         | Accuracy | Features Used                                                       |
|---------------|----------|----------------------------------------------------------------------|
| KNN           | 99.08%   | PCA ; components = 2                                                |
| Naive Bayes   | 99.00%   | PCA ; components = 2                                                |
| Decision Tree | 99.04%   | Relative Humidity, Dry Bulb Temp, Visibility, Sea Level Temp, Wind Direction |
| Random Forest | 99.50%   | Relative Humidity, Wet Bulb Temp, Precipitation, Sea Level Temp, Wind Direction |

While the four models performed poorly in scenario 1, the accuracy improved to 99% in scenario 2 for all models. Random Forest model appears to be the most effective, with an accuracy of 99.50%, utilizing features such as Relative Humidity, Wet Bulb Temperature, Precipitation, Sea Level Temperature, and Wind Direction.


### Files
- Data folder: contains information about the data used for the project
- Analysis.ipynb: contains Jupyter notebook that contains all the python codes used to perform data analysis
- Project Proposal ISYE 6740.pdf: The submitted project proposal. 
- Project Report ISYE 6740.pdf: The submitted project report.

### Conclusion
Flight delays and cancellations can cause significant inconvenience to travelers and incur significant costs to airlines. This project aimed to address this issue by using data analytics to predict flight results for the 10 busiest U.S. airports. The Airline On-Time Performance dataset and local weather data were utilized to develop predictive models for two scenarios.

In the first scenario, flight results were classified as On Time/Early, Slight Delay, Moderate Delay, Long Delay, or Cancelled. However, no significant distinction was found between the different types of delays and on-time/early flights. Thus, On Time/Early, Slight Delay, Moderate Delay, and Long Delay flights were grouped as Arrived for the second scenario, which only classified flight results as either Arrived or Cancelled.

While the four models performed poorly in scenario 1, with accuracy ranging from 57.07% to 62.09%, all models achieved an impressive 99% accuracy in scenario 2. The success of the models in scenario 2 suggests that the current dataset may be missing important features that are useful in distinguishing On Time/Early and Delay flights. Future studies could consider additional relevant features such as airport congestion or airline schedules, which could further improve the model's ability to predict flight delays.
