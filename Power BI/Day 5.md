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
2. Demo: Build Data Flows and create reports out of it    
  -Get Data -> Search for dataflow  
3. How to clear Data Source Connections
4. Enterprise level tool - Scalibility, Multiple reports, Governance, etc.
  - Key Players  
  -IBM InfoSphere DataStage  
  -Informatica  
  -SSIS  
  -Power Query (Power BI)  
5. Data Source -> Data Flows -> (Data Set -> Data Modeling ->) Build Reports  
  -Do specific calculations in reports (Visualizations). This way your data model will be generic enough to build multiple reports. **Note: This concludes Power Query**  
### Modeling Data  
1. Introduction  
(This is one of the complex module in Power BI e.g. DAX)  
  -Data Model is a collection of tables with fields and relationship between those tables  
  -IN RDBS, we usually have multiple tables and we denormalize data (flatten data)  
  -In Power BI, there is no need to flatten data (There are some exceptions though). You let Power BI do it using relationships  
  -Data Types, Fact and dimension tables (create start schema in model), Cross filtering, Reduce size of dataset  
  - Data Types - Make sure all columns are in correct data types  
  - Fact and dimension tables - Main (fact) table is at the center (e.g. Sales) and then every other table is like ray (e.g. Customer)  
  Note: In Datawarehousing you would usually use [Star or Snowflake schema](https://techdifferences.com/wp-content/uploads/2017/12/Untitled1.jpg)  
  -Power BI works really welll with either of these schemas, but the data need not to be in these schema types  
  - Cross filtering (Later)  
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
  -SharePoint Online is supported for Automatic refresh. Since both Power BI and SharePoint Online are in cloud, there are hooks to find out if a particular report data source file is changed. If so, the data would automatically refresh 

## Sample Data
Download from [here](https://docs.microsoft.com/en-us/power-bi/create-reports/sample-datasets)

## Lab 5


## Reflect after lesson or lab
