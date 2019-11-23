# Printing_Website_Project
It's a Printing website project developed using Django framework as a backend.
I have implemented whole project's UI using CSS,HTML and little Javascript.
User can register and login to the site, they can order different items like visiting cards, banners ets.
Once the order is placed from UI, a mail conataining order information will be sent automatically to the registered mail id.
We have a admin dashboard where admin/superuser can view the user/profile and the placed orders.
He has all the access and he can delete, modify and add the user.
Here database setup is done for MySql.
We can configure mail, database in settings.py

Steps:
Pip install django
python manage.py createsuperuser (to create admin user)
python manage.py makemigrations(database migrations)
python manage.py migrate(migrate/sync)

To run the code in local:
Python manage.py runserver.

