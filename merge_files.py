validURL = []
search_call = 0
lyric_call = 0
other_call = 0
robot_list = set()
new_robot_list = set()

with open('C:/Users/ricar/Desktop/robotList_09_01_2018.csv', 'r') as file:
    for line in file.readlines():
        new_robot_list.add(line)

with open('C:/Users/ricar/Desktop/robotList', 'r') as file:
    for line in file.readlines():
        robot_list.add(line)

print(len(new_robot_list))
print(len(robot_list))


# with open('C:/Users/ricar/Desktop/destination500k.csv', 'w') as file_dest:
#     for line in validURL[:500000]:
#         # print(line)
#
#         if line.startswith('/search.do'):
#             search_call += 1
#
#         if line.startswith('/lyric.do'):
#             lyric_call += 1
#
#         if not line.startswith('/lyric.do') and not line.startswith('/search.do'):
#             other_call += 1
#
#         file_dest.write("%s\n" % line)
#
# print('/search.do: ' + str(search_call))
# print('/lyric.do: ' + str(lyric_call))
# print('others: ' + str(other_call))
