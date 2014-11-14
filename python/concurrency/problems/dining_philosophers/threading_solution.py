import threading
import time
import random
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',)

class Philosopher(threading.Thread):

    def __init__(self, group=None, target=None, name=None, args=(),
                 kwargs=None, verbose=None):
        """
        Setup our philosopher.
        """
        threading.Thread.__init__(self, group=group, target=target, name=name,
                                  verbose=verbose)
        self.current_forks = []
        self.index = args[0]
        self.set_forks(args[1])
        self.has_eaten = 0

    def run(self):
        """
        Main thread process where they are deep in thought.
        """
        logging.debug('Thinking for a few seconds')
        time.sleep(random.random())
        self.pick_up_forks()

    def set_forks(self, forks):
        """
        Based on the forks available and the position of the philosopher,
        determine the left and right fork.
        """
        if self.index == 0:
            self.left_fork = forks[-1]
            self.right_fork = forks[self.index]
        else:
            self.left_fork = forks[self.index - 1]
            self.right_fork = forks[self.index]

    def eat(self):
        """
        When the philosopher has both forks, he can safely eat
        """
        self.has_eaten += 1
        logging.debug('Eating for a little. Number: %d' % self.has_eaten)
        time.sleep(random.random())

    def pick_up_forks(self):
        """
        If the philosopher hasn't eaten yet, he may attempt to pick up his
        right fork and if he gets that then he can pick up the left fork to
        eat.
        """
        if self.has_eaten < 3:
            has_it = self.right_fork.pick_up()

            if has_it:
                logging.debug('Got right fork')
                self.current_forks.append(self.right_fork)
                has_it = self.left_fork.pick_up()

                if has_it:
                    logging.debug('Got left fork')
                    self.current_forks.append(self.left_fork)
                    self.eat()

            self.put_down_forks()
        else:
            return

    def put_down_forks(self):
        """
        Put down current forks and think again.
        """
        for fork in self.current_forks:
            fork.put_down()

        self.current_forks = []
        self.run()

class Fork(object):
    def __init__(self):
        """
        Define lock.
        """
        self.lock = threading.Lock()

    def pick_up(self):
        """
        Pick up a fork means acquiring the lock
        """
        has_it = self.lock.acquire()
        return has_it

    def put_down(self):
        """
        Putting down a fork means releasing the lock
        """
        self.lock.release()


forks = [Fork() for i in xrange(5)]
philosophers = [Philosopher(args=(i, forks,), name='Philosopher %d' % i)
                for i in xrange(5)]

for p in philosophers:
    p.start()

for p in philosophers:
    p.join()
