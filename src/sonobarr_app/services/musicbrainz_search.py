import socket
import requests

orig_getaddrinfo = socket.getaddrinfo

def getaddrinfo_ipv4(host, port, family=0, type=0, proto=0, flags=0):
    return orig_getaddrinfo(host, port, socket.AF_INET, type, proto, flags)

socket.getaddrinfo = getaddrinfo_ipv4

def search_artist(name, max_artists):
    headers = {
        'User-Agent': 'Sonobaar/0.11.1 (https://github.com/Dodelidoo-Labs/sonobarr)'
    }
    url = "https://musicbrainz.org/ws/2/artist/"
    params = {
        'query': f'artist:{name}',
        'fmt': 'json',
        'limit': max_artists,
    }
    found = []
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            for artist in data.get('artists', []):
                found.append(Artist(artist.get('name'), artist.get('id')))
        else:
            print(response.status_code)
    except Exception as e:
        print(e)

    return found


class Artist:
    def __init__(self, name, artist_id):
        self.name = name
        self.artist_id = artist_id

    def get_id(self):
        return self.artist_id

    def get_name(self):
        return self.name
