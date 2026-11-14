"""Optimal O(n) solution to the Two Sum problem."""


def two_sum(nums: list[int], target: int) -> list[int]:
    """Return indices of two distinct values that add up to target.

    Uses a hash map for O(n) time and O(n) extra space. Raises ValueError
    if no matching pair exists.
    """
    seen: dict[int, int] = {}

    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index

    raise ValueError("No two numbers add up to the target")


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
