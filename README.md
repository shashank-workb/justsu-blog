# JUTSU-BLOG: Project to practice and showcase Dev skills
This is an attempt to design, develop and deploy a production level app, with an intent to practice and showcase dev skills.

This is a generic blog app, name being used is domain name I have kept for personal future endeavours.

[conceptguitar.in](https://conceptguitar.in/)


# 🔗 Links
Hi, I'm Shashank Mishra! 👋

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://conceptguitar.in/about/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mshashank-work/)

## FEATURES for Users

- Account registration/Login/Logout
- CRUD Blog posts
- Check weather for user location/Automatic and Manual update
- Profile picture
- Change user info
- Check other user's Profile
- View other user's posts
- Change Password
- Reset forgotten password with email link


# Tech Stack

**Client:** HTML CSS

**Server:** Django

**DB:** PostgreSQL

**Deployment:** AWS(EC2 Ubuntu 20.04)/Nginx/Gunicorn

# Technical Features

**Frontend:** Plain old HTML/CSS, Crispy Template for forms

**Backend:**

- Django 3.2
- Both Functional views and CBVs present in codebase
- Custom CBVs(overriden)
- 3rd Party API Integration to get weather updates, handling of errors (https://openweathermap.org/current)
- Automatic location detection via IP (http://ipinfo.io/json)
- PostgreSQL as DB
- Async Tasks of updating weather(Celery Worker) and updating weather of location objects periodically(Celery beat) with message queue(redis)
- Mixins(and decorators) to check logged in and permissions and redirect accordingly
- Pagination
- Password protection with extra hashing algos(Bcrypt)
- Email server to send password reset links
- Image upload with pillow and size conversions
- Minimal UT coverage(Please see future plans)
- Seperation of local(dev) and prod settings, use of .env for prod
- Dockerized the local dev setup

**Deployment**
- AWS EC2 micro instance, Ubuntu 20.04
- Nginx as web server(reverse proxy server) to provide static content
- SSL certification with Let's Encrypt and domain name in GoDaddy
- Gunicorn as app server(proxy server) for Django app to compute dynamic requests
- Celery worker and beat with redis as broker
- All the above services being run as systemd services
- PostgreSQL installation
- All the above services are currently installed in the Ubuntu server itself

**Architecture**
There are two apps involved in the project, along with 3 tables in the DB


![Blank diagram](https://user-images.githubusercontent.com/64981954/143776306-2557306c-1f4c-42a6-9d20-ed2f236cd99d.jpeg)

![ERD with colored entities (UML notation)](https://user-images.githubusercontent.com/64981954/143776314-0fa2fe7c-642e-4f58-ac4a-b2f264a1fa68.jpeg)



# Feedback

If you have any feedback, please reach out to me at
- shashank.workb@gmail.com
- https://www.linkedin.com/in/mshashank-work/
