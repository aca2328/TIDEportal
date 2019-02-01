# tideportal
Fetch Threat Intelligence data from Infoblox TIDE and convert them to html
this script use https://pandas.pydata.org to convert the json output from Infoblox TIDE api endpoint into a browser friendly HTML file. 
The rest call url can be modied outside the script, while the token key must be inserted into the script line 20/21.

##### Prerequisites
sudo apt install python3-pip (ubuntu)
install python 3.6 ( mac )
pip3 install jinja2
pip3 install pandas.io.json
pip3 install requests
pip3 install json

Tested with ubuntu 14.04 LTS