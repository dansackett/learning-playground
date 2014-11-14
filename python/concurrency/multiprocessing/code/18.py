"""
The Pool class can be used to manage a fixed number of workers for simple
cases where the work to be done can be broken up and distributed between
workers independently. The return values from the jobs are collected and
returned as a list. The pool arguments include the number of processes and a
function to run when starting the task process (invoked once per child).
"""

import multiprocessing

def do_calculation(data):
    return data * 2

def start_process():
    print 'Starting', multiprocessing.current_process().name

if __name__ == '__main__':
    inputs = list(range(10))
    print 'Inputs   :', inputs

    builtin_outputs = map(do_calculation, inputs)
    print 'Built-Ins:', builtin_outputs

    pool_size = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(processes=pool_size, initializer=start_process,
                               maxtasksperchild=2)
    pool_outputs = pool.map(do_calculation, inputs)
    pool.close()
    pool.join()

    print 'Pool    :', pool_outputs
