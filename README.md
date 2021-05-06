# Setup python 3.8 on virtual machine and create virtual environment
Installation of pure Python 3.8:
* https://linuxize.com/post/how-to-install-python-3-8-on-ubuntu-18-04/
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.8
sudo apt-get install python3-pip
sudo apt-get install python3.8-venv
python3.8 -m pip install --upgrade pip setuptools wheel
sudo apt-get install build-essential libssl-dev libffi-dev python3.8-dev

Verify it works by running:
* python3.8 --version
Setup virtual environment:
* python3.8 -m venv env_veracity
* source env_cable_cutters/bin/activate
* pip install wheel


# Setup odbc drivers 
Install windows SQL odbc drivers:
* https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15#ubuntu17



# Handle persmissions on .pem file 
* https://gist.github.com/jaskiratr/cfacb332bfdff2f63f535db7efb6df93 
Alter to chmod 400 by runing these commands on Windows: 

Source: https://stackoverflow.com/a/43317244
$path = "C:\working\azure\keys\vm-ngs-playground-dev_key.pem"
icacls.exe $path /reset
icacls.exe $path /GRANT:R "$($env:USERNAME):(R)"
icacls.exe $path /inheritance:r

# SSH into virtual machine 
* ssh -i C:\working\keys\ssh\XXX.pem azureuser@20.67.241.61 

# (optional to be able to connect with X2Go - currently NOT WORKING yet):
* https://docs.microsoft.com/en-us/azure/virtual-machines/linux/use-remote-desktop 
Install xfc4 and the xrdp 
* sudo apt-get update
* sudo apt-get -y install xfce4
* sudo apt-get -y install xrdp
* sudo systemctl enable xrdp

# active and restart
* echo xfce4-session >~/.xsession
* sudo service xrdp restart 


# Visual code connection 
* (Ubuntu machine) ssh -i "C:\working\keys\ssh\XXX.pem" azureuser@IPIPIPIP
* (data science, NOT WORKING) ssh -i "C:\working\keys\ssh\XXX.pem" azureuser@IPIPIPIP

# Visual code Python debugging 
Follow guide from here: https://marketplace.visualstudio.com/items?itemName=ms-python.python 
* Ctrl+Shift+P 
	* Python: Select Interpreter	Switch between Python interpreters, versions, and environments.
	* Python: Run Python File in Terminal	Runs the active Python file in the VS Code terminal. You can also run a Python file by right-clicking on the file and selecting Run Python File in Terminal.

# Installation af docker på basis Ubuntu18.04 
Follow setup from here:
* https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04


# Install azure CLI
Follow instructions here: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt
* curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash 


# Environmental variables 
* AZUREML_DATA_ACCESS_USE_DEVICE_CODE=true


# Give service principal access to storage account 
??? (Data engineering der skal gøres dette)