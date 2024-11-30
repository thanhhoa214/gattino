import subprocess

def write_file(path: str, content: str) -> None:
    """Write content to a file at the specified path."""
    with open(path, 'w') as file:
        file.write(content + '\n')

def run_command(command: str) -> str | None:
    try:
        output = subprocess.check_output(command, shell=True)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error code {e.returncode}")
        return None
