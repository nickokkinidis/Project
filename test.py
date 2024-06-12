import requests
from bs4 import BeautifulSoup

def search_vgmdb(query):
    search_url = f"https://vgmdb.net/search?q={query.replace(' ', '+')}"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the search result links
    results = soup.find_all('div', class_='albumtitle')
    if not results:
        return None

    search_results = []
    for result in results:
        link = result.find('a')
        if link:
            album_url = "https://vgmdb.net" + link['href']
            search_results.append(album_url)
    
    return search_results

def get_album_info(album_url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    album_response = requests.get(album_url, headers=headers)
    if album_response.status_code != 200:
        return None

    album_soup = BeautifulSoup(album_response.text, 'html.parser')

    # Extract album title
    album_title = album_soup.find('h1', class_='albumtitle').text.strip()
    
    # Find and parse tracklist table
    tracklist = []
    tracklist_table = album_soup.find('table', class_='tracklist')
    if tracklist_table:
        for row in tracklist_table.find_all('tr'):
            columns = row.find_all('td')
            if len(columns) > 1:
                track_title = columns[1].text.strip()
                tracklist.append(track_title)

    # Find and parse artist and composer information
    composer = 'Unknown'
    artist = 'Unknown'
    info_sections = album_soup.find_all('div', class_='album_infobit')
    for section in info_sections:
        header = section.find('b')
        if header:
            header_text = header.text.strip().lower()
            if 'composer' in header_text:
                composer = section.text.replace('Composer:', '').strip()
            elif 'performer' in header_text or 'artist' in header_text:
                artist = section.text.replace('Performer:', '').replace('Artist:', '').strip()
    
    return {
        'album': album_title,
        'composer': composer,
        'artist': artist,
        'tracks': tracklist
    }

def main():
    while True:
        print("Search VGMdb by:")
        print("1. Title")
        print("2. Artist")
        print("3. Composer")
        search_choice = input("Enter your choice (1/2/3): ")

        if search_choice == '1':
            search_type = "title"
        elif search_choice == '2':
            search_type = "artist"
        elif search_choice == '3':
            search_type = "composer"
        else:
            print("Invalid choice. Please try again.")
            continue

        query = input(f"Enter the {search_type} to search: ")

        search_results = search_vgmdb(query)
        if not search_results:
            print(f"No results found for {search_type}: {query}")
            continue

        print(f"Found {len(search_results)} results.")
        for album_url in search_results:
            info = get_album_info(album_url)
            if info:
                print(f"\nAlbum: {info['album']}")
                print(f"Composer: {info['composer']}")
                print(f"Artist: {info['artist']}")
                if search_type in ['artist', 'composer']:
                    print("Tracks:")
                    for i, track in enumerate(info['tracks']):
                        print(f"{i + 1}. {track}")

                    track_choice = input("Enter the number of the track you want details for (or press Enter to skip): ")
                    if track_choice.isdigit():
                        track_index = int(track_choice) - 1
                        if 0 <= track_index < len(info['tracks']):
                            print(f"\nSelected Track: {info['tracks'][track_index]}")
                            print(f"Album: {info['album']}")
                            print(f"Composer: {info['composer']}")
                            print(f"Artist: {info['artist']}")
                        else:
                            print("Invalid track number.")
            else:
                print(f"Failed to retrieve info for album: {album_url}")

        search_again = input("Do you want to search again? (y/n): ")
        if search_again.lower() != 'y':
            break

if __name__ == "__main__":
    main()
