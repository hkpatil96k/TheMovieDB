import urllib3
import json
def search_movie(title):
    if len(title) < 1 or title=='quit':
        print("Goodbye now…")
        return None
try:
    url = 'https//api.themoviedb.org' + urllib3.parse.urlencode({'t': 'title'})+'f357fae24e8a04b6a01a129f4bcf097f'
    print(f'Retrieving the data of "{title}" now… ')
    uh = urllib3.request.urlopen(url)
    data = uh.read()
    json_data=json.loads(data)
    if json_data['Response']=='True':
        print (json_data)
except urllib3.error.URLError as e:
    print(f"ERROR: {e.reason}")
