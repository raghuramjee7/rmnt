from utils import Content, Structure, Commands, PrePostCommands
from pathlib import Path
import os
import sys
sys.path.append('')
from dynamo import exec, generator


def start(project_name):

    scaffold(project_name)
    create_virtual_environment(project_name)
    initialise_git()
    
def create_virtual_environment(project_name):

    # install virtualenv
    exec.run_command(PrePostCommands.venv_install_pre, 
         Commands.venv_install, 
         PrePostCommands.venv_install_post)
    
    # create virtual environment
    exec.run_command(PrePostCommands.venv_create_pre,
         Commands.get_venv_command(project_name),
         PrePostCommands.venv_create_post)
    

def initialise_git():
    
    exec.run_command(PrePostCommands.git_pre,
         Commands.git,
         PrePostCommands.git_post)

def scaffold(project_name):
    current_dir = Path.cwd()

    # create project folder
    generator.generate_object(current_dir,
                              project_name,
                              "folder")

    # change directory to inside project
    os.chdir(str(current_dir) + "/" + project_name)
    current_dir = Path.cwd()

    # create subfolders
    create_list_folders(current_dir, Structure.folders)

    # create files
    create_list_files(current_dir, Structure.files)
    
    # add content to gitignore
    gitignore_path = str(current_dir) + '/' + '.gitignore'
    generator.update_file_content(gitignore_path, 
                              Content.get_gitignore_content(project_name))
    
    # move to github folder
    os.chdir(str(current_dir)+"/"+".github")
    # create workflow dir
    create_list_folders(Path.cwd(), Structure.github_folders)
    move_to_project_folder()

    # move to src folder
    os.chdir(str(current_dir)+"/"+"src")
    # create src files
    create_list_files(Path.cwd(), Structure.src_files)
    move_to_project_folder()

    # move to tests folder
    os.chdir(str(current_dir)+"/"+"tests")
    # create tests files
    create_list_files(Path.cwd(), Structure.test_files)
    move_to_project_folder()

def move_to_project_folder():
    # move to project folder
    current_directory = os.getcwd()
    parent_directory = os.path.dirname(current_directory)
    os.chdir(parent_directory)

def create_list_files(current_dir, file_list):
    for file in file_list:
        generator.generate_object(current_dir,
                                  file,
                                  "file")
        
def create_list_folders(current_dir, folder_list):
    for folder in folder_list:
        generator.generate_object(current_dir,
                              folder,
                              "folder")