import subprocess
from typing import Optional

def write_file(path: str, content: str) -> None:
    """Write content to a file at the specified path."""
    with open(path, 'w') as file:
        file.write(content + '\n')
