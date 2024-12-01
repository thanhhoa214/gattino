import subprocess
import sys
import time
from typing import List


class Spinner:
    def __init__(self):
        self.frames: List[str] = ['⢄', '⢂', '⢁',
                                  '⡁', '⡈', '⡐', '⡠']
        self.index: int = 0

    def next_frame(self) -> str:
        frame = self.frames[self.index]
        self.index = (self.index + 1) % len(self.frames)
        return frame

    def show(self, process: subprocess.Popen) -> None:
        while process.poll() is None:  # While process is still running
            print(f"\r{self.next_frame()}", end='', file=sys.stderr)
            time.sleep(0.1)
        print("\r", end='', file=sys.stderr)  # Clear the spinner


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


def show_spinner(process: subprocess.Popen) -> None:
    spinner = Spinner()
    spinner.show(process)
