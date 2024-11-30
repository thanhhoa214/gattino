from kitty.boss import Boss # type: ignore
import subprocess
import re
import json

def load_config() -> dict:
    config_path = '/Users/szappala/.config/kitty/gattino/gattino.config.json'
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        print(f"Config file not found at {config_path}")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error parsing config file: {e}")
        return {}

def main(args: list[str]) -> str:
    # https://www.asciiart.eu/animals/cats
    # http://patorjk.com/software/taag/#p=display&f=Calvin%20S&t=gattino
    print(""" _._     _,-'""`-._
(,-.`._,'(       |\\`-/|
    `-.-' \\ )-`( , o o)
          `-    \\`_`"'-

┌─┐┌─┐┌┬┐┌┬┐┬┌┐┌┌─┐
│ ┬├─┤ │  │ │││││ │
└─┘┴ ┴ ┴  ┴ ┴┘└┘└─┘

What do you want to do?
""")

    human_language_command = input('> ')
    prompt = f"""
You will be given an action in human language to be executed on a bash shell.
Please generate a single line bash command that executes the action.
ATTENTION: please fence the command using a code block. No explanation needed. Do not prefix the line with `$` or `#`.

Action to execute: {human_language_command}
"""
    write_file('/tmp/gattino_prompt.txt', prompt)
    config = load_config()
    model_name = config.get('model', 'codellama')
    model_output = run_command(f'/usr/local/bin/ollama run {model_name} "" --nowordwrap < /tmp/gattino_prompt.txt')
    command = extract_first_code_block(model_output)
    return command

def write_file(path, content):
    with open(path, 'w') as file:
        file.write(content + '\n')

def run_command(command):
    try:
        output = subprocess.check_output(command, shell=True)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error code {e.returncode}")
        return None

def extract_first_code_block(text):
    text = text.replace('```bash', '```')
    match = re.search(r"```(.*?)```", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""

def handle_result(args: list[str], answer: str, target_window_id: int, boss: Boss) -> None:
    w = boss.window_id_map.get(target_window_id)
    if w is not None:
        w.paste_text(answer)
