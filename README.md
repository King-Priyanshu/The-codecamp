# Thecodecamp  

Thecodecamp is a coding learning platform that allows users to learn programming interactively. It features language compilers and editors for Python, Java, C++, and JavaScript, making coding accessible and efficient.  

---

## Features  
- Interactive compilers for Python, Java, C++, and JavaScript.  
- Organized and user-friendly interface.  
- Language-specific dedicated pages for focused learning.  
- Suitable for beginners and intermediate coders.  

---

## Technologies Used  
### Frontend  
- HTML  
- CSS  
- JavaScript  

### Backend  
- Django  

### Database  
- SQLite (default with Django)  

---

## Project Structure  
```plaintext
Thecodecamp/
├── manage.py
├── codecamp/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── compilers/
│   ├── __init__.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── python.html
│   │   ├── java.html
│   │   ├── cpp.html
│   │   └── javascript.html
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── script.js
│   │   └── images/
│   ├── views.py
│   └── urls.py
└── db.sqlite3