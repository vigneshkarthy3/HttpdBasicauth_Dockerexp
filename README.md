# Http_Basic_Auth

As you were curious on the hours took for completion was around 3-4 max, with distractions in my house :D.

I used a Docker image pulled from nginx latest image and provided with a Dockerfile and .htpasswd to pass our admin username and password "e-bot7".
Securing the app with the http basic auth.

From my point of view,
Each access to the page can be passed to mongodb collections named "access" either by Full-load (Truncate and import data) or incremental Load (Import with last updated date incrementally). Incremental load might be efficient way to use incase of larger data. I proceeded with Full load as it will be easier to demonstrate and might take some time to write up the script. I will demonstrate on how this can be done incrementally in our next interview.

I used three Docker containers, 

1) Nginx on nginx layer
2) Database on mongodb layer
3) Script on ubuntu layer ( scheduling the script periodically) (Volume mounted from nginx on logs)

Script will load the data and finds if there's more than 10 access denial, then emails to the respective email provided in the script. I have removed my password from "script.py" as you can provide your username and password before running the Docker-compose file.

To not to have the email on spam or rejected, Please enable your alert email id with IPAM and turn on less secure app access if it's a gmail. 

# Start the script

docker-compose up --build -d