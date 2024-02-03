# Error
## Error: listen EADDRINUSE: address already in use :::3000
```sh
lsof -i :3000
```
or
```sh
netstat -anp | grep 3000
```
## why
docker did not stopped
check
```sh
docker ps
```
so do
```sh
docker stop <container_id>
```
**Nope** so maybe not ```config.env```
**ohh yesss this thing is terrible**
- can use ```config.js```
- or maybe set it in Dockerfile using
```sh
ENV NODE_ENV=production
```
Assuming this is the line in ```config.env```
OR
Maybe do this for the entire file:
```sh
COPY config.env .env
```


# Kong
- ```--network=host``` in ```run_kong.sh```allows **Kong** to use the host's network. Need to be adjusted based on the deployment.
- replace ```localhost``` with the **actual IP address or hostname** where Kong can reach your Express.js app.