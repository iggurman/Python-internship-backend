"""
11. What is the difference between an iterable and an iterator?

Ans:
Iterable: An object that can be iterated over. It implements __iter__().
Examples: list, tuple, string, dictionary.

Iterator: An object that returns elements one by one. It implements
both __iter__() and __next__().
Example: it=iter(1,2,3)
print


12. Can a single iterator object be reused after it is exhausted? Why or why not?

Ans:
No. Once an iterator is exhausted, it cannot be reused because its
internal state has reached the end of the sequence.
To iterate again, a new iterator must be created.


13. How does a for loop internally work with iterators?

Ans:
A for loop first calls iter() on the iterable to get an iterator.
It then repeatedly calls next() on the iterator until
StopIteration is raised, which ends the loop.


14. What will happen if __next__() never raises StopIteration?

Ans:
The iteration will never end, resulting in an infinite loop
(unless the loop is manually stopped or a break statement is used).


15. Which module in Python provides built-in infinite iterators?
Name at least three such functions.

Ans:
The itertools module provides built-in infinite iterators.
Examples:
1. itertools.count()
2. itertools.cycle()
3. itertools.repeat()

"""