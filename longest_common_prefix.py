"""Solution to the Longest Common Prefix problem."""


def longest_common_prefix(strs: list[str]) -> str:
    """Return the longest prefix shared by every string in ``strs``.

    Compares characters across the strings from left to right. Runs in
    O(n * m) time, where n is the number of strings and m is the length of
    the shortest string, and uses O(1) extra space.
    """
    if not strs:
        return ""

    for index, character in enumerate(strs[0]):
        for string in strs[1:]:
            if index >= len(string) or string[index] != character:
                return strs[0][:index]

    return strs[0]


if __name__ == "__main__":
    print(longest_common_prefix(["flower", "flow", "flight"]))  # "fl"
    print(longest_common_prefix(["dog", "racecar", "car"]))  # ""
