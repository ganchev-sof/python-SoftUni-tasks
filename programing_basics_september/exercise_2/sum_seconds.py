seconds_in_minutes = 60

time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third
minutes = total_time // seconds_in_minutes
seconds = total_time % seconds_in_minutes

if seconds < 10:
    print(f"{minutes}:{seconds:02d}")
else:
    print(f"{minutes}:{seconds}")