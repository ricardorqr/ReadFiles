import datetime

# Old Code
string_begin1 = '2021-06-10 18:52:06.881'
date_time_begin1 = datetime.datetime.strptime(string_begin1, '%Y-%m-%d %H:%M:%S.%f')

string_end1 = '2021-06-10 19:32:24.996'
date_time_end1 = datetime.datetime.strptime(string_end1, '%Y-%m-%d %H:%M:%S.%f')

print('Old code:', date_time_end1 - date_time_begin1)

# New Code
string_begin2 = '2021-06-10 19:50:03.060'
date_time_begin2 = datetime.datetime.strptime(string_begin2, '%Y-%m-%d %H:%M:%S.%f')

string_end2 = '2021-06-10 20:29:36.403'
date_time_end2 = datetime.datetime.strptime(string_end2, '%Y-%m-%d %H:%M:%S.%f')

print('New code:', date_time_end2 - date_time_begin2)
