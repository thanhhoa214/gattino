import subprocess


def write_file(path: str, content: str) -> None:
    """Write content to a file at the specified path."""
    with open(path, 'w') as file:
        file.write(content + '\n')


def run_command(command: str, input: str = None) -> str:
    process = subprocess.run(
        command.split(),
        input=input,
        capture_output=True,
        text=True
    )
    return process.stdout
