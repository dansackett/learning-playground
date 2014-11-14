## Dining Philosophers

http://en.wikipedia.org/wiki/Dining_philosophers_problem

Five silent philosophers sit at a round table with bowls of spaghetti. Forks
are placed between each pair of adjacent philosophers. (An alternative problem
formulation uses rice and chopsticks instead of spaghetti and forks.)

Each philosopher must alternately think and eat. However, a philosopher can
only eat spaghetti when he has both left and right forks. Each fork can be
held by only one philosopher and so a philosopher can use the fork only if
it's not being used by another philosopher. After he finishes eating, he needs
to put down both forks so they become available to others. A philosopher can
grab the fork on his right or the one on his left as they become available,
but can't start eating before getting both of them.

Eating is not limited by the amount of spaghetti left: assume an infinite
supply.
