import requests
import json

from constants import API_KEY, API_ENDPOINT, OPENAI_MODEL


def _invoke_openai(data):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")


def invoke_with_function(messages,
                         functions,
                         function_invoker,
                         temperature=1):
    data = {
        "model": OPENAI_MODEL,
        "messages": messages,
        "functions": functions,
        "temperature": temperature,
    }
    result = _invoke_openai(data=data)
    message = result["choices"][0]["message"]
    if "function_call" not in message:
        raise Exception("Expected OpenAI to send a function call")
    function_name = message["function_call"]["name"]
    function_arguments = message["function_call"]["arguments"]
    json_arg = json.loads(function_arguments)
    # function_response = globals()[function_name](json_arg)
    function_response = _invoke_function(function_invoker, function_name, json_arg)
    return function_name, message, function_response


def _invoke_function(function_invoker, function_name, arguments):
    return function_invoker(arguments)


def invoke_with_function_response(messages, function_request, function_name, function_response, temperature=1):
    messages.append({
        "role": "function",
        "name": function_name,
        "content": str(function_response)
    })
    messages.append(function_request)
    data = {
        "model": OPENAI_MODEL,
        "messages": messages,
        "temperature": temperature,
    }
    result = _invoke_openai(data=data)
    return result["choices"][0]["message"]["content"]
