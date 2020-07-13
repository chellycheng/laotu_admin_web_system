# laotu_admin_web_system

 A web system to orgnize and visualize the database collected from Laotu Mini Apps for Laotu Admins

## Before running

### Requriment (for now, also can check requirements.txt):
 - asgiref==3.2.10
  - Django==3.0.8
  - pytz==2020.1
 - sqlparse==0.3.1
### Install instruction
If you dont have homebrew

    /user/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)
After having home brew

    brew install python3
Install the virtual enviroment

    pip3 install virtualenv
Install django

    pip install django
Install requirements

    pip install -r requirements.txt

### Local server
Run in terminal

    cd yourpath/laotu_admin_web_system
    source venv/bin/activate
    python admin_system/manage.py runserver
Open broswer, enter the following address

    http://127.0.0.1:8000
If you want to stop the local server `control +c` in your terminal
For quitting the virtual environment: 'deactivate' 

### Test
    source venv/bin/activate
    cd admin_system
    python manage.py test

or 
    python admin_system/manage.py test <app_name>
### Support features

 - Customers Message Orgnization
 - ...

### Helps 

    - url-patterns

### Reference
 - Front-end template: https://startbootstrap.com/themes/sb-admin-2/