# Power BI

## Discussion Points
### DAX - Data Analysis Expressions is a formula language
1. Introduction  
-Use DAX or calculate and return single value, or multiple values  
-DAX already exists in Power Pivot for Excel, SSAS and Power BI. It is designed to work with relational data  
-Perform calculations like year-on-year sales, running total 
-It is used to for dynamic calculations  
2. DAX Formulas
-DAX is fairly complex, so it is used for dynamic calculations. Power BI provides inbuild functions for common transformations, for which DAX should not be used  
-DAX formulas must be syntactically correct before you can save them to the model.  
-Sample **Measure/Calculated Column = calculated function**  
-DAX functions are predefined formulas that perform calculations on one or more arguments  
-You can pass a column, expression, formula, constant, number, text, TRUE or FALSE as arguments  
-DAX library has 200+ functions  
3. Context - It changes the result of function without changing the function itself. In programming language functions typically take input. In Power BI functions typically don't take input (sometimes they do), but the input is context  
-Row Context and Filter Context  
-Row Context is the current row. Often applied to measures to identify a single row  
-Filter context - Exists in addition to row context. It incorporates any explicit filters (filter panel) and implicit filters (visualization level). Filter context changes on the fly  
-Filter contexts are used in visualizations; e.g. a chart with Sales, Sales person, and month. The chart returns subsets of data based on a specific Sales Person, and Month  
-You can apply filter contexts using visualizations, and DAX  
4. One can create 3 type of entities using DAX  
- Calculated columns  (Not so often used)
-Calculated columns are added to tables using DAX formulas to perform operations on existing data  
-Columns created using DAX instead of Power Query or data source  
-Useful when the model does not have the data you need  
-Concatenate strings, calculate numbers, or combine data from elsewhere in the model  
-After creating, use in visualizations as you would any other column  
- Calculated tables  (Not so often used)
-Create calculated tables using data that exists in the model  
-Use functions such as UNION, NATURALINNERJOIN, NATURALOUTERJOIN, or DATATABLE  
-Calculated tables are used in the same way as other tables. Rename table and columns, use in relationships with other tables, change data types, add columns, measures, and use in visualizations  
-Sometimes it is used to create a Date table for a range of dates e.g. 1900 - Today (2020)  
- Measures (Most commonly used)
-Measures help you discover insights into your data that might otherwise be hidden  
-Include aggregations in your measures, such as average, minimum, maximum, count distinct DAX functions  
-Use other DAX functions to create complex calculations  
-**Useful to highlighting running totals, comparing sales this year to date with sales for the same period last year, and sales forecasting**  
-Measures are used in visualizations like columns with some limitations e.g. they can not be used on Axis because it does not distinct values since they are calculated




## Tips  


## Sample Data
Download from [here](https://docs.microsoft.com/en-us/power-bi/create-reports/sample-datasets)

## Lab 6


## Reflect after lesson or lab
