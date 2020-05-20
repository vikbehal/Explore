# Deno Installation

Below step are optional and installs Chocolatey. Chocolatey is Package Manager for Windows.
## Install Choco
1. Open PowerShel as admin
2. Run either of below commands   
**Set-ExecutionPolicy AllSigned** or **Set-ExecutionPolicy Bypass -Scope Process**
3. Run below command to install chocolatey  
**Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))** 
4. The output should look similar to
![Result](https://github.com/vikbehal/Explore/blob/master/Deno/Artifacts/InstallationResult.PNG)
5. Finally, verify chocolatey by running below command
**choco**
![Verify Choco](https://github.com/vikbehal/Explore/blob/master/Deno/Artifacts/VerifyDeno.PNG)

Learn more: Find more information about Chocolatey [here](https://chocolatey.org/install)

## Install Deno
1. Run below command to install deno  
**choco install deno**  
2. The output shall be similar to  
![Result](https://github.com/vikbehal/Explore/blob/master/Deno/Artifacts/DenoInstallationResult.PNG)

Learn more: Find more information about Deno [here](https://deno.land/)
