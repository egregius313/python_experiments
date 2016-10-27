#!/usr/bin/env python


from contextlib import contextmanager


class HaltedSwitch(BaseException):
    """Meant to be used for `break`-like behavior in switches.
    """


class SwitchError(ValueError):
    """Used for case's implentation. Will be raised if
    there is no value to be matched.
    """


_switches = []


@contextmanager
def switch(value):
    """Allows switch/case like behaviour in a
    contextmanager.

    >>> with switch(3 * 4):
    ...     if case(12):
    ...         print('Twelve')
    ...     elif case(10):
    ...         print('Ten')
    ...     else:
    ...         print('Something else')
    ...
    Twelve

    See also:
        case
    """
    global _switches
    try:
        _switches.append(value)
        yield value
    except HaltedSwitch:
        pass
    finally:
        _switches.pop()


def case(*values):
    """Return whether or not any of the parameters
    is equivalent to the current switch.
    """
    if len(_switches) < 1:
        # ensure _switches is not empty
        raise SwitchError('No value to be matched in current scope.')
    return any(value == _switches[-1] or value is _switches[-1]
               for value in values)


def halt():
    """Used as an equivalent of the break statement
    in other languages' case statements.
    """
    raise HaltedSwitch()

