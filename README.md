# Belview Resort And Spa-Management-System 

### Before running the program, make sure to have installed the dependencies 
1. System wide installation:
```shell
sudo pip install -r requirements.txt
```
2. If you want to use `virtualenv`: (preferable)
* Create a virtual environment as (you can use any name of the environment as you like):
```shell
virtualenv -p python3 env
```
* Then execute this:
```shell
source env/bin/activate
```
* The install requirements as:
```shell
pip install -r requirements.txt
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
* This should work if correctly set up. Go to the localhost address specified to access the application.

__Note:__ To deactivate `virtualenv`, execute 
```shell 
deactivate
```
