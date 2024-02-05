# aws cli
**in aws config**
AWS Access Key ID [None]: from the ```credentials```
AWS Secret Access Key [None]: account of walkersarf

## finding the instance
aws rds describe-db-instances   --query "*[].[DBInstanceIdentifier,Endpoint.Address,Endpoint.Port,MasterUsername]"

## installed pgadmin
```sh
# Install the public key for the repository (if not done previously):
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg

# Create the repository configuration file:
sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'


# Install for both desktop and web modes:
sudo apt install pgadmin4
```


# ohh thisss
## Error – FATAL: database name does not exist
using the default database name **postgres** for the --dbname option.
## connect to PostgreSQL server: FATAL: no pg_hba.conf entry for host
listen_addresses = '*'
<br>So maybe allow all inbound traffic<br>
**nop it's because of rds.ssl set to 1**
- So new param and det to 0
- then select the new parameter gorup in DB