import sys
import re
from datetime import datetime


def test_day4_1():
    event1 = parse_line("[1518-04-21 00:57] wakes up")
    assert event1.event_type == Event.EventType.WakesUp and str(
        event1.date_time) == "1518-04-21 00:57:00"
    event2 = parse_line("[1518-04-21 00:04] Guard #3331 begins shift")
    assert event2.event_type == Event.EventType.BeginsShift and str(
        event2.date_time) == "1518-04-21 00:04:00"
    assert day4_1(
        "[1518-11-01 00:00] Guard #10 begins shift\n[1518-11-01 00:05] falls asleep\n[1518-11-01 00:25] wakes up\n[1518-11-01 00:30] falls asleep\n[1518-11-01 00:55] wakes up\n[1518-11-01 23:58] Guard #99 begins shift\n[1518-11-02 00:40] falls asleep\n[1518-11-02 00:50] wakes up\n[1518-11-03 00:05] Guard #10 begins shift\n[1518-11-03 00:24] falls asleep\n[1518-11-03 00:29] wakes up\n[1518-11-04 00:02] Guard #99 begins shift\n[1518-11-04 00:36] falls asleep\n[1518-11-04 00:46] wakes up\n[1518-11-05 00:03] Guard #99 begins shift\n[1518-11-05 00:45] falls asleep\n[1518-11-05 00:55] wakes up"
    ) == 4455
    print("All tests successful.")


class Event:

    def __init__(self, date_time, event_type, guard_id=None):
        self.date_time = date_time
        self.event_type = event_type
        self.guard_id = guard_id

    class EventType:
        BeginsShift = 1
        FallsAsleep = 2
        WakesUp = 3


def parse_line(line):
    """
    [1518-04-21 00:57] wakes up
    [1518-09-03 00:12] falls asleep
    [1518-04-21 00:04] Guard #3331 begins shift
    """
    regex = r"\[(.*)\] ([a-zA-Z]+) #?(\d*)"
    match = re.search(regex, line)
    date_time = datetime.strptime(match.group(1), r"%Y-%m-%d %H:%M")
    type = match.group(2)
    if type == "wakes":
        event_type = Event.EventType.WakesUp
    elif type == "falls":
        event_type = Event.EventType.FallsAsleep
    else:
        event_type = Event.EventType.BeginsShift

    return Event(date_time, event_type, match.group(3))


def add_guard_sleep_minutes(guard_id, start_sleep, end_sleep, guards):
    if guard_id not in guards:
        guards[guard_id] = [0] * 60
    for i in range(start_sleep, end_sleep):
        guards[guard_id][i] += 1
    return guards


def day4_1(input):
    lines = input.split("\n")
    events = [parse_line(line) for line in lines]
    events = sorted(events, key=lambda e: e.date_time)
    guards_sleep = {}
    for e in events:
        if e.event_type == Event.EventType.BeginsShift:
            guard_id = e.guard_id
        elif e.event_type == Event.EventType.FallsAsleep:
            start_sleep = e.date_time.minute
        else:
            guards_sleep = add_guard_sleep_minutes(
                guard_id, start_sleep, e.date_time.minute, guards_sleep)
    guards_sleep_max_minute = {
        id: max(range(60), key=lambda min: sleep[min])
        for id, sleep in guards_sleep.items()
    }
    guard_id_sleep_max_minute = max(
        guards_sleep_max_minute, key=lambda id: guards_sleep_max_minute[id])
    return int(guard_id_sleep_max_minute
              ) * guards_sleep_max_minute[guard_id_sleep_max_minute]


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as file:
            print(f"Result for file input: {day4_1(file.read().strip())}")
    else:
        test_day4_1()
