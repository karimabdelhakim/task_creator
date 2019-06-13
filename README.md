# task_creator
app for creating tasks and sending an emial with its details to the user who created it  
# install
create account on https://www.mailjet.com/ and get credentials to send emails  
create python 3 virtualenv    
pip install requirements.txt   
add a .env file and set those environment variables  
SECRET_KEY
EMAIL_HOST_USER  
EMAIL_HOST_PASSWORD  
FROM_EMAIL  
optional: add local.py file in settings folder for local environment  
python manage.py makemigrations  
python manage.py migrate  
python manage.py runserver  
go to http://127.0.0.1:8000
