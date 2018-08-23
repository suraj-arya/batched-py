# -*- coding: utf-8 -*-

import functools
import types


def batched(batch_size):
    """
    call the decorated function with batching the first argument
    into given batch size

    :param batch_size: number of items per batch
    :type batch_size: int

    >>> @batched(batch_size=2)
    ... def test(batch):
    ...     print batch
    ...     return True
    ...
    >>> test([1, 2, 3])
    [1, 2]
    [3]
    [True, True]
    >>> def generator():
    ...     for i in xrange(5):
    ...         yield i
    ...
    >>> test(generator())
    [0, 1]
    [2, 3]
    [4]
    [True, True, True]
    >>> test({4})
    [4]
    [True]
    >>> test((1, 5))
    [1, 5]
    [True]
    """
    def batched_list(func, data, *args, **kwargs):
        results = []
        batch = []
        for item in data:
            batch.append(item)
            if len(batch) == batch_size:
                results.append(func(batch, *args, **kwargs))
                batch = []
        if batch:
            results.append(func(batch, *args, **kwargs))
        return results

    def decorator(func):
        @functools.wraps(func)
        def wrapper(data, *args, **kwargs):
            assert isinstance(data, (list, tuple, set, types.GeneratorType)),\
                "data should be of list types."
            return batched_list(func, data, *args, **kwargs)
        return wrapper
    return decorator


if __name__ == '__main__':
    import doctest
    doctest.testmod()
