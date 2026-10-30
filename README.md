# Car Data Dashboard

An interactive Streamlit app that explores U.S. fuel economy data from the EPA, from 1984 to today. It shows how engine size affects efficiency and cost, how MPG has changed over the years, and which vehicles are the most and least efficient.

**Live app:** https://fuel-economy-dashboard.streamlit.app/

## Dataset

- **Source:** [EPA Fuel Economy Data](https://www.fueleconomy.gov/feg/download.shtml) (`vehicles.csv`), public domain
- **File used by the app:** `data/vehicles_clean.csv`, 50,363 vehicles (one row per model, year and engine configuration)
- **Columns:** make, model, year, cylinders, fuel type, technology type, combined MPG, yearly fuel cost
- **Cleaning** (done by `clean_data.py`):
  - Only the 8 columns above are kept (the original file has 84)
  - Hydrogen vehicles and rows with no fuel type were removed (44 rows), because the EPA lists no fuel cost for them
  - An empty technology type was filled with "Conventional" (a regular engine with no hybrid, electric or flex-fuel system)
  - Cylinders are stored as whole numbers; electric vehicles have none, so that value is empty
- **Notes:**
  - Yearly fuel cost is the EPA's estimate at today's fuel prices and 15,000 miles per year, even for older cars
  - Electric vehicle efficiency is in MPGe, which is not directly comparable to MPG

## How to use

The top of the page shows the total number of vehicles, the average MPG and the average yearly fuel cost. Below that are five tabs:

- **Engine & Fuel:** average MPG or yearly fuel cost by number of cylinders. Use the radio buttons to switch between the two.
- **Trends:** average MPG by model year. Pick one or more makes to compare them, or leave it empty to see all vehicles.
- **Rankings:** the 10 most or least efficient vehicles. Use the radio buttons to switch.
- **Insights:** key findings from the data and its limitations.
- **Data:** the full table. Filter it by fuel type.

All charts are interactive: hover for exact values, drag to zoom, and click legend items to hide or show them.

## Run it locally

1. Install the packages:
   ```
   pip install -r requirements.txt
   ```
2. Start the app:
   ```
   streamlit run app.py
   ```

The clean dataset is already in the repo, so no download is needed.

### Rebuild the clean dataset (optional)

1. Download `vehicles.csv` from the [EPA download page](https://www.fueleconomy.gov/feg/download.shtml) and put it in `data/raw/`.
2. Run:
   ```
   python clean_data.py
   ```

## Project structure

```
app.py                    Streamlit app: layout, widgets and charts
clean_data.py             Builds the clean CSV from the raw EPA file
data/vehicles_clean.csv   Cleaned dataset the app reads
requirements.txt          Python packages
```

## Built with

- [Streamlit](https://streamlit.io/): web app
- [pandas](https://pandas.pydata.org/): loading and summarizing the data
- [Plotly Express](https://plotly.com/python/plotly-express/): interactive charts
