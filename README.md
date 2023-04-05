Analysis of IBB Istanbul Weather and Traffic Dataset
====================================================

This project is an analysis of the Istanbul Weather and Traffic Data based on datasets extracted Istanbul Metropolitan Municipality data portal.

Data Extraction
-----------------
The data is extracted from [IBB Istanbul Weather Data](https://data.ibb.gov.tr/dataset/meteorology-observation-station-data-set) and [IBB Istanbul Traffic Density Data](https://data.ibb.gov.tr/dataset/hourly-traffic-density-data-set) using SQL commands. Extracted data consists of results from 2020-01 to 2021-04.

'get_hourly_figures.ipynb': This file contains the SQL queries to extract hourly aggregated data store the results in csv --> 'weather_hourly_agg.csv' and 'traffic_hourly_agg.csv'

'final_data.csv': This file contains the final merged data from weather and traffic files

Analysis
-----------------
* **Exploratory Data Analysis**: The relationship among variables are explored, such as average temperature, number of vehicles. Various statistical methods and data visualization techniques are used to gain insights into the data.
* **Time Series Forecasting for Weather**: ARIMA Model is used for time series forecasing to predict the daily average temperature

Technologies Used
-----------------

*   Python
*   Pandas
*   Matplotlib
*   SQL

Future Improvements
-------------------

This project can be improved in the following ways:

*   Adding more data to the dataset to provide a more comprehensive analysis.
*   Conducting further analysis on the relationship between weather conditions and traffic density.
*   A multivariate Time Series Forecasting can be applied to traffic density (Number of vehicles)

