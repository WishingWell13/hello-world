class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        numLength = [0] * 61
        numPairs = 0

        for dur in time:
            numPairs += numLength[(60 - dur) % 60]

            # We add the curr value to the array after we change number of pairs, b/c we don't want to create a pair with ourselves
            numLength[dur % 60] += 1

            # print(f'{numPairs} | {dur} {dur%60} | {(60 - (dur%60))}')
            # print(numLength)

        return numPairs
