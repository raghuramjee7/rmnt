# rmnt

CLI Scaffolding Tool for web applications with python

## Installation

## Project Structure
```
project/
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── utils.py
│   ├── models.py
│   └── exceptions.py
├── tests/
│   ├── __init__.py
│   ├── test_utils.py
├── .github/
│   └── workflows/
├── README.md
├── Dockerfile
├── LICENSE
├── .gitignore
└── .env
```

## Commands
1. `rmnt make <project-name>` - Initialize a new project
2. `rmnt --help` - Show help message
3. `rmnt --version` - Show version

## Features
1. Builds project structure for FastAPI and Flask projects
2. Installs common required dependencies - pytest, sqlalchemy
3. Creates a virtual environment
4. Initializes a git repository
