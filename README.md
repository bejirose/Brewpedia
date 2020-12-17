# Brewery Data Analysis

## Hypothesis
Expect IPA to be the most consumed style globally due to the high Alcohol By Volume (ABV) and International Bitterness Unit (IBU). For this:
  - we identified brewery counts by country, state, city
  - found top beer type for each country
  - identified Amount of beer brewed by state vs number of breweries
  
## Data Source Limitations
  - Unable to get API Key (Untappd API, TripAdvisor API)
  - Limited API request calls (Beermapping API – dropped it)
  - Limited datasets (Google API, Rapid API)
  - Limited documentation (Rapid API)
  - Static data for data analysis in .csv format (Kaggle.com)
  - Paid membership required to BrewerAssociation.com for yearly data, actual production volumes of breweries
  - OpenBreweryDB – 25 results/page max but can iterate over index pages
  - Bad data
  
## Data Extraction and Tranformation
  - Queried breweryDB API
  - Cleaned the data with no Latitude and Longitude

## Data Search on Pandas
- Created Jupyter Notebook to search the data by Beer Name or Brewery

## Data Visualization
  - Marked latitude and longitude on the map on the mean coordinates.
  - Creatd Heatmap on rating and pinned on Brewery Name, Website, Location
  - import Pandas ipywidgets as widgets for drop down menus
  ### Plots
  - Created the following bar plots:
    1) Bar plots for breweries by countries
    2) Most beer style for Belgium and Germany
    3) Number of Breweris in the US for each state
    4) Cities with most number of breweries in the US
    4) Most Brewed Beer Style in the world
    5) Beer with Highest ABV
    6) Alcohol Volume By US States
    7) Market Share of Top 5 US Brewers
 - Created the following line plots:
    1)  Line plot on 2019 Gallup poll results for  Spirit, Wine, and Beer
