# Power BI

## Discussion Points
1. Data Types  
  -Files, SQL Server, Other data-sources, R & Python
  - Files  
  -Connect to files from Power BI Desktop or Service  
  -Compatible types include Excel, CSV, XML, and JSON
  - Folder connector  
  -Demo  
  - From Power BI Service connect to local files, OD4B or Personal One Drive, SharePoint  
  -Maximum file size would be 250 MBs  
  - Power BI Desktop has more source connections than Power BI Service  
  - SQL Server  
  -All recent versions up to SQL Server 2019 are supported  
  -Similarly SQLs cloud versions are also supported
  - Saas providers include Bing, Google Analytics, facebook, Salesforce, Github, etc.  
  - Supports other databases like Access, Oracle, DB2, MySQL, etc.  
  - Connect to any webpage to scrape structured data (Demo)
  - R & Python  
  -Install and use R & Python to generate data or visuals in Power BI Desktop  
  -Power BI Service already includes commonly used libraries  
  -This feature is not supportd in Power BI Report Server  
2. What is MarketPlace?  
3. Migration of legacy reports into Power BI  
  -Demo
4. Web Scrapping Demo  
  -Import data from a website that provides data in tabular structure  
  -Import using Get Web, Web  
  -be aware that source data could be removed
5. Data Transformation  
  - Introduction to Power Query and its need  
  -Powery Query Editor enables you to load data and apply transformations  
  -Ribbon has four tabs - Home, Transform, Add Column and View  
  -Home: Import data, hide or delete columns, reduce rows, merge and append queries  
  -Transform: Create aggregated columns, transpose, pivot, unpivot, split values  
  -Add Column: Add columns, add indexex, apply functions  
  -View: Show or hide the query settings pane
  - Applied Steps  
  -Query Editor records all transformations to a query in the Applied Steps setting  
  -All transformations are listed in order of creation  
  -Navigation includes select tables and views  
  -Can reorder, delete, undo or rename steps  
  - Advanced Editor  
  -It shows actual query written in M Power Query Formula Language  
  -The list of steps mentioned in the query are in the same order as transformation steps  
  -You can edit the query, but use syntax checker
6. Demo: Append and Merge in Power Query  
  - Merge one table into another using a joining column  
  -Choose from join types  
  -All columns are initially merged, but use the selector to choose which columns you want to keep  
  - Append rows from one or more table to another table  
  -Column data does not have to match  
  -Mismatching can result in unclean data and nulls  
  -Add index to combine table

## Sample Data
Download from [here](https://docs.microsoft.com/en-us/power-bi/create-reports/sample-datasets)

## Lab 4
1. Migrate a legacy Power View report to Power BI and find what works and what does not (Limitations of migrated report in Power BI)  
2. Use web scrapping technique to fecth data from Internet and build reports   
3. Explore Marketplace and import 'Play Axis (Dynamic Slicer)' chart and build Animated Power BI using it  
4. Perform data transformation. You shall at least rename, remove, move, naming moves, Append and Merge

## Reflect after lesson or lab
1. How to you import legacy Excel Reports into Power BI?
2. Can I using Oracle DB as data-source? Do I need any setup to use Oracle DB?  
3. What is the use of R & Python in Power BI?  
4. What is MarketPlace?  
5. What is Web Scrapping? How does it help in Power BI?
6. What is Power Query?  
7. How do you find algorithm behind data transformation?
8. What is Merge and Append in Power Query?
