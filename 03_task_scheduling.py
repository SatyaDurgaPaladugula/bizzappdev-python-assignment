"""
Problem:
Maximize number of tasks completed within deadlines.
"""
import heapq

def schedule_tasks(tasks):
    tasks.sort(key=lambda x: x['deadline'])
    time = 0
    max_tasks = []

    for task in tasks:
        time += task['duration']
        heapq.heappush(max_tasks, -task['duration'])
        if time > task['deadline']:
            time += heapq.heappop(max_tasks)

    return len(max_tasks)


tasks = [
    {'name': 'Task 1', 'deadline': 4, 'duration': 2},
    {'name': 'Task 2', 'deadline': 3, 'duration': 1},
    {'name': 'Task 3', 'deadline': 2, 'duration': 1},
    {'name': 'Task 4', 'deadline': 1, 'duration': 2},
]
print("Max tasks that can be completed:", schedule_tasks(tasks))
