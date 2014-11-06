"""
The status code produced when the process exits can be accessed via the
exitcode attribute.

For exitcode values:
    exitcode == 0 - no error was produced
    exitcode > 0 - the process had an error, and exited with that code
    exitcode < 0 - the process was killed with a signal of -1 * exitcode
"""

import multiprocessing
import sys
import time

def exit_error():
    sys.exit(1)

def exit_ok():
    return

def return_value():
    return 1

def raises():
    raise RuntimeError('There was an error')

def terminated():
    time.sleep(3)

if __name__ == '__main__':
    jobs = []
    for f in [exit_error, exit_ok, return_value, raises, terminated]:
        print 'Starting process for', f.func_name
        j = multiprocessing.Process(target=f, name=f.func_name)
        jobs.append(j)
        j.start()

    jobs[-1].terminate()

    for job in jobs:
        j.join()
        print '%s.exitcode = %s' % (job.name, job.exitcode)
