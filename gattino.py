from kitty.boss import Boss # type: ignore
import subprocess
import re
import json
import system_utils

def main(args: list[str]) -> str:
    # https://www.asciiart.eu/animals/cats
    print_intro()

    human_language_command = print_input_line()
    prompt = get_prompt(human_language_command)
    system_utils.write_file('/tmp/gattino_prompt.txt', prompt)
    config = load_config()
    model_name = config.get('model', 'codellama')
    model_output = system_utils.run_command(f'/usr/local/bin/ollama run {model_name} "" --nowordwrap < /tmp/gattino_prompt.txt')
    command = extract_first_code_block(model_output)
    return command

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

def get_prompt(human_language_command: str) -> str:
    return f"""
You will be given an action in human language to be executed on a bash shell.
Please generate a single line bash command that executes the action.
ATTENTION: please fence the command using a code block. No explanation needed. Do not prefix the line with `$` or `#`.

Action to execute: {human_language_command}
"""

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

def print_intro() -> None:
    # https://www.asciiart.eu/animals/cats
    # http://patorjk.com/software/taag/#p=display&f=Calvin%20S&t=gattino
    print(""" _._     _,-'""`-._
(,-.`._,'(       |\\`-/|
    `-.-' \\ )-`( , o o)
          `-    \\`_`"'-

┌─┐┌─┐┌┬┐┌┬┐┬┌┐┌┌─┐
│ ┬├─┤ │  │ │││││ │
└─┘┴ ┴ ┴  ┴ ┴┘└┘└─┘

""")

def print_input_line() -> str:
    print('What do you want to do?')
    return input('> ')
