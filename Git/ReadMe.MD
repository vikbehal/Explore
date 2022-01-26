**git clone <url>  **  
**git add <filename>**  
#Add mentioned file to the list of files I will commit next time. Adds files to staging area.  
**git commit -m "message" **   
#Add relevant message  
**git status**  
#To find out what is going on in current repository  
**git push  **
#Push changes to server  

**Typically, do this:  **  
Make changes -> git add -> git commit -> git push  

**git pull  **
#Get latest changes from server and bring them here. This is when someone else has updated repository and we want to get them.  

#Conflict may happen while pulling, which is often the case if same lines are modified locally and on server as well. We need to manually resolve them and then commit & push. Do this  
fix the issue -> git add -> git commit -> git push  

**git log  **

**git reset  **
#go back to particular commit, origin, or branch  
**git reset --hard <commit> **
**git reset --hard origin/master  **

#branching is helpful while working on new features. Typically there is master and HEAD points to it but we can branch and point HEAD to branch. So, we work on that branch. Later we can merge the branch with master.  
git branch #tells me all branches  
git checkout #checks out to a specific branch  
**git checkout -b <branch-name>** #creates new branch and checks it out  

Do this  
branch using commit -> make changes -> git add -> git commit  

#Once ready, merge it  
**git merge <branch-name> ** 

#You may not push changes  

#If branch is no longer required, delete it. This is hard delete.  
git branch -D <branch-name>  

### Do branching for building new features. Below is an example where red is new feature branch
#git branch -b red  
#make changes  
#git commit -am "message"  
#error because red does not exist on server  
#git push --set-upstream origin red  

#Now you have 2 branches on github. master and red. You may now propose the change using "pull request"  
#Someone who owns repository can now look into the proposed changes and then have option to accept/merge changes.  
#You may now delete red branch  

#Collaborators can do it. From settings.  

#Shorthands  
**git commit -am  **
#Add all changed files and then commit  

**git add . ** 
#add everything that has changed  

Source: https://www.youtube.com/watch?v=eulnSXkhE7I  
