# Power BI

## Discussion Points
#### Data Modes
Import, Direct Query, Composite (Import + direct),  
1. Direct Query   
- Good for very large datasets, which otherwise would be slow if imported into Power BI  
- Near real-time, always current  
 -Only structure is stores in Power BI, data always comes from source  
- Transformation works in Direct Query. It has 2 steps:  
-1. Translate transformation into M langauge  
-2. Translate M language code into SQL. This technique is called Query Folding  
-Right click step -> View Native Query to find actual query  
2. Live Mode  
-Mostly used with Cube service (multidimentional) e.g. SSAS  
-Data Model comes from Cube, so Model and data views are hidden. Additionally, data transformation is not available as well  

| Mode | Date stored in Power BI? | Data Model created in Power BI? | 
| --- | --- | --- |
| Import | Yes | Yes |
| DirectQuery| No | Yes |
| Live | No | No |



## Tips
1. There is no data view for Direct Query  
2. In direct Query data preview is loaded during transformation
3. In direct query transformation are applied at data-source level than Power Query, which is faster
4. One can not go from import mode to direct query, but we can go from direct query to import mode  
5. SharePoint does not supports direct query/live connection. Find more information [here](https://docs.microsoft.com/en-us/power-bi/power-bi-data-sources)

## Sample Data
Download from [here](https://docs.microsoft.com/en-us/power-bi/create-reports/sample-datasets)

## Lab 9


## Reflect after lesson or lab
1. What is Query Folding
