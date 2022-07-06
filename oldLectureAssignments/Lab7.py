from LinkedLists import Link

# Question 1
# link = Link(1000)
# print(link.first)
# print(link.rest is Link.empty)
# link = Link(1000, 2000)
# # link = Link(1000, Link()) -> error
# link = Link(1, Link(2, Link(3)))
# print(link.first)
# print(link.rest.first)
# print(link.rest.rest.rest is Link.empty)
# link.first = 9001
# print(link.first)
# link.rest = link.rest.rest
# print(link.rest.first)
# link = Link(1)
# link.rest = link
# print(link.rest.rest.rest.rest.first)


# Question 2

def insert_front(linked_list, new_val):
    """Inserts NEW_VAl in front of LINKED_LIST, returning new linked list."""
    return Link(new_val, linked_list)


def reverse_link(lnk):
    ret_list = Link.empty
    if lnk.rest == Link.empty:
        ret_list = lnk
        return ret_list
    while lnk.rest is not Link.empty:
        new_val = lnk
        ret_list = insert_front(ret_list, new_val)
        lnk = lnk.rest
    return ret_list


s = Link(1, Link(2, Link(3, Link.empty)))
print("Returned list is " + reverse_link(s).__str__())
