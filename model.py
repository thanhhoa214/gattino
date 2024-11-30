def get_prompt(human_language_command: str) -> str:
    return f"""
You will be given an action in human language to be executed on a bash shell.
Please generate a single line bash command that executes the action.
ATTENTION: please fence the command using a code block. No explanation needed. Do not prefix the line with `$` or `#`.

Action to execute: {human_language_command}
"""
