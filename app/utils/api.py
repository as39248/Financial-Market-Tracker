from polygon import RESTClient
from dotenv import load_dotenv
import os

load_dotenv() 
API_KEY = os.getenv("API_KEY")

def get_polygon_client():
    return RESTClient(api_key=API_KEY)
