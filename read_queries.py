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

            if token_list[3].strip() == 'ApiSongDAO':
                completeQuery = ' '.join(token_list[8:])
                queries.append([token_list[7], completeQuery.strip()])
        except:
            print("Line: " + str(line_count) + " - " + lineTest, end='')

workbook = xlsxwriter.Workbook('C:/Users/ricar/Desktop/Queries.xlsx')
worksheet = workbook.add_worksheet()
worksheet_index = 0

print("Queries: " + str(len(queries)))
print("Lines: " + str(line_count))

for file_index, time_and_query in enumerate(queries):
    time = time_and_query[0]
    query = time_and_query[1]

    # print(str(i) + ' - ' + time + ' ' + query)

    worksheet.write(int(worksheet_index), 0, int(file_index))
    worksheet.write(int(worksheet_index), 1, int(time))
    worksheet.write(int(worksheet_index), 2, query)

    if file_index != 0 and file_index % NUMBER_OF_LINES == 0:
        worksheet = workbook.add_worksheet()
        worksheet_index = 0
    else:
        worksheet_index += 1

workbook.close()
