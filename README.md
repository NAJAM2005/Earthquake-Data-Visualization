🌍 Earthquake Data Visualization Dashboard

A Python-based data analysis and visualization dashboard that explores global earthquake and tsunami patterns using historical data. Built with Pandas, Matplotlib, and Seaborn.


📊 Visualizations

The dashboard generates 4 insightful charts from the dataset:

ChartDescription🟣 Earthquakes Per YearCount plot showing earthquake frequency trends over time🔴 Average Magnitude Per YearLine chart tracking how earthquake intensity changed over the years🌊 Tsunamis Per YearBar chart showing tsunami occurrence frequency per year🔵 Magnitude vs DepthScatter plot revealing relationship between depth and magnitude, colored by tsunami occurrence


🚀 Getting Started

Prerequisites

bashpip install pandas matplotlib seaborn

Run the Dashboard

bashpython main_earthquake.py

The script loads earthquake.csv, prints a data summary, and generates all 4 charts automatically.


📁 Project Structure

earthquake-data-dashboard/
│
├── main_earthquake.py   # Main analysis and visualization script
└── earthquake.csv       # Historical earthquake dataset


🔍 Dataset Features

The dataset includes the following columns used in analysis:


Year — Year the earthquake occurred
magnitude — Richter scale magnitude of the earthquake
depth — Depth (km) at which the earthquake occurred
tsunami — Whether the earthquake triggered a tsunami (0 = No, 1 = Yes)



💡 Key Insights This Dashboard Reveals


Which years had the highest earthquake activity
Whether average earthquake magnitude has increased or decreased over time
The correlation between earthquake depth and magnitude
How often earthquakes trigger tsunamis and in which years



🛠️ Tech Stack


Language: Python
Libraries: Pandas, Matplotlib, Seaborn
Techniques: Data cleaning, aggregation, multi-chart visualization, geospatial trend analysis



👤 Author

Najam Ul Hasan
BSCS Student — Government College University Faisalabad
GitHub | Email
