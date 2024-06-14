Use pip install -r requirments.txt

Migrate the model and start the app:

python manage.py makemigrations
python manage.py migrate 
python manage.py runserver

I used Insomia for testing the app manually 
below is the data for testing

Create the user: 

url : http://127.0.0.1:8000/account/
method : post
data : {
    "account_name": "David",
    "email_id": "david@test.com"
    }

Create the destinations:

destination 1:
url : http://127.0.0.1:8000/Destination/
method : post
data: {
    "destination_url": "https://reqres.in/api/users",
    "http_method": "post",
    "header": {
        "Content-Type": "application/json"
    },
    "account": 1
}

destination 2:

url : http://127.0.0.1:8000/Destination/
method: post
data : {
    "destination_url": "https://reqres.in/api/unknown",
    "http_method": "get",
    "header": {
        "Content-Type": "application/json"
    },
    "account": 1
}

Created two destinations for the user account 1

now sending the data using data_handler method:

url : http://127.0.0.1:8000/server/incoming_data/
method: post
data : {
    "name": "morpheus",
    "job": "leader"
}
add the CL-X-TOKEN in the header. Can get the token for the particular account 
using http://127.0.0.1:8000/account/1 method.

Using the above method the you can send the data to all the destination under the account

 
