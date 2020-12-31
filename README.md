## Prerequisites
* Docker
* ngrok

## Initial App Setup 
1. Clone repository
2. Set up env file:
    2.1. `VGS_USER` - forward proxy username credential
	2.2. `VGS_PWORD` - forward proxy password credential
	2.3. `VGS_TENANT` - VGS vault tenant ID
3. Run `docker_run.sh` (Script starts the Docker container in detached mode which allows you to use the same terminal session for future commands)
4. Execute the following:
```
docker-compose exec web python manage.py migrate
```
### Optional
In order to use the Django admin console and verify the data being stored in the database. You will need to create a user account.
1. Execute the following:
```
docker-compose exec web python manage.py createsuperuser
```
2. 	Enter username, email (optional), and password.


## VGS Integration
1. Start an HTTP tunnel using ngrok (free account, URL is random):
```
./ngrok http 8000
```
2. Note the forwarding URL provided by ngrok.
3. Open the Routes menu of the VGS Dashboard to configure the Inbound/Outbound routes.
    1. Import `config_inbound.yaml`
        1. Modify the Upstream Host field to use the ngrok URL.
    2. Import `config_outbound.yaml`
        1. The outbound proxy URL is constructed using the `.env` variables and is handled by the requests module in Django. 
4. Note the Inbound Route URL on the VGS dashboard. This is the URL you will use to reach the app.


