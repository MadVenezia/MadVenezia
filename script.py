import requests
import random

# Function to fetch a random cat fact
def get_random_cat_fact():
    url = "https://cat-fact.herokuapp.com/facts"
    response = requests.get(url)
    data = response.json()
    if data and 'all' in data:
        return random.choice(data['all'])['text']
    return "Failed to fetch cat fact"

# Get a random cat fact
cat_fact = get_random_cat_fact()

# Format the fact
formatted_fact = f"**Cat Fact of the Day:** {cat_fact}"

# Display on README (or you can print it, save to a file, etc.)
print(formatted_fact)
