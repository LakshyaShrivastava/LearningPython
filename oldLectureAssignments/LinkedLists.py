class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


def range_link(start, end):
    """Return a Link containing consecutive integers from START to END, not including END."""
    if start >= end:
        return Link.empty
    return Link(start, range_link(start + 1, end))


def map_link(f, ll):
    """Return a Link that contains f(x) for each x in Link ll"""
    if ll is Link.empty:
        return Link.empty
    return Link(f(ll.first), map_link(f, ll.rest))


def filter_link(f, ll):
    """Return a Link that contains only the elements x of Link ll for which f(x)is a true value."""
    if ll is Link.empty:
        return Link.empty
    elif f(ll.first):
        return Link(ll.first, filter_link((f, ll.rest)))
    return filter_link(f, ll.rest)


s = Link("A", Link("B", Link("c")))
s.first = "Hi"
s.rest.first = "Hola"
s.rest.rest.first = "Oi"


def insert_front(linked_list, new_val):
    """Inserts NEW_VAl in front of LINKED_LIST, returning new linked list."""
    return Link(new_val, linked_list)


def add(ordered_list, new_val):
    """Add NEW_VAL to ORDERED_LIST, returning modified ORDERED_LIST"""
    if new_val < ordered_list.first:
        original_first = ordered_list.first
        ordered_list.first = new_val
        ordered_list.rest = Link(original_first, ordered_list.rest)
    elif new_val > ordered_list.first and ordered_list.rest is Link.empty:
        ordered_list.rest = Link(new_val)
    elif new_val > ordered_list.first:
        add(ordered_list.rest, new_val)
    return ordered_list
