# Game Sales Data Analysis

## Objective
The goal of this project is to explore, clean, and visualize global video game sales data. The analysis aims to highlight patterns in sales, identify best-selling platforms and publishers, and provide insights into the gaming industry's trends over the years.

## Dataset Description
This project uses a cleaned version of the **Video Game Sales** dataset (`vgsales.csv`), filtered to remove missing or incomplete entries.

- **Source**: vgsales dataset
- **Cleaned & Filtered Rows**: Only valid games with proper sales and year info
- **Final Dataset Size**: 16,291 games

## Tools & Technologies Used
- **Microsoft Excel** (Power Query, Pivot Tables, Slicers, Charts)
- **CSV** (Data Storage)
- **GitHub** (Project Hosting and Sharing)

## Process Overview
1. **Data Cleaning**
   - Removed null or missing values
   - Excluded records without valid year, genre, or sales data

2. **Data Transformation**
   - Grouped data by genre, publisher, console, and year
   - Calculated total and average sales across regions

3. **Visualization**
   - Built interactive dashboard using Excel slicers and charts
   - Added line charts, bar graphs, and pie charts for key insights

## Key Insights
- **Total Games Analyzed**: 16,291  
- **Average Global Sales per Game**: $0.54 Million  
- **Average Regional Sales**:  
  - North America: $0.27M  
  - Europe: $0.15M  
  - Japan: $0.08M  
  - Other Regions: $0.05M  

- **Most Released Genre**: Sports  
- **Highest Selling Genre (Global Sales)**: Platform  

- **Year with Most Game Releases**: Around 2009  
- **Top Publisher by Game Count**: Electronic Arts  
- **Top Selling Console**: PS2  
- **Market Share (by Publisher)**:
  - Nintendo: 26%
  - Electronic Arts: 21%
  - Activision: 13%
  - Others include Ubisoft, Sony, and more

## How to Use This Project
1. Download the CSV and Excel dashboard from this repository.
2. Open the Excel file to explore the dashboard.
3. Use the slicers (Genre, Year, Platform) to filter and analyze specific segments.
4. View trends across time, publisher performance, and sales region-wise.

## Suggestions for Improvement
- Integrate review scores (Metacritic, user ratings) for more detailed analysis.
- Build dynamic dashboards using Python or Power BI.
- Extend dataset beyond 2016 with newer game releases.
- Predict future sales using machine learning models.
- Create a web-based version of the dashboard using Tableau or Streamlit.

## Conclusion
This project provides a clean, interactive, and insightful analysis of video game sales data. The dashboard helps users quickly identify trends by genre, year, publisher, and platform. It’s useful for game enthusiasts, business analysts, and anyone interested in the gaming industry.

---
