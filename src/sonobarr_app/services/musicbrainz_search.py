import requests

class Artist:
    def __init__(self, name, artist_id):
        self.name = name
        self.artist_id = artist_id

    def get_id(self):
        return self.artist_id

    def get_name(self):
        return self.name

def search_artist(name):
    headers = {
        'User-Agent': 'Sonobaar/0.11.1 (https://github.com/Dodelidoo-Labs/sonobarr)'
    }

    url = f"https://musicbrainz.org/ws/2/artist/"
    params = {
        'query': f'artist:{name}',
        'fmt': 'json'
    }

    response = requests.get(url, headers=headers, params=params)

    found = []
    if response.status_code == 200:
        data = response.json()
        print(data)
        for artist in data.get('artists', []):
            artist_name = artist.get('name')
            artist_id = artist.get('id')
            found.append(Artist(artist_name, artist_id))
    else:
        print(f"Error: {response.status_code}")

    return found