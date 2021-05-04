import xlsxwriter

NUMBER_OF_LINES = 100000
queries = []
line_count = 0

with open('C:/Users/ricar/Desktop/spring-boot-logger.log', 'r', encoding="utf8") as file:
    for lineTest in file.readlines():
        try:
            if lineTest != "\n":
                line_count += 1

            token_list = lineTest.split()

            if token_list[6].strip() == 'TestLocalRico':
                # print((token_list[7].split('##')[1][32:]))    # URL
                # print(token_list[9][13:])             # PARAMETERS
                # print(token_list[10].split('##')[1])  # SONG_IDS
                # print(token_list[11].split('##')[1])  # TIME_ELAPSED

                completeQuery = ' '.join(token_list[12:]).split('##')[1]
                # print(completeQuery)                          # QUERY

                queries.append([
                    str(token_list[7].split('##')[1][32:]) + '?' +  # URL
                    str(token_list[9][13:]),            # PARAMETERS
                    token_list[10].split('##')[1],      # SONG_IDS
                    token_list[11].split('##')[1],      # TIME_ELAPSED
                    completeQuery.strip()])             # QUERY
        except:
            print("Line: " + str(line_count) + " - " + lineTest, end='')

workbook = xlsxwriter.Workbook('C:/Users/ricar/Desktop/Complete Queries.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0, 0, "index")
worksheet.write(0, 1, "ids")
worksheet.write(0, 2, "url")
worksheet.write(0, 3, "time_elapsed")
worksheet.write(0, 4, "query")

# worksheet_index = 0

print("Queries: " + str(len(queries)))
print("Lines: " + str(line_count))

for file_index, time_and_query in enumerate(queries):
    url = time_and_query[0]
    song_ids = time_and_query[1]
    time_elapsed = time_and_query[2]
    query = time_and_query[3]

    worksheet.write(int(file_index) + 1, 0, int(file_index))
    worksheet.write(int(file_index) + 1, 1, song_ids)
    worksheet.write(int(file_index) + 1, 2, url)
    worksheet.write(int(file_index) + 1, 3, int(time_elapsed))
    worksheet.write(int(file_index) + 1, 4, query)

    # if file_index != 0 and file_index % NUMBER_OF_LINES == 0:
    #     worksheet = workbook.add_worksheet()
    #     worksheet_index = 0
    # else:
    #     worksheet_index += 1

workbook.close()
