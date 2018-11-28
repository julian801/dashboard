
# Django Dashboard

## Goals

- create a dashboard that plots data and runs on AWS
- needs to be easy to install, so that we can create 10 machines if necessary

## Requirements:

- AWS account
- AWS key pair
- GitHub account
- data in a CSV file

## TODO:

### AWS Configuration
  - create an EC2 instance (AWS dashboard)
  - in the security group, open a port for HTTTP :80
  - add your host name to the ALLOWED_HOSTS in settings.py
  - start Django on the remote machine, so that it keeps running
  python manage.py runserver 0.0.0.0:80

###  Fabric:
  - copy installation script to EC2 and execute it

### Web Dev
  - write a HTML template (with D3!!!)

## Alternative Options
- Docker
- plotly
- create AWS image, and start multiple copies of that image
- monitoring (Sentry)


## DONE
- create an installation script
- write Django app locally
- create a git repository, push
- !! gitignore, so that AWS key pair doesnt get inside
- write a HTML template (with D3!!!)
- NGINX
