from ex import Solution


def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}


def test_merge_dictionaries():
    try:
        args1 = [dic1, dic2]
        args2 = [dic1, dic2, dic3]
        res1 = {1: 10, 2: 20, 3: 30, 4: 40}
        res2 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
        case1 = Solution().merge_dictionaries(args1)
        assert case1 == res1, f"Running merge_dictionaries({args1})... Expected {res1}, got {case1}"
        case2 = Solution().merge_dictionaries(args2)
        assert case2 == res2, f"Running merge_dictionaries({args2})... Expected {res2}, got {case2}"
        success()
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)


if __name__ == "__main__":
    test_merge_dictionaries()
