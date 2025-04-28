Project Title
Analysis on Used Bike Sales Dataset

Project Description
This project presents an in-depth Exploratory Data Analysis (EDA) of a used bike sales dataset. Using Python and its powerful libraries, we extract key insights into market trends, customer preferences, resale price dynamics, seller behavior, and more.
The goal is to assist buyers, sellers, and marketplaces in making data-driven decisions by analyzing real-world data.

Dataset
Name: cas2.csv

Attributes:

Brand, Model, Year of Manufacture

Engine Capacity

Price, Resale Price

Seller Type (Individual, Dealer)

City Tier (1, 2, 3)

Fuel Type

Insurance Status

Tools & Technologies Used
Programming Language: Python 3.x

Libraries:

Pandas (Data Manipulation)

NumPy (Numerical Operations)

Seaborn and Matplotlib (Data Visualization)

Regex (Text Cleaning)

Development Environment:

Jupyter Notebook / Visual Studio Code (VS Code)

Project Structure
bash
Copy
Edit
├── data/
│   └── cas2.csv
├── notebooks/
│   └── used_bike_analysis.ipynb
├── outputs/
│   ├── graphs/
│   └── summary_reports/
├── README.md
├── requirements.txt
└── report.pdf
Key Analysis Performed
📊 Sales Contribution by Seller Type (Pie Chart)

📈 Mileage Distribution (Histogram + KDE)

🏍️ Top-Selling Bike Brands (Bar Plot)

🔥 Impact of Engine Capacity on Resale Value (Scatter Plot)

🏙️ Resale Price Variations by City Tier (Box Plot)

📉 Outliers in Resale Price (Histogram)

🔧 Depreciation Rates across Brands (Line Plot)

🛡️ Insurance Coverage Trends by State (Stacked Bar Chart)

⛽ Fuel Type Preference (Bar Plot)

📍 Regional Analysis - Bikes Sold per State (Bar Chart)

🧩 Correlation Analysis between Features (Heatmap)

📅 Price and Resale Price Trends over Years (Line Plot)

🏷️ Brand-wise Resale Price Spread (Box Plot)

Main Findings
Dealers dominate the resale market.

Mileage generally ranges between 40–60 kmpl.

Top-selling brands are Hero, Honda, and Bajaj.

Bikes in Tier 1 cities fetch higher resale prices.

Older bikes show greater depreciation.

Petrol bikes are the most preferred.

Insurance coverage varies significantly by state.

Future Scope
Build a machine learning model to predict resale prices.

Create a bike recommendation system based on user preferences.

Develop interactive dashboards for real-time analytics.

Integrate external datasets like accident history, road conditions.

How to Run the Project
Clone the repository or download the files.

Install the required libraries:

bash
Copy
Edit
pip install pandas numpy matplotlib seaborn
Open the Jupyter Notebook or Python file.

Load the dataset cas2.csv.

Run the cells/sections sequentially to generate analysis and visualizations.

Author
Name: Akepogu Sampath Kumar

Registration No: 12326876

Course Code: INT-375

Program: Data Science (K23EL)

Institution: Lovely Professional University, Punjab

License
This project is for educational purposes only.
