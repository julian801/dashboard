#!/usr/bin/bash
#
# To be exectued on a RedHat EC2 instance with nothing
#

# install Python, Django, git
sudo yum -y install python36
sudo yum -y install python3-pip
sudo yum -y install git

# install the Python program
git clone https://github.com/krother/dashboard.git
cd dashboard
sudo pip3 install -r requirements.txt

# download CSV file
# curl http://somewhere.com/my.csv
