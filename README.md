# deepseek-engineer

If you are looking for the evolution that is an opinionated, managed service – check out deepseekengineer.app.

If you are looking for a well maintained hackable CLI for – check out aider.

deepseek-engineer lets you:
- Specify software in natural language
- Sit back and watch as an AI writes and executes the code
- Ask the AI to implement improvements

## Getting Started

### Install deepseek-engineer

For **development**:
- `git clone https://github.com/deepseek-engineer-org/deepseek-engineer.git`
- `cd deepseek-engineer`
- `poetry install`
- `poetry shell` to activate the virtual environment

We actively support Python 3.10 - 3.12.

### Setup API key

Choose **one** of:
- Export env variable (you can add this to .bashrc so that you don't have to do it each time you start the terminal)
    - `export DEEPSEEK_API_KEY=[your api key]`
- .env file:
    - Create a copy of `.env.template` named `.env`
    - Add your DEEPSEEK_API_KEY in .env
- Custom model:
    - See [docs](https://deepseek-engineer.readthedocs.io/en/latest/open_models.html), supports local model, azure, etc.

Check the [Windows README](./WINDOWS_README.md) for Windows usage.

**Other ways to run:**
- Use Docker ([instructions](docker/README.md))
- Do everything in your browser:
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/deepseek-engineer-org/deepseek-engineer/codespaces)

### Create new code (default usage)
- Create an empty folder for your project anywhere on your computer
- Create a file called `prompt` (no extension) inside your new folder and fill it with instructions
- Run `python main.py <project_dir>` with a relative path to your folder
  - For example: `python main.py projects/my-new-project` from the deepseek-engineer directory root with your new folder in `projects/`

### Improve existing code
- Locate a folder with code which you want to improve anywhere on your computer
- Create a file called `prompt` (no extension) inside your new folder and fill it with instructions for how you want to improve the code
- Run `deepseeke <project_dir> -i` with a relative path to your folder
  - For example: `deepseeke projects/my-old-project -i` from the deepseek-engineer directory root with your folder in `projects/`

## Terms
By running deepseek-engineer, you agree to our [terms](https://github.com/deepseek-engineer-org/deepseek-engineer/blob/main/TERMS_OF_USE.md).


## Features

### Pre Prompts
You can specify the "identity" of the AI agent by overriding the `preprompts` folder with your own version of the `preprompts`. You can do so via the `--use-custom-preprompts` argument.

Editing the `preprompts` is how you make the agent remember things between projects.

### Vision

By default, deepseek-engineer expects text input via a `prompt` file. It can also accept image inputs for vision-capable models. This can be useful for adding UX or architecture diagrams as additional context for DeepSeek Engineer. You can do this by specifying an image directory with the `—-image_directory` flag and setting a vision-capable model in the second CLI argument.

E.g. `deepseeke projects/example-vision gpt-4-vision-preview --prompt_file prompt/text --image_directory prompt/images -i`
