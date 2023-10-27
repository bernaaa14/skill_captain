from typing import List


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams = {}  # dictionary to store the anagrams
    for string in strs:  # Iterate over the list of strs
        sorted_str = "".join(sorted(string))  # sort the string,concatenate into single string

    if sorted_str not in anagrams:  # check if the sorted_Str is not yet in anagram
        anagrams[sorted_str] = [string]  # if not, add the inputted string in anagram
    else:
        anagrams[sorted_str].append(string)  # group strings
    return list(anagrams.values())  # teturns the values of the dictionary


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = groupAnagrams(strs)
print(result)

