from kitty.boss import Boss # type: ignore
import re
import system_utils
import model
import config
import ui

def main(args: list[str]) -> str:
    # https://www.asciiart.eu/animals/cats
    ui.print_intro()

    human_language_command = ui.print_input_line()
    prompt = model.get_prompt(human_language_command)
    system_utils.write_file('/tmp/gattino_prompt.txt', prompt)
    config_data = config.load_config()
    model_name = config_data.get('model', 'codellama')
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
