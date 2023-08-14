from sys import argv

from functions import weather_functions
from openai_gateway import invoke_with_function, invoke_with_function_response
from weather_apis.factory import get_current_weather_from_provider
from constants import WEATHER_PROVIDER


def orchestrate(messages, functions):
    response = invoke_with_function(messages=messages,
                                    functions=functions,
                                    function_invoker=get_current_weather_from_provider(
                                        weather_provider=WEATHER_PROVIDER))
    function_name = response[0]
    function_request = response[1]
    function_response = response[2]
    return invoke_with_function_response(messages=messages,
                                         function_request=function_request,
                                         function_name=function_name,
                                         function_response=function_response)

def main():
    prompt = argv[1]
    messages = [
        {"role": "user", "content": prompt}
    ]
    response = orchestrate(messages, weather_functions)
    print(f"{prompt} \n {response}")


if __name__ == "__main__":
    main()
