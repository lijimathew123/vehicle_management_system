# vehicle_management_system

Introduction:

The Vehicle Management System is a comprehensive software solution designed to streamline the management of vehicles and their associated data within an organization

Key Features:

User Authentication: Secure login system with different roles (super admin, admin, user) to control access and permissions.

Vehicle Database: A centralized repository to store detailed information about each vehicle, including vehicle number, type, model, and description.

Add and Edit Vehicles: Add new vehicles to the system or edit existing ones with updated information.

Delete Vehicles: Remove vehicles from the system when they are no longer in use or have been disposed of.

Role-Based Access: Different levels of access and permissions based on user roles, ensuring data security and integrity.

User-Friendly Interface: An intuitive and user-friendly interface that simplifies navigation and data entry.

## Instalation

1. clone repository
2. Change directory to the project folder:    cd your-project/
3. Create a virtual environment: python -m venv venv
4. Activate the virtual environment (Windows): venv\Scripts\activate  , (Linux): source venv/bin/activate
5. Install project dependencies: pip install -r requirements.txt
6. Apply database migrations: python manage.py migrate
7. Start the development server: python manage,py runserver
8.  Access the project in your web browser at `http://localhost:8000/`

SUPER ADMIN:
USER NAME: superuser
PASSWORD: 12345

ADMIN:
USER NAME: admin
PASSWORD: 1234

USER:
USER NAME: richu
PASSWORD: 1234

## New user can register and login.
Admin can login and view and edit vehicle details.
Super user can Login: Can add vehicle,edit vehicle details and delete vehicle details. 
                      Can add admin and remove admin from system.














