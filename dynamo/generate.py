import os
from pathlib import Path

def generate_object(directory, objectname, type, content=""):
    object = Path(directory, objectname)

    if object.exists():
        print("{}} already exists".format(objectname))
        return False
    
    print("Creating {}..".format(objectname))

    if type=="file":
        with open(object, "w") as f:
            f.write(content)
    elif type=="folder":
        object.mkdir()

    print("{} created successfully".format(objectname))

    return True


