Using Counters for Frequency
============================

Instead of manually building counts of words and items, we can use the
collections.Counter class which does it for us. It essentially makes a
dictionary with words as keys and counts as values without you having to do
the heavy lifting::

    >>> from collections import Counter
    >>> words = [
    ...     'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    ...     'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    ...     'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    ...     'my', 'eyes', "you're", 'under'
    ... ]
    >>>
    >>> word_counts = Counter(words)
    >>> top_three = word_counts.most_common(3)
    >>> print(top_three)
    [('eyes', 8), ('the', 5), ('look', 4)]

This is always prefered over manual counting.
