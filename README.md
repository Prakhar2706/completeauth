# CompleteAuth

CompleteAuth is a Django project that provides a complete authentication system with features like user registration, email OTP verification, and full admin access. This project can serve as a foundational structure for any web application that requires secure user authentication.

## Features

- **Create User**: New users can register and create accounts.
- **Register**: Users can register with an email and password.
- **Email OTP Verification**: Registration includes email verification via a one-time password (OTP) sent to the user's email.
- **Admin Access**: Admins have full access to manage users and other resources via the Django admin interface.
- **User Authentication**: Secure login and authentication system.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Prakhar2706/completeauth.git
   ```
2. Navigate to the project directory:
   
   ```bash
   cd completeauth
   ```
3. Create a virtual environment:
   
   ```bash
   python -m venv env
   ```
4. Activate the virtual environment:

   * On Windows:
     
   ```bash
   .\env\Scripts\activate
   ```

   *On macOS/Linux:
   
   ```bash
   source env/bin/activate
   ```
5. Install the dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```
6. Create migrations for your models:

   ```bash
   python manage.py makemigrations
   ```
7. Apply migrations:
   
   ```bash
   python manage.py migrate
   ```
8. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```
9. Start the development server:
   
   ```bash
   python manage.py runserver
   ```
10. Visit http://127.0.0.1:8000 in your browser to access the app.

11. For admin panel:
    
    ```bash
    http://127.0.0.1:8000/admin
    ```

## Requirements

    ```txt
    Django==5.0
    djangorestframework==3.14.0
    ```

## Usage
- Register: Users can sign up by providing an email and password.
- OTP Verification: An OTP will be sent to the user's email for verification.
- Admin Access: Admins can manage users and other functionalities through the Django admin panel.
- Authentication: The system ensures secure login and account verification.
