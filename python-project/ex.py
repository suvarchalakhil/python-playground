class Solution:
    def merge_dictionaries(self, *dicts: list[dict[int, int]]) -> dict[int, int]:
        """
        :type dicts: list[dict[int, int]]
        :rtype: dict[int, int]
        """
        return {**dicts}
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
print("\n================================")
print(Solution().merge_dictionaries(dic1, dic2, dic3))