import json 
import requests
import pandas as pd


def lambda_handler(event, context):
    print("Event: ", event)

    response = requests.get("https://google.com")
    print("Response: ", response)

    d = pd.DataFrame({
        "name": ["John", "Jane", "Doe"],
        "age": [28, 34, 45],
        "city": ["New York", "Los Angeles", "Chicago"]
    })

    print("DataFrame: ", d)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from Lambda!",
            "data": d.to_dict(orient='records')
        })
    }