# encoding:utf-8


def read_keys(path: str) -> dict:
    '''
    this function is only to read token.
    if key.txt does not exist, log shows FileNotFoundError and Type Error.
    '''
    try:
        with open(path, "r")as f:
            text = f.readlines()
            list_dict = []
            for t in text:
                list_dict.append(tuple(t.rstrip().split(":")))
            return dict(list_dict)
    except Exception:
        return None


def main():
    from bot import MyBot
    bot = MyBot(read_keys("..\\.data\\key.txt"), "!")
    bot.wake()


if __name__ == "__main__":
    main()
