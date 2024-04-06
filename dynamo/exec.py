import subprocess

def run_command(premessage, command, postmessage):
    # run the command
    print(premessage)
    result = subprocess.run(command, 
                            shell=True, 
                            capture_output=True, 
                            text=True)   
    if result.returncode == 0:
        print(result.stdout)
        print(postmessage)
        return True
    else:
        print(result.stderr)
        print("Failed to execute command. Exiting...")
        return False


