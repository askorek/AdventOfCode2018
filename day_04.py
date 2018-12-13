import re

with open("day_04.txt") as f:
    data = f.readlines()


# data = """[1518-11-01 00:00] Guard #10 begins shift
# [1518-11-01 00:05] falls asleep
# [1518-11-01 00:25] wakes up
# [1518-11-01 00:30] falls asleep
# [1518-11-01 00:55] wakes up
# [1518-11-01 23:58] Guard #99 begins shift
# [1518-11-02 00:40] falls asleep
# [1518-11-02 00:50] wakes up
# [1518-11-03 00:05] Guard #10 begins shift
# [1518-11-03 00:24] falls asleep
# [1518-11-03 00:29] wakes up
# [1518-11-04 00:02] Guard #99 begins shift
# [1518-11-04 00:36] falls asleep
# [1518-11-04 00:46] wakes up
# [1518-11-05 00:03] Guard #99 begins shift
# [1518-11-05 00:45] falls asleep
# [1518-11-05 00:55] wakes up""".splitlines()

data.sort()

guards = {}
current_guard = None
sleep_start = None

for line in data:
    time_rex = r' [0-9][0-9]:([0-9][0-9])]'
    if "Guard" in line:
        id_rex = r"Guard #([0-9]+) begins"
        id = re.findall(id_rex, line)[0]
        current_guard = int(id)
    if "falls asleep" in line:
        time = re.findall(time_rex, line)[0]
        sleep_start = int(time)
    if "wakes up" in line:
        sleep_stop = int(re.findall(time_rex, line)[0])
        if not current_guard in guards:
            guards[current_guard] = []
        minutes = [0 for _ in range(60)]
        for i in range(sleep_start, sleep_stop):
            minutes[i] = 1
        guards[current_guard].append(minutes)

max_sleep = 0
sleepy_guard = None

for guard in guards:
    sleep_sum = 0
    for shift in guards[guard]:
        sleep_sum += sum(shift)
    if sleep_sum > max_sleep:
        sleepy_guard = guard
        max_sleep = sleep_sum

shifts = len(guards[sleepy_guard])

golden_minute = None
minute_total_max = 0
for minute in range(60):
    minute_sum = sum([shift[minute] for shift in guards[sleepy_guard]])
    if minute_sum > minute_total_max:
        minute_total_max = minute_sum
        golden_minute = minute

print(f"strategy 1 ans: {golden_minute*sleepy_guard}")


max_times_asleep = 0
guard_asleep = None
hour_asleep = None
for minute in range(60):
    for guard in guards:
        total_sleep_in_minutes = sum(shift[minute] for shift in guards[guard])
        if total_sleep_in_minutes > max_times_asleep:
            max_times_asleep = total_sleep_in_minutes
            guard_asleep = guard
            hour_asleep = minute

print(f"strategy 2 ans: {hour_asleep*guard_asleep}")
