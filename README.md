# Gattino 🐱

A kitty terminal extension that translates human language commands into bash commands using ollama.

![Demo](assets/demo.gif)

## Installation

### Requirements
- [ollama](https://ollama.ai/)

## Configuration

The configuration is located in `~/.config/kitty/gattino/gattino.config.json` and the following options are available:

* `model`: The ollama model to use for command translation (default: "codellama")
* `ollama_path`: Path to the ollama executable (default: "/usr/local/bin/ollama")
