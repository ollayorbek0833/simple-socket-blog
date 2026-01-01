🧩 Simple Socket Blog (Python)
==============================

A minimal blog application built **without any web framework**, using only **raw Python sockets**, **HTTP**, and **SQLite**.

This project is designed for **educational purposes** to clearly demonstrate how web frameworks like **Flask** or **Django** work _under the hood_.

🚀 Key Features
---------------

*   🧠 Custom HTTP server built with socket
    
*   🗄️ SQLite database integration
    
*   ✍️ Create blog posts via HTML form
    
*   📃 Display all posts on the home page
    
*   🔗 Open each post on a separate page
    
*   ⚙️ No external libraries or frameworks
    
*   📦 Clean and minimal project structure
    

🖥️ Tech Stack
--------------

*   **Language:** Python 3
    
*   **Networking:** Python socket
    
*   **Database:** SQLite
    
*   **Frontend:** Plain HTML
    
*   **Protocol:** Raw HTTP (GET / POST)
    

📁 Project Structure
--------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   simple_project/   ├── db_init.py       # Database initialization script   ├── get_posts.py     # Database access layer   ├── server.py        # Socket server, routing, HTML rendering   ├── posts.db         # SQLite database (ignored by git)   └── README.md   `

⚙️ Installation & Usage
-----------------------

### 1️⃣ Initialize the Database (run once)

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python db_init.py   `

This will create the SQLite database and the posts table.

### 2️⃣ Start the Server

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python server.py   `

You should see:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Server running: http://127.0.0.1:8080   `

### 3️⃣ Open in Browser

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   http://127.0.0.1:8080   `

🌐 Available Routes
-------------------

MethodRouteDescriptionGET/Home page (posts list + form)POST/createCreate a new postGET/post?id=1View a single post

🧠 What This Project Teaches
----------------------------

This project helps understand:

*   How HTTP requests and responses work
    
*   How routing works internally
    
*   How HTML forms send POST data
    
*   How backend logic interacts with a database
    
*   What frameworks abstract away for developers
    

> Everything here is done manually to make the core concepts **clear and transparent**.

🔮 Possible Improvements
------------------------

*   ✏️ Edit and delete posts
    
*   📄 Pagination
    
*   🔐 Input validation & XSS protection
    
*   🧱 MVC folder structure
    
*   📡 REST API (/api/posts)
    
*   🚀 Migrate to Flask or FastAPI
    

📜 License
----------

This project is licensed under the **MIT License**.

🙌 Author
---------

Built for learning and experimentation with low-level backend concepts in Python.