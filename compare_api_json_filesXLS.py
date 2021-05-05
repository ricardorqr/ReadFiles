import csv
import datetime

import pysolr
import xlsxwriter
from requests.auth import HTTPBasicAuth

queries = []

with open('C:/Users/ricar/Desktop/Queries.csv', 'r', encoding='utf8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        query = row["solrQuery"].split('_query_:')

        for album_query in query:
            if 'albumNames' in album_query:
                queries.append(album_query)

# print(*queries[:5000], sep='\n')

solrAlbum = pysolr.Solr('http://10.6.0.17:8983/solr/apiAlbum/', auth=HTTPBasicAuth('test', 'zapp123'))
print(solrAlbum.ping())

solrSong = pysolr.Solr('http://10.6.0.17:8983/solr/apiSong/', auth=HTTPBasicAuth('test', 'zapp123'))
print(solrSong.ping())

workbook = xlsxwriter.Workbook('C:/Users/ricar/Desktop/Queries OUTPUT.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0, 0, "Query")
worksheet.write(0, 1, "Songs")
worksheet.write(0, 2, "Songs Time Elapsed/ms")
worksheet.write(0, 3, "All Albums")
worksheet.write(0, 4, "Unique Albums")
worksheet.write(0, 5, "Albums Time Elapsed/ms")
worksheet.write(0, 6, "Difference")
worksheet.write(0, 7, "Difference IDs")

for file_index, query in enumerate(queries[:100]):
    uniqueSongs = set()
    uniqueAlbums = set()
    allAlbums = []

    # Songs
    startSong = datetime.datetime.now()
    try:
        songs = solrSong.search(q=query, **{
            # 'fl': 'id',
            'start': 0,
            'rows': 3000000,
            'wt': 'json',
        })
    except:
        print(query)
    endSong = datetime.datetime.now()

    for line in songs:
        uniqueSongs.add(line["id"])

    # Albums
    query = query.replace('albumNames', 'albumName')
    startAlbum = datetime.datetime.now()
    try:
        albums = solrAlbum.search(q=query, **{
            # 'fl': 'songId',
            'start': 0,
            'rows': 13000000,
            'wt': 'json',
        })
    except:
        print(query)
    endAlbum = datetime.datetime.now()

    for line in albums:
        album = line["songId"]
        uniqueAlbums.add(album)
        allAlbums.append(album)

    worksheet.write(int(file_index) + 1, 0, query)
    worksheet.write(int(file_index) + 1, 1, int(len(uniqueSongs)))
    worksheet.write(int(file_index) + 1, 2, (endSong - startSong).total_seconds() * 1000)
    worksheet.write(int(file_index) + 1, 3, int(len(allAlbums)))
    worksheet.write(int(file_index) + 1, 4, int(len(uniqueAlbums)))
    worksheet.write(int(file_index) + 1, 5, (endAlbum - startAlbum).total_seconds() * 1000)

    uniqueSongs.symmetric_difference_update(uniqueAlbums)
    worksheet.write(int(file_index) + 1, 6, int(len(uniqueSongs)))
    worksheet.write(int(file_index) + 1, 7, ', '.join(uniqueSongs))

workbook.close()
