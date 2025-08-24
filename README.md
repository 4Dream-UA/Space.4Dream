# Space 4Dream

Space 4Dream is a modern business project management system that brings everything you need into one place — from task planning to document storage. Built for teams that value clarity, speed, and structure at every stage of their work.


<strong>Navigation:<br>
<a href="https://discord.gg/6MbYCn2MpH">4Dream Community</a>
* [Demo](#demo)
* [Technologies](#technologies)
* [Features](#features)
* [Installation](#installation)
</strong>

## Demo
* Website: https://space-4dream.onrender.com/
* Test Users:
  * username: a.admin; password: PasswordADM; 
  * username: g.stealth; password: PositionCTO;
  * username: g.morgan; password: PositionSDO;
  * <i>(See more about users in config/public_config.py)</i>

## Technologies
<strong>Main technologies in project are:</strong>
* Backend: Python; Django
* Frontend: HTML5; CSS; Bootstrap5; Tailwind CSS
* Data Base: SQLite; PostgresSQL

## Features
* <strong>Project Catalog: </strong> Easily organize and manage multiple projects. Each project is created as a separate workspace with its own settings and modules.
* <strong>Document Hub: </strong> Every project includes a dedicated document center. Keep all your files and documentation well-organized, centralized, and accessible to your team.
* <strong>Document Hub: </strong> A built-in task management system featuring (Task creation, assignment, and tracking; Support for statuses and deadlines; Comments and change history)
* <strong>Team & Role Management: </strong> Flexible user assignment by roles and teams; Hierarchical company structure: departments, positions, and subunits; Granular access control at the project and task levels
* <strong>Modern Frontend: </strong> Fast and responsive interface; Adaptive design for all devices; Seamless user interaction and feedback

## Installation

<i>!! Main requirement is Python3+</i>

1.  Clone the repository: 
    ```bash
    git clone https://github.com/4Dream-UA/Space.4Dream.git
    ```
2.  Create a virtual environment:
    ```bash
    python -m venv venv
    ```
3. Activate the virtual environment:
    * Windows:
    ```bash
    venv\Scripts\activate
    ```
    * macOS/Linux: 
    ```bash
    source venv/bin/activate
    ```
4.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Create .env file
6. Set SECRET_KEY in .env file
7. Run migrations:
    ```bash
    python manage.py migrate
    ```
8. Initialization: 
    ```bash
    python manage.py shell
    ```
    ```py
    from teamspace.models import Worker, Position, TaskType
    from config.public_config import init_requirements, init_users
    
    init_requirements(position_model=Position, taskType_model=TaskType)
    # >>> Get True return
    
    init_users(worker_model=Worker, position_model=Position)
    # >>> Get True return
    
    # You can find all accounts data in config/public_config.py
    ```
9. Start the server: 
    ```bash
    python manage.py runserver 8000
   // http://127.0.0.1:8000/
   ```

