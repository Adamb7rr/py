import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def get_fun_fact(_):
    clear()  # clear everything on screen
    put_html('<h2 style="text-align:center">Fun Facts Generator</h2>')  # re-add title
    put_text("Fetching fun fact...")  # show loading

    url = 'https://uselessfacts.jsph.pl/random.json?language=en'
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        clear()
        put_html('<h2 style="text-align:center">Fun Facts Generator</h2>')
        put_text(data['text'])  # show fact
    except requests.exceptions.RequestException:
        clear()
        put_html('<h2 style="text-align:center">Fun Facts Generator</h2>')
        put_text("⚠ Could not fetch fun fact. Please try again.")

    # re-add the button
    put_buttons([dict(label='Click Me', value='outline-success')], onclick=get_fun_fact)

if __name__ == '__main__':
    put_html('<h2 style="text-align:center">Fun Facts Generator</h2>')
    put_buttons([dict(label='Click Me', value='outline-success')], onclick=get_fun_fact)
    hold()