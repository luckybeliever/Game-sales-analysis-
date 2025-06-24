# Game Sales Data Analysis

## Objective
The goal of this project is to explore, clean, and visualize video game sales data. The analysis helps us understand game performance across regions, top publishers, sales trends, and market share.

## Dataset Description
This project uses a filtered and cleaned version of the **Video Game Sales** dataset (originally known as `vgsales`). It contains details about game names, platforms, release years, genres, publishers, and regional/global sales figures.

- **Original Source**: vgsales.csv
- **Filtered Rows**: Removed missing or incomplete entries
- **Final Records**: 16,291 games

## Tools & Technologies Used
- Microsoft Excel (Power Query, Pivot Tables, Charts)
- Power BI (for advanced visualizations)
- CSV for dataset storage and cleaning
- GitHub (for project sharing and version control)

## Process Overview
1. **Data Cleaning**  
   - Removed null values
   - Filtered out games without proper sales or year information

2. **Data Transformation**  
   - Grouped data by genre, publisher, year, and platform
   - Added calculated fields like average sales per region

3. **Visualization**  
   - Created an interactive dashboard in Excel
   - Included pie charts, bar graphs, and line charts to show trends and insights

## Key Insights
- **Total Games Analyzed**: 16,291  
- **Average Global Sales**: $0.54 Million  
- **Most Games Published By**: Electronic Arts  
- **Top Console by Sales**: PS2  
- **Leading Genre**: Action  
- **Year with Peak Game Releases**: Around 2009  
- **Highest Market Share**: Nintendo

## How to Use This Project
1. Download the cleaned CSV file and Excel dashboard.
2. Open the `.xlsx` file to interact with the dashboard.
3. Use slicers (Genre, Year, Date) to filter and explore different aspects of the data.

## Suggestions for Improvement
- Add more recent data to cover post-2016 game sales.
- Include critic/user scores to analyze quality vs sales.
- Use Python (Pandas/Matplotlib/Seaborn) or Power BI for deeper insights and automation.
- Build a web dashboard using tools like Tableau Public or Streamlit.
- Add predictive modeling to forecast future game sales.

## Conclusion
This project provides a simple but informative analysis of global video game sales data. It highlights how genres, publishers, and platforms perform over time. The dashboard makes it easy to interact with and draw conclusions for both casual viewers and business users.
