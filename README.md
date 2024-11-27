# ✈️Airplane Boarding System✈️

## Project Overview

The Airplane Boarding System is a web based designed to manage and streamline flights,bookings, customer support, check in.

The website offers intuitive features for both employees and administrators, providing a streamlined solution for the tracking and management of airport data records. This system is designed to efficiently capture, store, and process airport management data through a comprehensive digital platform.

---

## 🔨 Built With:
- Python
- Django
- BootStrap css
- JavaScript
---

## 🙋‍♂️ Members:
- John Gabriel Cañal
- Allen Luis Mangoroban
- Daniel Stephen Delima
---

## 🚀 Table of Contents

- [Installation](#installation)
- [Features](#Features)
- [Usage](#usage)
- [Project Documentation/Resources](#Documentation)

---

## ⚙️ Installation

Follow these steps to set up the project on your local machine.

### Prerequisites

Make sure you have the following software installed:

- **Python 3.12.5 (you can check by running `python --version` or `python3 --version` in your terminal).
- **pip** (Python's package manager), usually installed alongside Python.
- **Django** (installed through pip).
- **MySQL Workbench**
  
If you don't have these installed, download Python from the [official website](https://www.python.org/downloads/), and `pip` comes with it.

Follow these steps to install the project:

1. Clone the repository:
    ```bash
    git clone https://github.com/username/repository-name.git](https://github.com/Daniel-Stephende5/IM2-Repository.git
    ```

2. Navigate into the project directory:
    ```bash
    cd NewDjango
    cd myblogsite
    ```
3. Create a virtual environment (optional but recommended):
   - For Windows
    ```bash
    python -m venv myenv
    myenv\Scripts\activate
    ```
   - For MacOS/Linux:
    ```bash
    python3 -m venv myenv
    source myenv/bin/activate
    ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    -If the project doesn't include a requirements.txt file, you can manually install Django and other dependencies as needed:
   ```bash
    pip install django
    ```

5. Check Python and Django versions: Verify that Python and Django are properly installed:
- Python
    ```bash
    python --version
    ```
- Django
   ```bash
    python -m django --version
    ```
6. Set up the database: Run the database migrations to create the necessary database tables:
   ```bash
   python manage.py migrate
   ```
7. Create a superuser (optional, but required to access the Django admin panel): To create an admin user, run:
   ```bash
   python manage.py createsuperuser
   ```
   - Follow the prompts to create a superuser with a username, email, and password.
   
8. Run the server: Once everything is set up, start the development server:
   ```bash
   python manage.py runserver
   ```
   - You can now visit the application in your browser at http://127.0.0.1:8000/. The Django admin panel can be accessed at http://127.0.0.1:8000/admin/, where you can log in using       the superuser credentials you just created.
   

---

## 💻 Usage

### Running the Application
After setting up the project and starting the server with `python manage.py runserver`, open the following in your web browser:

- **Home Page**: `http://127.0.0.1:8000/`
- **Admin Panel**: `http://127.0.0.1:8000/admin/` (Login using the superuser credentials you created)

---

## 📌 Features

- Signup
- Login
- Logout
- Check In
- Tracking Status
- View Flights
- Customer Support
- Booking

---


## 📝 Project Documentation/Resources

UI/UX DESIGN: [Figma Prototype](https://www.figma.com/design/0e5BfOdvtAELFK7U6jpDsq/Tripma---Flight-booking-web-app-(Community))

Gantt Chart: [View Timeline](https://docs.google.com/spreadsheets/d/1RtIbCRl-FmereZ7Tpj5udKsKCI9Hw0kPL5Dq4iP-QKE/edit?fbclid=IwY2xjawGzcIhleHRuA2FlbQIxMAABHej8IBSb2SVHL-hYlW08w_0YEcDj8Rrd9NJU6izkvqKTg6Lkvc0lIqbrag_aem_u4wN5XH3qej5vk7bbkQXuQ&gid=1313092142#gid=1313092142)

Entity Relationship Diagram (ERD): [View ERD](https://drive.google.com/file/d/1WhFnhzwXh_JXbuH18tJD9ri-ZCCkUzlR/view)

Functional Requirements Document (FRD): [Project Document](https://drive.google.com/file/d/1hxGc3FTgeE1cwjW-61ZUVKxXmaCkioIE/view?usp=sharing)

