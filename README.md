# U.S. Flight Delay and Cancellation Prediction
### Introduction
This project is the final requirement for the Computation Data Analytics (ISYE 6740) course for the Master of Science in Analytics degree at Georgia Institute of Technology. The objective of this project is to predict flight delays and cancellations for the 10 busiest U.S. airports, and to improve an airline's ability to cancel flights in advance.

### Problem Statement
Flight delays and cancellations are a significant problem for both travelers and airline companies. Predicting flight delays and cancellation is challenging due to various situations or events that can happen before the flight such as weather problems, aircraft downtime/mechanical problems, queuing issues, system problems, crew scheduling issues, and air traffic congestion. The goal of this project is to help address this problem and improve an airline's ability to cancel flights in advance to enhance customer experience and route recovery planning.
1. Customer experience: Canceling flights 4 hours before the flight, allows customers to avoid traveling to the airport only to find their flights canceled or moved.  It also enables customers to rebook flights earlier, and find better routes.
2. Planning of route recovery: By being more intentional on the flights/routes that are canceled, airlines can better plan how to get back to 100% operational capacity, with the least amount of delays.

### Data Source
The data used for this project is the Airline On-Time Performance dataset, which is created and maintained by the Bureau of Transportation Statistics. The team filtered the dataset to only include the top 10 busiest U.S airports and merged it with local weather data from the National Centers for Environmental Information (NCEI).

### Methodology
The team performed the following steps to achieve the project objective:

1. Data acquisition and cleaning: The flight and weather datasets were downloaded, and the necessary data cleaning process was performed.
2. Exploratory data analysis: The dataset was explored using descriptive statistics, data visualization, and other techniques to identify patterns and trends.
3. Data preprocessing: The categorical data was converted to dummy variables, and the data was standardized to have a range of 0-1.
4. Dimensionality reduction: Principal Component Analysis (PCA) was performed to reduce the dimensionality of the dataset and to identify the most important features.
5. Model development: Four classification models, namely K-Nearest Neighbors, Naive Bayes, Decision Trees, and Random Forest, were developed to predict the flight results. The hyperparameters of each model were experimented with to find the optimal hyperparameters.
6. Model evaluation: The classification models were compared based on their accuracy, precision, recall, and F1-score to determine the optimal model that best predicts the flight results.

### Evaluation and Result
The project's evaluation and results are yet to be determined.

### Files
- Data folder: contains information about the data used for the project
- Analysis.ipynb: contains Jupyter notebook that contains all the python codes used to perform data analysis
- Project Proposal ISYE 6740.pdf: The submitted project proposal. 
- Project Report ISYE 6740.pdf: The submitted project report.

### Conclusion
This project aims to address the issue of flight delays and cancellations using data analytics. The team used the Airline On-Time Performance dataset and local weather data to predict flight results for the 10 busiest U.S. airports. The classification models developed in this project can be used to aid airlines in making better decisions regarding flight cancellation, leading to improved customer experience and route recovery planning.
