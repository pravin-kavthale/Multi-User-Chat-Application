# 🧠 Multi-User Chat Automation (Django + Channels + WebSockets + Redis + Gemini AI)

## 📖 Project Overview

**Multi-User Chat Automation** is a real-time Django-based chat application that allows multiple users to chat with an **automated AI bot** simultaneously.  
It uses **Django Channels**, **WebSockets**, **Redis**, and **Gemini AI** to provide instant message exchange and persistent chat history.

### ⚙️ Core Features
- Real-time bi-directional communication using **Django Channels**
- Automated responses powered by **Gemini AI**
- User-based chat persistence in **MySQL**
- REST API endpoint for fetching chat history
- Modern responsive UI using **TailwindCSS**
- Dual theme support (Dark + Light Card for Chat History)
- Fully containerized setup using **Docker**
- Scalable async handling via **Daphne** and **Redis**

---

## 🧩 Tech Stack

| Component | Technology Used |
|------------|----------------|
| Backend Framework | Django 4.x / Django Channels |
| Frontend | HTML, TailwindCSS, Vanilla JS |
| Database | MySQL |
| Real-Time Engine | Redis |
| ASGI Server | Daphne |
| AI Integration | Google Gemini API |
| Deployment | Docker + WSL2 |

---

## 🚀 Project Setup Guide

### 🛠 1. Clone the Repository
```bash
git clone https://github.com/pravin-kavthale/Multi-User-Chat-Application.git
cd Multi-User-Chat-Application
```
### 🐍 2. Create and Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate       # On Windows
# OR
source venv/bin/activate    # On Linux/Mac
```
### 📦 3. Install Dependencies
``` bash
pip install -r requirements.txt
```
### 🗝 4. Generate and Setup Gemini API Key
1. Visit Google AI Studio
2. Click on “Create API Key”
3. Copy your API key.
4. Create a .env file in your project root:
   ``` bash
        touch .env
   ```
5. Add the following inside .env:
   ``` bash
    DJANGO_SETTINGS_MODULE=UserChatAutomation.settings
    DEBUG=True
    GENAI_API_KEY=your_generated_key
    
    
    
    MYSQL_DB_NAME=your database name
    MYSQL_USER= mysql username
    MYSQL_PASSWORD=password
    MYSQL_HOST=localhost
    MYSQL_PORT=3306
   ```
### 🗃 5. MySQL Database Setup

Step 1: Open MySQL and Create Database
Step 2: Update settings.py
In your UserChatAutomation/settings.py, update the DATABASES configuration:
``` python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('MYSQL_DB_NAME'),
        'USER': os.getenv('MYSQL_USER'),
        'PASSWORD': os.getenv('MYSQL_PASSWORD'),
        'HOST': os.getenv('MYSQL_HOST'),
        'PORT': os.getenv('MYSQL_PORT'),
    }
}
```
Step 3: Apply Migrations
``` bash
python manage.py makemigrations
python manage.py migrate
```
step 4: Create super user
```bash
python manage.py createsuperuser
```
###🐧 6. Setup WSL and Redis (For Real-Time Messaging)
Step 1: Install WSL (Windows)
Open PowerShell as Administrator and run:
``` bash
wsl --install
```
Restart your system when prompted.
Step 2: Install Ubuntu (from Microsoft Store)
``` bash
wsl --install -d Ubuntu
```
Step 3: Update and Install Redis inside Ubuntu
``` bash
sudo apt update
sudo apt install redis-server
```
Step 4: Enable and Start Redis
``` bash
sudo service redis-server start
```
Step 5: Test Redis
``` bash
redis-cli ping
# Should return: PONG
```
### 🌐 7. Install Daphne (ASGI Server)
Daphne is required to handle WebSockets with Django Channels.
```bash
pip install daphne
```
#### Start Dhapne server
Run this command from the project root:
``` bash
Run this command from the project root:
```
### 💬 9. Testing Multi-User Real-Time Chat
Open two different browsers (e.g., Chrome and Firefox) or use incognito mode.
Log in with two different users.
Both users can chat in real time with the AI Bot.
Messages are stored in MySQL and fetched via the REST API for chat history.
### 🔑 10. Useful Commands Summary
| Task                     | Command                                                |
| ------------------------ | ------------------------------------------------------ |
| Start Redis              | `sudo service redis-server start`                      |
| Run Migrations           | `python manage.py migrate`                             |
| Create Superuser         | `python manage.py createsuperuser`                     |
| Start Django Dev Server  | `python manage.py runserver`                           |
| Start Daphne ASGI Server | `python -m daphne UserChatAutomation.asgi:application` |
| Collect Static Files     | `python manage.py collectstatic`                       |
### 11. Directory Structure
``` bash
multi-user-chat-automation/
│
├── Chats/
│   ├── consumers.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── models.py
│
├── Users/
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── UserChatAutomation/
│   ├── settings.py
│   ├── routing.py
│   ├── asgi.py
│   └── urls.py
│
├── templates/
│   ├── base/
│   ├── Chats/
│   └── Users/
│
├── .env
├── requirements.txt
└── README.md
```
### 🧠 12. Key Modules Used
channels — for asynchronous WebSocket communication
asgiref — ASGI interface support
daphne — production-ready ASGI server
redis — message broker for real-time communication
google-generativeai — for Gemini integration
rest_framework — for chat history API
mysqlclient — MySQL database connection
### 🎯 Final Notes
✅ Supports multi-user concurrent chat
✅ Fetches chat history dynamically using REST APIs
✅ Uses Redis for scalability and real-time message handling
✅ Gemini AI provides intelligent automated responses
✅ Tested with multiple browser sessions simultaneously


