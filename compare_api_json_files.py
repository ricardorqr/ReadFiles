from requests.auth import HTTPBasicAuth
import pysolr
import csv
import time

queries = []

with open('C:/Users/ricar/Desktop/Queries.csv', 'r', encoding='utf8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        query = row["solrQuery"].split('_query_:')

        for album_query in query:
            if 'albumNames' in album_query:
                queries.append(album_query)

# print(*queries, sep='\n')

uniqueSongs = set()
uniqueAlbums = set()

solrAlbum = pysolr.Solr('http://10.6.0.17:8983/solr/apiAlbum/', auth=HTTPBasicAuth('test', 'zapp123'))
solrAlbum.ping()

solrSong = pysolr.Solr('http://10.6.0.17:8983/solr/apiSong/', auth=HTTPBasicAuth('test', 'zapp123'))
solrSong.ping()

with open('C:/Users/ricar/Desktop/Queries OUTPUT.csv', mode='w', encoding='utf8', newline='') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(['Query', 'Songs', 'Time Elapsed Songs/s', 'Albums', 'Time Elapsed Albums/s'])

    for query in queries:
        # Songs
        startSong = time.perf_counter()
        try:
            songs = solrSong.search(q=query, **{
                'fl': 'id',
                'start': 0,
                'rows': 13000000,
                'wt': 'json',
            })
        except:
            print(query)
        endSong = time.perf_counter()

        for line in songs:
            uniqueSongs.add(line["id"])

        # Albums
        query = query.replace('albumNames', 'albumName')
        startAlbum = time.perf_counter()
        try:
            albums = solrAlbum.search(q=query, **{
                'rows': 10000000,
                'wt': 'json',
            })
        except:
            print(query)
        endAlbum = time.perf_counter()

        for line in albums:
            uniqueAlbums.add(line["songId"])

        writer.writerow([query, len(uniqueSongs), f"{endSong - startSong:0.4f}", len(uniqueAlbums),
                         f"{(endAlbum - startAlbum):0.4f}"])
