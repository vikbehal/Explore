# Power BI

## Discussion Points  
Problem Statement: What if we want to reuse Power Query?
1. [Data Flows](https://docs.microsoft.com/en-us/power-bi/media/service-dataflows-overview/powerbi-dataflows_01.png)  
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
**Note: This concludes Power Query**  
5. Data Source -> Data Flows -> (Data Set -> Data Modeling ->) Build Reports  
  -Do specific calculations in reports (Visualizations). This way your data model will be generic enough to build multiple reports.


## Sample Data
Download from [here](https://docs.microsoft.com/en-us/power-bi/create-reports/sample-datasets)

## Lab 5


## Reflect after lesson or lab
