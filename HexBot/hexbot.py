"""H=x Bot Request code"""
import requests
from pprint import pprint

URL = "https://api.noopschallenge.com/hexbot"

# req = requests.get(URL)
# result = req.json()
# print(result['colors'][0]['value'])  # prints the hex code, e.g. #7A5A28

# Additional parameters
# Hexbot supports: count, width, height, seed

def get_hexbot_colours(count, seed='', width=40, height=40):
    """
    Returns Hex code colours from Hexbot API
    :param count: 1-1000
    :param seed: "FF7F80"
    :param width: 1-1000
    :param height: 1-1000
    :return: {'colors': [{'coordinates': {'x':123, 'y':123}, 'value': '#ED5D9B'}, ...]}
    """
    # /?count=1000&width=500&height=500&seed=FF7F50,FFD700,FF8C00
    # seed = "FF7F50,FFD700,FF8C00"
    params = {'count': count, 'width': width, 'height': height}
    if seed:
        params['seed'] = seed

    req = requests.get(URL, params=params)  # the requests module will handle the parameter encoding
    result = req.json()
    # pprint(result) # prints a list of hexcodes
    return result

if __name__ == '__main__':
    colors = get_hexbot_colours(1000)
    pprint(colors)
