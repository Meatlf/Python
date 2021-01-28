name = "小明"


def test():
    global name
    name = "xiaoming"
    return name


if __name__ == "__main__":
    print(name)
    print(test())
    print(name)
