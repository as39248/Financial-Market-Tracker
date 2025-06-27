from polygon import RESTClient

API_KEY = "lRZg8R5AflQqo34bbvXjjkwpRyu5sI6x"

def get_polygon_client():
    return RESTClient(api_key=API_KEY)
