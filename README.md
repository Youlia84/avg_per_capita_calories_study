# avg_per_capita_calories_study

<h2>A Study of Loss-Adjusted Food Availability in the United States</h2>

<b>Link to app</b>
https://youlia84-avg-per-capita-calories-study-app-ozbtam.streamlit.app/

<b>Data Source</b>

The data was obtained by the USDA.  All CSV files can be found here: https://www.ers.usda.gov/data-products/food-availability-per-capita-data-system/

<b>Introduction: Domain problem characterization</b>

I wanted to understand whether there were any trends or patters in the food consumed in the United States.

<i>Tip: Choose the Dairy or Sugars filter on the Details tab to see some pretty interesting trends!</i>

<b> Data/operation abstraction design</b>

I used the calories.xlsx file from the USDA's website.  The Totals tab remained unchanged, thought I pivoted it in Python so the data could be vertically organized for easier visualization.

I also manually rearranged the different food tabs in the calories.xlsx file into one details tab, such that each food category and two sub categories were again vertically organized; this data was then aggregated into different data frames for visualization.
 
<b>Future work</b>

It would be fascinating to obtain more granular geographic data to see if some trends are driven by a certain region of the country.
