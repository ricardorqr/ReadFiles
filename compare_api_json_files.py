from requests.auth import HTTPBasicAuth
import pysolr

uniqueSongs = set()
uniqueAlbums = set()

solrAlbum = pysolr.Solr('http://10.6.0.17:8983/solr/apiAlbum/', auth=HTTPBasicAuth('test', 'zapp123'))
solrAlbum.ping()

albums = solrAlbum.search(q="_query_:{!dismax mm='-34%' qs='1' qf='albumName' v='Piano Music Volume1' }", **{
        # 'indent': 'true',
        # 'sort': 'songId asc',
        'rows': 10000000,
        'wt': 'json',
    })

for line in albums:
    uniqueAlbums.add(line["songId"])

solrSong = pysolr.Solr('http://10.6.0.17:8983/solr/apiSong/', auth=HTTPBasicAuth('test', 'zapp123'))
solrSong.ping()

songs = solrSong.search(q="_query_:{!dismax mm='-34%' qs='1' qf='albumNames' v='Piano Music Volume1' }", **{
        # 'indent': 'true',
        # 'sort': 'id asc',
        'fl': 'id',
        'start': 0,
        'rows': 10000000,
        'wt': 'json',
    })

for line in songs:
    uniqueSongs.add(line["id"])

print('Album: ' + str(len(uniqueAlbums)))
print('Song: ' + str(len(uniqueSongs)))

uniqueSongs.symmetric_difference_update(uniqueAlbums)
print('Difference: ' + str(len(uniqueSongs)) + '\n')

print(uniqueSongs)
