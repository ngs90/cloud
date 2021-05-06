# working directory
#mkdir working
#cd working 
#mkdir ngs-lib 
#cd ngs-lib 

# clone repository 
#git clone https://ngs90.visualstudio.com/ngs90/_git/ngs90


# Install python3.8z
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.8
sudo apt-get install python3-pip
sudo apt-get install python3.8-venv
sudo python3.8 -m pip install --upgrade pip setuptools wheel
sudo apt-get install build-essential libssl-dev libffi-dev python3.8-dev 

# Check it works and create virtualenvironment 
python3.8 --version
python3.8 -m venv env_veracity
source env_veracity/bin/activate
pip install wheel


# Setup odbc drivers 
sudo su
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
exit
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17
# optional: for bcp and sqlcmd
sudo ACCEPT_EULA=Y apt-get install -y mssql-tools
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
source ~/.bashrc
# optional: for unixODBC development headers
sudo apt-get install -y unixodbc-dev

# env variables
export AZUREML_DATA_ACCESS_USE_DEVICE_CODE=true
