from ordered_set import OrderedSet
import json

sqlAlbums = []
jsonAlbums = []

with open('C:/Users/ricar/Desktop/JSON_FILE.txt', 'r', encoding="utf8") as file:
    json_data = json.load(file)

for doc in json_data["response"]["docs"]:
    line = json.dumps(doc["albumName"], sort_keys=True, ensure_ascii=False).strip()

    if line[0] == '"':
        line = line[0: 0:] + line[1:-1:]

    line = line.replace('\\"', '"')
    jsonAlbums.append(line)

jsonAlbums.sort()

with open('C:/Users/ricar/Desktop/SQL_FILE.txt', 'r', encoding="utf8") as file:
    for line in file:
        line = line.strip()

        if line[0] == '"':
            line = line[0: 0:] + line[1:-1:]

        line = line.strip().replace('""', '"')
        sqlAlbums.append(line)

sqlAlbums.sort()

intersection = (set(sqlAlbums)) ^ set(jsonAlbums)

print('SQL:' + str(len(sqlAlbums)))
print('JSON:' + str(len(jsonAlbums)))
print('Intersec:' + str(len(intersection)) + '\n')

intersection = OrderedSet(intersection)

for line_aux in intersection:
    print(line_aux)
