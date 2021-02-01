# RESTAPI for User Profile.

# Project Setup
1. Install Virtualbox and Vagrant for your system

2. Navigate to the project loaction
```bash
# create and configure the virtual machine according to the Vagrantfile 
$ vargrant up
# connect to the virtual machine by SSH
$ vagrant ssh
```
3. Go to your project directory in vagrant server and Create a python virtual environment

```bash
# Navigate to project directory 
$ cd /vagrant
# create a python virtual environment at home
$ python -m venv ~/<venv_name>
```
4. Install the requirements

```bash
$ pip install -r requirements.txt

```