weather_functions = [
        {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. Bangalore, India"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"]
                    }
                }
            }
        }
    ]

email_functions = [
    {
            "name": "send_email",
            "description": "Send email to a recipient with a body",
            "parameters": {
                "type": "object",
                "properties": {
                    "to": {
                        "type": "string",
                        "description": "Recipient to send email to"
                    },
                    "body": {
                        "type": "string",
                        "description": "Email body containing details"
                    }
                }
            }
        }
]