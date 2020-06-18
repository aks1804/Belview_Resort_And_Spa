# Belview Resort And Spa-Management-System 

### The software project contributors are required to install the dependencies as follows:
1. If you want to install system wide:
```shell
sudo pip install -r requirements.txt
```
2. If you want to use `virtualenv`:
* Create a virtual environment as (you can use any name of the environment as you like):
```shell
virtualenv -p python3 hms-virtual-env
```
* Then execute this:
```shell
source hms-virtual-env/bin/activate
```
* The install requirements as:
```shell
pip install -r requirements.txt
```
__Note:__ To deactivate `virtualenv`, execute 
```shell 
deactivate
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
* This will work if correctly set up.
