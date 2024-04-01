import time
import sys

cutoff = 0.3
timeout = 1.5

DOT = (0.1, cutoff)
DASH = (cutoff, timeout)

states = [
    DASH,
    DOT,
    DOT,
    DASH,
    DOT
]
num_states = len(states)

times = []

t = time.time()

for _ in sys.stdin:
    t2 = time.time()
    diff = t2 - t
    t = t2

    if (diff > timeout):
        times = []
        print('TIMEOUT')
    else:
        times.append(diff)

    if (len(times) >= num_states):
        last_states = times[(-num_states):]

        valid = True
        for i in range(num_states):
            (low, high) = states[i]
            diff = last_states[i]

            if not (low < diff < high):
                print('invalid', i)
                valid = False

        if valid:
            print('BINGO')
            times = []
