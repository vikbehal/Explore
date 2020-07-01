# Power BI

## Discussion Points
### Visualizations
1. Types - Charts, Cards, Maps, Tables and Matrices, Tree maps    
#### Charts
- Bar and column charts  
- Line and area charts  
- Line and column charts  
- Funnel charts  
- Scatter charts
- Bubble charts
- Pie charts
- Donut charts
#### Cards
- Cards present most important data first:  
-If users normally read left to right and top to bottom, show most important data in top left  
- Card chart:  
-Display a single numeric value, such as Total Sales  
-Optionally displays data label and title  
- Multirow card chart:  
-Shows multiple numeric values, useful for small datasets, such as Main Category and Total Sales  
-Optionally include the data labels and a chart title  
- KPI  
-Visualize a business objective and show progress towards the goal  
#### Maps
-Microsoft maps use Bing maps technology  
- Map chart  
-Represents data as propotionally sized, color-coded bubbles -Good for data based on cities  
- Filled map chart  
-Uses shading accross a region; darker shades for higher numbers, or rather, high density  
-Useful for demographic data  
- ArcGIC map chat  
-Uses points, areas, clusters, heat maps  
-Can analyze your data against demographic layers  
#### Tables and Matrices  
- Display data in columns and rows  
-Useful for displaying numeric data, such as financials  
-Each numeric column is aggregated  
- Table  
-Best for small datasets  
-Includes very little visual formatting  
-Data must be read to be understood  
-Consumes a lot of space on the report canvas  
- Matrix  
-Can add rows, columns, and values  
-Can enable drilldown  
#### Tree Maps
- The tree map functionality represents a tree, even though it does not look like one  
-Data represented as a rectangle or branch  
-Branch can be further divided into nested rectangles, or leaves of a branch  
- Represents data hierarchically  
- Efficient use of space  
-Flattens data to show two layers - e.g. sales by country, with each country broken into territories  
-No need to drill down  
#### Demo of Visualizations  
#### Formatting Charts  
- All charts can be customized with colors and borders  
-Show or hide a chart title, change font and size  
-Set X and Y position, width and height of each chart  
-Show or hide axis, data labels, or legends  
-Set colors od data points - e.g. all columns - or by each value  
- Add shapes, text boxes, and images  
-Use shapes to group related visuals  
-Use text boxes to add headers or create hyperlinks  
-Add corporate logos, pictures, or photos to enhance report  
- Right-click bar or line: drill down to underlying records  
- cutomize tooltips by adding extra fields  
- Quick measures quickly change the aggregation on a field  
- Add trend, constant, and dynamic reference lines to charts  
#### Page layouts and formatting
-Customize each report using formatting options  
- Page name: give each report a name to describe the content, rather than the Power BI default Page 1, Page 2  
- Page size: default aspect ratio is 16:9. Change to 4:3, Cortana, Letter, or set width and height in pixels using Custom Option  
- Page background: change the background color and transparency. Use theme color, or own color. Use image to create highly customized reports  
- Page view: alter the zoom on the page. Default is Page view-fits all visuals onto screen. Choose Actual Size for one-to-one pixel mapping
#### Working with multiple visualizations
-Use Settings and formatting to ensure multiple visuals interact correctly on a report  
- Visual relationships 
-Filter: Only show corresponding data  
-None: Show all data, do not interact  
-Highlight: show all data, corresponding values highlighted  
-Typically visualizations on the same page are interactive i.e. if you click on a part of one chart, say, pie chart, all other visuals on the page will be filtered based on that selection. This is because of the relationships that are present in the model  
-You may choose to keep one (or some) visualizations static by editing interaction setting. To change it, Select source visual, click on 'Edit interactions' under Format tab, select destination visual (the visual that you intend to keep static), and then click on 'None'. Then, exit 'Edit interactions'. Do this for every [source] visual present on the report  
- Show items with no data: displays items with empty values, value of 0 included by default  
- Default summarization: change from the default sum to average, minimum, maximum, count or count distinct  
- Default categorization: e.g. ensure address fields are categorized as City rather than Country, or State  
- Arrange report elements: sending visuals forwards or backwords to create layers-known as z-order


## Tips  
1. [ersi's](https://www.esri.com) is a good place for getting inspiration for geographical chats  
2. Filled maps which  takes the shape of geographic (polygons) area e.g. each state of U.S. are called Chroropleth  
3. Matrix typically has dynamic columns and rows, whereas table has fixed columns  
4. Maps can sometimes show data in wrong position, this happens if the geocoder had to guess. E.g. Cambridge location is in Boston, US as well as in the UK. Now if you are developing maps from US, it might guess Cambridge in Bosotn. To correct this, consider creating a single field which helps geocoder to map it correctly e.g. City, State, Country, ZipCode

## Sample Data
Download from [here](https://docs.microsoft.com/en-us/power-bi/create-reports/sample-datasets)

## Lab 8
1. Create visualizations mentioned above and try formatting charts and page layouts  
- Build map chart using Address, City, State, Country, Zipcode. Make sure Data Category is correctly given to each one of the column  
-Full address can be created using formula
```
FullAddress = Customers[AddressLine1] & ", " & Customers[City] & ", " & Customers[StateProvince] & ", " & Customers[CountryRegion] & ", " & Customers[PostalCode]
```
- Internal columns/tables can be hidden using 'Hide in report view' feature
2. Create bar charts with Constant Line from Analytics tab. Not all reports has this feature

## Reflect after lesson or lab
