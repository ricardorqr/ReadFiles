import json

file_lines = []
count = 0

# with open('C:/Users/ricar/Desktop/1835_CW201214780_FUL.V21', 'r', encoding="utf8") as file:
#     for line in file.readlines():
#         # print(line, end='')
#         file_lines.append(line)

with open('C:/Users/ricar/Desktop/1835_CW201214780_FUL.V21', 'r', encoding="utf8") as file:
    json_data = json.load(file)

# for json_line in read_api_json.py["tracks"]:
#     print(json_line["songId"])

# print('Lines: ' + "{:,}".format(len(file_lines)))

# with open('C:/Users/ricar/Desktop/NEW_FILE.V21', 'w', encoding="utf8") as file_dest:
#     for line in file_lines:
#         file_dest.write("%s" % line)
#         count += 1

# print('Lines: ' + "{:,}".format(count))

with open('C:/Users/ricar/Desktop/NEW_FILE.V21', 'w', encoding="utf8") as file_dest:
    file_dest.write("%s" % "{\n")
    file_dest.write("%s" % "\"specification\"" + ": " + json.dumps(json_data["specification"], indent=4) + ",\n")
    file_dest.write("%s" % "\"clientName\"" + ": " + json.dumps(json_data["clientName"], indent=4) + ",\n")
    file_dest.write("%s" % "\"password\"" + ": " + json.dumps(json_data["password"], indent=4) + ",\n")
    file_dest.write("%s" % "\"tracks\"" + ": [\n")
    file_dest.write("%s" % "{\n")
    for index in range(100):
        print(str(index))

        for line in json_data["tracks"]:
            file_dest.write("%s" % "{\n")
            file_dest.write("%s" % "\"songId\"" + ": " + json.dumps(line["songId"], indent=4) + ",\n")
            file_dest.write("%s" % "\"newRecord\"" + ": " + json.dumps(line["newRecord"], indent=4) + "\n")
            file_dest.write("%s" % "}\n")
    file_dest.write("%s" % "}\n")
    file_dest.write("%s" % "]\n")
    file_dest.write("%s" % "}")

# print(read_api_json.py.dumps(json_data["tracks"], indent=4))
