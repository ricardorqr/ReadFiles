validURL = []
search_call = 0
lyric_call = 0
other_call = 0

with open('C:/Users/ricar/Desktop/localhost_access_log.2021-01-19.txt', 'r') as file:
    for line in file.readlines():
        token_list = line.split()
        for token in token_list:
            if token.startswith('/'):
                validURL.append(token)
                # print('http://localhost:8080/apiservice' + token)

print(len(validURL))
print(len(validURL[:500000]))

with open('C:/Users/ricar/Desktop/destination500k.csv', 'w') as file_dest:
    for line in validURL[:500000]:
        # print(line)

        if line.startswith('/search.do'):
            search_call += 1

        if line.startswith('/lyric.do'):
            lyric_call += 1

        if not line.startswith('/lyric.do') and not line.startswith('/search.do'):
            other_call += 1

        file_dest.write("%s\n" % line)

print('/search.do: ' + str(search_call))
print('/lyric.do: ' + str(lyric_call))
print('others: ' + str(other_call))
