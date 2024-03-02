# DB
sqlite for auth and mongo using djongo for shipment
# App
new app need to be included in the ```INSTALLED_APPS``` list in project's settings (```settings.py```).
- user authentication App: This app handles user authentication, including login, logout, password reset, and account activation functionalities.

- User profile App: The profile app manages user profiles and additional user-related information.

- permission and Roles App: This app manages user permissions and roles, including the central authority role responsible for approving new accounts.

- Email App: The email app handles email notifications, including account activation emails triggered manually by the central authority after account approval.


# App URLs
URL patterns for each app in project's main URL configuration file (```urls.py```) to map URL paths to **views** within each app.

# Account creation
- user will apply for account
- if another user with permission can approve then user will be sent an email
- now the email will contain the newly generated password
- user upon seeing the email with the activation link
- user will click it and link will take him to login

# to run
docker run -e PYTHONDONTWRITEBYTECODE=1 -e PYTHONUNBUFFERED=1 your_image_name

# for existing database schema
```sh
python manage.py inspectdb
```
it will give the code to populate models.py
