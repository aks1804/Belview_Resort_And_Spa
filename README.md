# Belview Resort And Spa-Management-System 

### Before running the program, make sure to have installed the dependencies in requirements.txt 
1. System wide installation:
```shell
sudo pip install -r requirements.txt
```
2. If you want to use `virtualenv`: (preferable)
* Create a virtual environment as:
```shell
virtualenv -p python3 env
```
or
```shell
virtualenv env
```
* Then execute this:
```shell
source env/bin/activate
```
* Then install requirements as:
```shell
pip3 install -r requirements.txt
```
### Finally:
* Go to Belview_Resort_And_Spa folder that you cloned before.
* Execute the followings: 
```shell
python3 manage.py migrate
```
Then,
```shell
python3 manage.py runserver
```
* This should work if correctly set up. Open the localhost address specified in a browser to access the application.

__Note:__ To deactivate `virtualenv`, execute 
```shell 
deactivate
```
