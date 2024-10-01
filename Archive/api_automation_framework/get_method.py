import requests
import json
from .config import CONFIG

# Load config

base_uri = CONFIG['base_uri']

def get_response(resource):
    return requests.get(f"{base_uri}{resource}")

def get_status_code(resource):
    response = get_response(resource)
    return response.status_code

def get_response_body(resource):
    response = get_response(resource)
    return response
