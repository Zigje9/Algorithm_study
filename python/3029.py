import sys

start_time = list(map(int, sys.stdin.readline().split(":")))
end_time = list(map(int, sys.stdin.readline().split(":")))


def change_format(s):
    h = s // 3600
    s %= 3600
    m = s // 60
    s %= 60
    print("%02i:%02i:%02i" % (h, m, s))


st = start_time[0]*3600 + start_time[1]*60 + start_time[2]
en = end_time[0]*3600 + end_time[1]*60 + end_time[2]

if st >= en:
    change_format(en + 24*3600 - st)
else:
    change_format(en-st)
