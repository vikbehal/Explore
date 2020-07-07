# Power BI

## Discussion Points
#### Power BI API
1. REST APIs to interact with Power BI  
- Three forms:  
-Power BI REST API  
-Power BI .NET SDK  
-Power BI JavaScript API  

2. Typical tasks performed using Power BI API  
- Pushing data to Power BI dashboard  
- Embedding tiles into an app  
- Emdedding reports into an app  
- Importing Power BI Desktop (PBIX) files  
- Authenticating Power BI web apps  

3. Emdedding Power BI content in applications  
- For your organization  
-Configure embedding in SharePoint Online, Microsoft Teams, and Microsoft Dynamics  
-Use Power BI APs to embed in custom applications, accessing content as the user  

- For your customers  
-Use Power BI APIs with Power BI Embedded to embed in custom applications, accessing content with a master account  

4. [Power BI Embedded Playground](https://microsoft.github.io/PowerBI-JavaScript/demo/v2-demo/index.html)  
- Purpose of the Power BI Embedded playground:  
-As a learning resource  
-For trying out Power BI REST API operations without writing code  
-To use API calls to perform specific tasks

#### Customs Visuals
1. Using custom visuals
- Custom Visual files:  
-.pbiviz files containing code  
-May be a privacy or security risk
- Organizational visuals:  
-Custom visuals that a Power BI admin has approved for your organization  
-Cannot be displayed in emails or exported to PowerPoint  
- Marketplace visuals:  
-Tested and approved for functionality and quality  
-Certified visuals - more rigrously tested subset that are supported in email and PowerPoint  
- Importing organizational and marketplace visuals 

2. Creating custom visuals  
- This is an advanced capability  
-Requires software development expertise  
-Needs to be maintaned over time as Power BI platform evolves  
-Typically multiple weeks to months to create a visual  
- Microsoft Power BI visuals project from Github  
-Open-source project  
-Compiles into JavaScript for browser compatibity

## Tips
1. A subset of approved visuals from marketplace can be approved and will show up under Organizational visuals
2. Find custom visual settings under Admin Portal -> Tenant settings -> scroll to Power BI Visuals  
3. Organizational visuals are also available under Admin Portal -> Organizational visuals

## Sample Data
Download from [here](https://docs.microsoft.com/en-us/power-bi/create-reports/sample-datasets)

## Lab 11
1. Try Chiclets and Visio custom visualizations from marketplace

## Reflect after lesson or lab
1. How to allow users to use only Microsoft build custom Visuals?

