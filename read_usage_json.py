import collections
import csv
import matplotlib.pyplot as plt
import pandas
import pysolr
from requests.auth import HTTPBasicAuth


class SongUsage:
    client_id = ''
    total_usage_count = 0
    usage_counts = []

    def __init__(self, client_id, total_usage_count, usage_counts):
        self.client_id = client_id
        self.total_usage_count = total_usage_count
        self.usage_counts = usage_counts

    def __str__(self):
        return 'client_id: ' + str(self.client_id) + ' usage_count: ' + str(self.total_usage_count)


class TestUsage:

    def print_dict(dictionary):
        for key, value in dictionary.items():
            sub_total = 0
            print(key)

            for sub_key, sub_frequency in value.items():
                print(sub_key, sub_frequency)
                sub_total += sub_frequency
            print(sub_total)

    def print_dict_tables(songs):
        for song_id, clients in songs.items():
            total = 0

            print('**Song: ' + str(song_id) + '**')
            print('|', 'client_id', '|', 'count', '|')
            print('| ------ | ------ |')

            for client_id, frequency in reversed(clients.items()):
                print('|', client_id, '|', frequency, '|')
                total += frequency

            print('|', '-', '|', 'Total:', total, '|\n')
            print('______')


if __name__ == '__main__':
    # csv_data = pandas.read_csv('C:/Users/ricar/Desktop/Top Songs.csv')
    csv_data = pandas.read_csv('C:/Users/ricar/Desktop/Trending Songs.csv')

    topSongs = []

    for index, row in csv_data.iterrows():
        topSongs.append(row[0])

    topSongs = topSongs[:10]

    solrAlbum = pysolr.Solr('http://63.247.64.138:8983/solr/searchUsageAnalytics/',
                            auth=HTTPBasicAuth('production', 'jTF4JPzVFDjFGmPhkfTNMK6W79vdFzat'))
    solrAlbum.ping()

    query = 'usage_date:[2021-07-23T00:00:00Z TO 2021-07-31T23:59:59.999Z] AND -client_id:721'

    usages = solrAlbum.search(
        q=query,
        **{
            'fl': ['id', 'catalog_song_id', 'usage_count'],
            'start': 0,
            'rows': 3000000,
            'wt': 'json',
        })

    songs = {}

    for line in usages:
        clients = {}
        json_id = line['id'].strip()
        client_id = json_id.split('_')[1]
        song_id = line['catalog_song_id']
        usage_count = line['usage_count']

        if song_id in topSongs:
            if song_id in songs:
                clients = songs.get(song_id)

                if client_id in clients:
                    songUsage_aux = clients.get(client_id)

                    usage_count_aux = songUsage_aux.total_usage_count
                    usage_count_aux += usage_count

                    songUsage_aux.total_usage_count = usage_count_aux
                    songUsage_aux.usage_counts.append(usage_count)

                    clients[client_id] = songUsage_aux
                    songs[song_id] = clients
                else:
                    songUsage = SongUsage(client_id, usage_count, [usage_count])
                    clients[client_id] = songUsage
                    songs[song_id] = clients
            else:
                songUsage = SongUsage(client_id, usage_count, [usage_count])
                clients[client_id] = songUsage
                songs[song_id] = clients

    print('Songs:', "{:,}".format(len(songs)))
    print(topSongs)
    # print(set(list(songs.keys())) == set(top500Songs))
    # print(collections.Counter(list(songs.keys())) == collections.Counter(top500Songs))

    all_clients = {}

    for song_id, clients in songs.items():
        for client_id, songUsage in clients.items():
            if client_id in all_clients:
                count = all_clients[client_id]
                count += songUsage.total_usage_count
                all_clients[client_id] = count
            else:
                all_clients[client_id] = songUsage.total_usage_count

    all_clients = {k: v for k, v in sorted(all_clients.items(), key=lambda item: item[1], reverse=True)}

    # header = ['client_id', 'usage_count']

    # with open('C:/Users/ricar/Desktop/Output Top Songs.csv', 'w', encoding='UTF8') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(header)
    #
    #     for client_id, usage_count in all_clients.items():
    #         writer.writerow([client_id, usage_count])

    # For one song
    for song_id, clients in songs.items():
        data = {}
        client_list = []
        total_usage_list = []

        for client_id, songUsage in clients.items():
            data[client_id] = songUsage.total_usage_count

        client_list = sorted(list(data.keys()))
        total_usage_list = list(data.values())

        fig = plt.figure(figsize=(10, 5))

        # Creating the bar plot
        plt.bar(client_list, total_usage_list, width=0.4)

        # Creating the labels on top each bar
        for i in range(len(total_usage_list)):
            plt.text(i, total_usage_list[i], total_usage_list[i], ha='center', bbox=dict(facecolor='white', alpha=.8))

        plt.xlabel("Clients")
        plt.ylabel("Total Usage")
        plt.title("Song " + str(song_id))
        # plt.savefig('C:/Users/ricar/Desktop/Top Song ' + str(song_id) + '.png', dpi=400)
        plt.savefig('C:/Users/ricar/Desktop/Trending Song ' + str(song_id) + '.png', dpi=400)
        plt.show()

    # all_clients = {}
    # for song_id, clients in songs.items():
    #     for client_id, songUsage in clients.items():
    #         if client_id in all_clients:
    #             count = all_clients[client_id]
    #             count += songUsage.total_usage_count
    #             all_clients[client_id] = count
    #         else:
    #             all_clients[client_id] = songUsage.total_usage_count
    #
    # print(all_clients)

    print()