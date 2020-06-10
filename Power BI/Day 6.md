# Power BI

## Discussion Points
### Data Modeling  
1. Hierarchies  
  -In Power BI hierarchies enables drill-down into your data  
  -A hierarchy is a set of related fields grouped together  
  -Each level is contained within next level and does not exist independently E.g Country, State, City  
  -Time intelligence: Power BI automatically creates drill-down on date columns for: Year, Quarter, Month, Day  
  -Can also use DAX time intelligence functions to aggregate date for specific time period  
  -Product Lines, Organization, Date, Areas, etc. are all suitable for hierarchies
2. **Demo: Hierarchies**  
3. [Tooltips](https://docs.microsoft.com/en-us/power-bi/desktop-tooltips)  
4. Filters  
  -You can set filters on 1) all pages 2) single page 3) specific visual  
5. **Demo: Filters**  
6. Relationships  
  -Power BI Autodetect feature can recognize relationships, and create them automatically  
  -E.g. In RDBS, it will use schema information (and Primary and Foreign Keys)  
  -E.g. In Excel, it will use column names and information in fields to make guess  
  -When Power BI detects more than one relationship between tables, **only one can be active** and set as default  
  -You can either let Power BI detect relationships or create them manually  
  -Typically a hybrid approach works best. You let Power BI detect relationships and then manually add missing, remove unwanted to adjust required relationships  
  -*If you can't create a relationship, it is probably because of NULL, empty values, or duplicate rows*  
  -*It is absolutely important that data relationships are valid. if not, they might break your visuals or even show incorrect data*  
  -**Relationhip types** - Cardinality, Cross Filter Direction, Active/Inactive flag   
  - Cardinality  
  -It is a relationship between two tables  
  -1:1,*:1, 1:*, *:* (* stands for many)  
  - Cross Filter Direction  
  -This relationhip affects how Power BI treats the tables in visualizations  
  -The cross filter direction is automatically set when relationships are created manually or using Autodetect    
  -Power BI makes best guess at direction  
  -This guess can be adjusted manually  
  -Types: Both, Single  
  -Both: First tables will filter second and second will filter first as well  
  -Single: First will filter second but second will not filter first  
  - Active/Inactive flag  
  -Each relationship in Power BI must be either active or inactive  
  -Active relationships  
  -Indicated by solid line  
  -Used automatically everywhere e.g. when column is dragged into report  
  -Inactive relationship  
  -Indicated by dotted line  
  -Usable relationship only with special DAX functions
7. **Demo: Relationships**  
   -*It is important to setup data model properly otherwise Data Refresh might fail. E.g. if you have a 1:M relationship which is incorrectly mapped as 1:1, and Data Refresh brings data which does not conforms to 1:1, the Data Rerfesh would fail*
  
## Tips  
1. Ctrl+C, Ctrl+V to duplicate a report  
2. You can duplicate entire report page by right click -> Duplicate page

## Sample Data
Download from [here](https://docs.microsoft.com/en-us/power-bi/create-reports/sample-datasets)

## Lab 6
1. Create a Data Model which has hierarchies except Date hierarchy. Ensure your data has Date field. Observe automatically created Date hierarchy
2. Build a report out of lab in step 1 above. For this report create all 3 types of filters
3. Finally, Import more than 3 data-sources (SharePoint lists, Excel files, etc.) and make sure relationships are properly defined. You shall check Cardinality, Cross Filter Direction and Active/Inactive flags

## Reflect after lesson or lab
1. How many times of filters can we create in Power BI reports?  
2. What is the difference between All pages and Single page filter?
3. What is a tooltip? Can we create a pie-chart as tool-tip?
4. Define Relationships?
5. What are types of relationships?
6. What is Auto Detect?
7. Give an exampe of when Data Refresh may fail due to wrong Data Model
8. Can two tables have more than 1 relationship?
9. What is the difference between Active and Inactive flag?
10. What difference does Active and Inactive flags make in reports?
