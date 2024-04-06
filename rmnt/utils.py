from typing import Any
from enum import Enum, auto


class Content:
    
    gitignore = """
    .ipynb_checkpoints
    __pycache__/
    .vscode/
    .idea/
    .env
    .DS_Store
    __pypackages__/
    instance/
    .webassets-cache
    .pytest_cache/
    """

    dockerfile = ""

    env = ""

    readme = ""

class Structure:
    
    folders = ["src", "tests", ".github/workflows"]

    src_files = ["__init__.py", "app.py", "config.py", "models.py", "utils.py", "exceptions.py"]
    
    files = ["README.md", "Dockerfile", ".env", ".gitignore", "LICENSE"]



