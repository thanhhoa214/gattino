from kitty.boss import Boss  # type: ignore
import src.system_utils as system_utils
import src.model as model
import src.config as config
import src.ui as ui
import src.parser as parser


def main(args: list[str]) -> str:
    config_data = config.load_config()
    ui.print_intro()
    human_language_command = ui.print_input_line()
    if not human_language_command:
        return 0
    prompt = model.get_prompt(human_language_command)
    model_name = config_data.get('model', 'codellama')

    model_output = system_utils.run_command(
        f'/usr/local/bin/ollama run {model_name} --nowordwrap',
        input=prompt)
    command = parser.extract_first_code_block(model_output)
    return command


def handle_result(args: list[str], answer: str, target_window_id: int, boss: Boss) -> None:
    window = boss.window_id_map.get(target_window_id)
    if window is not None:
        window.paste_text(answer)
