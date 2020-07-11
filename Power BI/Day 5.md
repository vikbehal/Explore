# Power BI

## Discussion Points  
Problem Statement: What if we want to reuse Power Query?
### [Data Flows](https://docs.microsoft.com/en-us/power-bi/media/service-dataflows-overview/powerbi-dataflows_01.png)  
1. Introduction  
  -Data Flows allows you to reuse transformations accross reports  
  -Alternatively, you could copy paste same transformation N number of time. If you do so, we have maintenance issue  
  -Data Flows also have performance benifits but the real use is to reusability of transformations  
  -Instead of putting transformation inside reports, put them inside Data Flows  
  a. Data -> Data Flows (Transform here)  
  b. Data Flows -> Build Reports 
  -Data Flow is available on Pro Tier and above    
2. **Demo: Build Data Flows and create reports out of it**  
  -Get Data -> Search for dataflow  
3. How to clear Data Source Connections
4. Enterprise level tool - Scalibility, Multiple reports, Governance, etc.
  - Key Players  
  -IBM InfoSphere DataStage  
  -Informatica  
  -SSIS  
  -Power Query (Power BI)  
5. Data Source -> Data Flows -> (Data Set -> Data Modeling ->) Build Reports  
  -Do specific calculations in reports (Visualizations). This way your data model will be generic enough to build multiple reports.   
  **Note: This concludes Power Query**  
### Modeling Data  
1. Introduction  
(This is one of the complex module in Power BI e.g. DAX)  
  -Data Model is a collection of tables with fields and relationship between those tables  
  -IN RDBS, we usually have multiple tables and we denormalize data (flatten data)  
  -In Power BI, there is no need to flatten data (There are some exceptions though). You let Power BI do it using relationships  
  -Data Types, Fact and dimension tables (create Star schema in model), Cross filtering, Reduce size of dataset  
  - Data Types - Make sure all columns are in correct data types  
  - Fact and dimension tables - Main (fact) table is at the center (e.g. Sales) and then every other table is like ray (e.g. Customer)  
  Note: In Datawarehousing you would usually use [Star or Snowflake schema](https://techdifferences.com/wp-content/uploads/2017/12/Untitled1.jpg)  
  -Power BI works really welll with either of these schemas, but the data need not to be in these schema types  
  - Cross filtering (To be covered later)   
  - Reduce size of dataset - Remove unnecessary data-columns or sensitive data  
2. Data Refresh  
  - Freuqency  
  -Free - 1/Day  
  -Power BI Pro - 8/Day  
  -Premium - 48/Day using UI; unlimited using API
  - Refresh Options  
  -Refresh Now (manual)  
  -Scheduled refresh  e.g. everuyday at 3 PM (just like windows scheduler)  
  -Automatic refresh 
  -Only available for certain type of data types   
  -SharePoint Online is supported for Automatic refresh. Since both Power BI and SharePoint Online are in cloud, there are hooks to find out if a particular report data source file is changed. If so, the data would automatically refresh (within a few minutes upto an hour)  
  -One drive for business is also supported for Automatic Refresh  
  - Only "Import" connection requires refresh  
  -DirectQuery and Live connection mode do not require refresh to be configured (To be covered later)  
  - Best Practices  
  -Schema must remain same (This is more of a issue with files created manually e.g. Excel. Databases have strong change management system so those are more reliable)  
  -Name of the file must be same  
  -**Demo: Parameters**  
  -File type must be same  
  -Data Structure must be largely same  
  -Power BI ignores format changes to columns  
  -New columns can be added without breaking refresh  
  -Removing column might break the refresh
3. Managing data relationships  
  -Primary Key & Foreign Key  
  -In Power BI, you can only have single column for PK & FK  
  -Compound kets are not supported  
  -Question: What if we do have a one column representing PK or FK?  
  -Option 1: Merge two or more columns to create PK/FK  
  -Option 2: Unique row number (just like ID column in SharePoint). In Database terms this is called Identity column  
  -**Demo: 1) Add Custom column to create a Primary Key** (Add Column -> Custom Column; & as separator) 2) Create Index column (ID/Identity)  
4. Optimizing Data Model  
  - Hide columns (It does not remove them from Data Model)  
  -Right click under Fields pane to see hidden columns  
  -Switch to Data View to find hidden field
  - Sorting  
  -By default every field is sorted by itself  
  -At times you may want to sort field based on another field e.g. Month Names  
  -**Demo: Create Order column for Day of Week data** (Enter Manually). Hide Column Order column   - Format  
  -Change Data types, add currency symbol, or format date type columns, etc.
  

## Sample Data
Download from [here](https://docs.microsoft.com/en-us/power-bi/create-reports/sample-datasets)

## Lab 5
1. Create a Data flow using Power BI Service and create at least 2 reports out of it
2. Research how you can use APIs to refrsh data in Power BI Premium Service  
3. Replicate demo of how to Create custom columns, sort columns based on other columns, etc.

## Reflect after lesson or lab
1. What are Data Flows?
2. What problem do Data Flow solve?
3. How can you use Power Query in Power BI Service?
4. What is Data Modeling?
5. Do we needto denormalize data in Power BI?
6. What is the difference between Star and Snowflake schema?
7. Can we build reports in Power BI without Start or Snowflake schema?
8. What is a fact table?
9. What are the 3 main ways one can refresh data?
10. Does all data-sources support Automatic Data Refresh?
11. Under what conditions Data Refresh might fail?
12. Will all of the reports will stop working when Data Refresh fails?
13. What are Parameters? What is the use of them?
14. How can we sort data which is naturally not sorted in desired format. E.g. Name of months
