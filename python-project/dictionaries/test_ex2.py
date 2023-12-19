from ex2 import Solution


def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")


def test_generate_squared_dict():
    try:
        f_name = 'generate_squared_dict'
        args1 = 1
        args2 = 5
        args3 = 10
        res1 = {1: 1}
        res2 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
        res3 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
        case1 = Solution().generate_squared_dict(args1)
        assert case1 == res1, f"Running {f_name}({args1})... Expected {res1}, got {case1}"
        case2 = Solution().generate_squared_dict(args2)
        assert case2 == res2, f"Running {f_name}({args2})... Expected {res2}, got {case2}"
        case3 = Solution().generate_squared_dict(args3)
        assert case3 == res3, f"Running {f_name}({args3})... Expected {res3}, got {case3}"
        success()
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)


if __name__ == "__main__":
    test_generate_squared_dict()
