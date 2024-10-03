import requests
import configparser

def fetch_data():
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    # Use the URL from the config file, or fall back to the predefined URL
    url = config['DEFAULT'].get('api_url', 'https://jsonplaceholder.typicode.com/posts/1')
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Title: {data['title']}")
        print(f"Body: {data['body']}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

if __name__ == "__main__":
    try:
        fetch_data()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        input("Press Enter to continue...")