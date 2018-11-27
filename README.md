
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

### AWS CONTROL PANEL (or boto3):
    create an EC2 instance (AWS dashboard)
    open a port for HTTTP :80

###  Fabric:
  - copy installation script to EC2 and execute it
  - start Django on the remote machine, so that it keeps running
    python manage.py runserver

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
