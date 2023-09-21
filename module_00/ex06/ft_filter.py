def ft_filter(func, iterable):
    '''filter(function or None, iterable) --> filter object
    Return an iterator yielding those items of iterable for
    which function(item)
    is true. If function is None, return the items that are true.'''
    if func is None or not callable(func):
        print("AssetionError function is not callable")
        return None
    try:
        iter(iterable)
    except TypeError:
        print("Second argument is not iterable")
        return None
    return iter([stuff for stuff in iterable if func(stuff) is True])
