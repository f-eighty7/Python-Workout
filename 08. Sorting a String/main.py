def strsort(s):
    return "".join(sorted(s))


# print(strsort("bca"))


def strsort2(s):
    return ", ".join(sorted(s.split()))


print(strsort2("Tom Dick Harry"))
