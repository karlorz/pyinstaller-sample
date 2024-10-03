import requests

def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"
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