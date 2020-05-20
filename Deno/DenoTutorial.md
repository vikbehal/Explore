## Check if deno is installed
> deno  
![Output](https://github.com/vikbehal/Explore/blob/master/Deno/Artifacts/DenoREPL.PNG)

## Check helper functions 
> deno help  
![Output](https://github.com/vikbehal/Explore/blob/master/Deno/Artifacts/Denohelp.PNG)

## run code  
> deno run server.ts
Note: Above will not work. You need to allow certain things for security reasons
![Output](https://github.com/vikbehal/Explore/blob/master/Deno/Artifacts/RunDeno_Error.PNG)

## run code (This will work!)
> deno run --allow-net --allow-env server.ts
> deno run --allow-net --allow-env lcoapi.ts
![Output](https://github.com/vikbehal/Explore/blob/master/Deno/Artifacts/RunDeno_WithSecurity.PNG)
