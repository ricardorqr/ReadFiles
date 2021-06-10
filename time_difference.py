import datetime

# Old Code
string_begin1 = '2021-06-09 18:57:36.606'
date_time_begin1 = datetime.datetime.strptime(string_begin1, '%Y-%m-%d %H:%M:%S.%f')

string_end1 = '2021-06-09 19:38:32.492'
date_time_end1 = datetime.datetime.strptime(string_end1, '%Y-%m-%d %H:%M:%S.%f')

print('Old code:', date_time_end1 - date_time_begin1)

# New Code
string_begin2 = '2021-06-09 19:53:25.924'
date_time_begin2 = datetime.datetime.strptime(string_begin2, '%Y-%m-%d %H:%M:%S.%f')

string_end2 = '2021-06-09 20:31:02.842'
date_time_end2 = datetime.datetime.strptime(string_end2, '%Y-%m-%d %H:%M:%S.%f')

print('New code:', date_time_end2 - date_time_begin2)
