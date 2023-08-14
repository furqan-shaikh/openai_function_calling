This repository contains my learnings with OpenAI's function calling features.

# What is function calling?
Developers can now describe functions to OpenAI models, and have the model intelligently choose to output a JSON object containing arguments to call those functions. This is a new way to more reliably connect GPT's capabilities with external tools and APIs.

# Repo details
This repository implements a simple use case for understanding function calling feature.
 - Enable OpenAI chat completion API to answer queries about current weather in a particular city

 # Running the application
 - Add your OpenAPI api key in `constants.py` under `API_KEY`
 - Run `python3 app.py <prompt>`.
    - For eg: `python3 app.py "What's the weather like in Bangalore today?"`
 - You should get a response from OpenAI with the weather details

# References
- https://platform.openai.com/docs/guides/gpt/function-calling