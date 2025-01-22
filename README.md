<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thecodecamp</title>
</head>
<body>
    <h1>Thecodecamp</h1>
    <p>
        Thecodecamp is a coding learning platform that allows users to learn programming interactively. It features language compilers and editors for Python, Java, C++, and JavaScript, making coding accessible and efficient.
    </p>
    
    <h2>Features</h2>
    <ul>
        <li>Interactive compilers for Python, Java, C++, and JavaScript.</li>
        <li>Organized and user-friendly interface.</li>
        <li>Language-specific dedicated pages for focused learning.</li>
        <li>Suitable for beginners and intermediate coders.</li>
    </ul>
    
    <h2>Technologies Used</h2>
    <h3>Frontend</h3>
    <ul>
        <li>HTML</li>
        <li>CSS</li>
        <li>JavaScript</li>
    </ul>
    <h3>Backend</h3>
    <ul>
        <li>Django</li>
    </ul>
    <h3>Database</h3>
    <ul>
        <li>SQLite (default with Django)</li>
    </ul>
    
    <h2>Project Structure</h2>
    <pre>
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
    </pre>
    
    <h2>How to Run the Project</h2>
    <ol>
        <li>Clone the repository:</li>
        <pre>
            git clone https://github.com/King-Priyanshu/Thecodecamp.git
            cd Thecodecamp
        </pre>
        <li>Install dependencies:</li>
        <pre>
            pip install -r requirements.txt
        </pre>
        <li>Apply migrations:</li>
        <pre>
            python manage.py migrate
        </pre>
        <li>Run the development server:</li>
        <pre>
            python manage.py runserver
        </pre>
        <li>Open your browser and navigate to <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a>.</li>
    </ol>
    
    <h2>Contribution</h2>
    <p>
        Contributions are welcome! If you would like to improve or enhance this project, feel free to:
    </p>
    <ol>
        <li>Fork this repository.</li>
        <li>Create a feature branch.</li>
        <li>Submit a pull request.</li>
    </ol>
    
    <h2>License</h2>
    <p>
        This project is licensed under the <a href="https://opensource.org/licenses/MIT">MIT License</a>.
    </p>
    
    <h2>Contact</h2>
    <p>
        For queries or suggestions, reach out to:  
        <strong>Priyanshu</strong><br>
        GitHub: <a href="https://github.com/King-Priyanshu">King-Priyanshu</a>
    </p>
</body>
</html>