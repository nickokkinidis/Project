import requests
from bs4 import BeautifulSoup

def search_vgmdb(song_name):
    # URL to search for albums with the given song name
    search_url = f"https://vgmdb.net/search?q={song_name}=type="

    # Make the request to VGMdb
    response = requests.get(search_url)

    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the search results
        results = soup.find_all('div', class_='albumtitle')

        if results:
            print(f"\nFound {len(results)} results for '{song_name}':\n")
            for result in results:
                # Extract the album title
                album_title = result.text.strip()
                # Extract the link to the album page
                album_link = "https://vgmdb.net" + result.find('a')['href']
                print(f"Title: {album_title}")
                print(f"Link: {album_link}\n")
        else:
            print("No results found.")
    else:
        print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")

if __name__ == "__main__":
    # Ask the user for a song name
    song_name = input("Enter the song name you want to search for: ")
    search_vgmdb(song_name)