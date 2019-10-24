from strings import *


def filtering():
    strings = [
        "hello",
        "world",
        "how",
        "are",
        "you",
        "python_file.py",
        "c_file.c",
    ]
    inclusions = ["."]
    exclusions = ["py"]

    def basic_functionality(mode):
        print(f"basic functionality test, mode=\"{mode}\"")
        print(filter_strings(strings, inclusions, exclusions, mode))
        print("\n")

    basic_functionality("both")
    basic_functionality("include")
    basic_functionality("exclude")


if __name__ == "__main__":
    filtering()
