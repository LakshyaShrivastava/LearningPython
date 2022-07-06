def replace_elements(source_list, dest_list):
    assert len(source_list) <= len(dest_list)
    for element in source_list:
        dest_list[source_list.index(element)] = element


def couple (s, t):
    assert len(s) == len(t)
    ret_list = []
    for i in range(len(s)):
        ret_list.append([s[i], t[i]])
