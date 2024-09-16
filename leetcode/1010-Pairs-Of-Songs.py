class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        numLength = [0] * 61
        numPairs = 0

        for dur in time:
            # We will only get pairs (time[j],time[i]) where index j > index i
            # Because we only check for target values that come before current value
            # target value = (60 - dur) % 60
            numPairs += numLength[(60 - (dur%60)) % 60]

            # We add the curr value to the array after we change number of pairs, b/c we don't want to create a pair with ourselves
            numLength[dur % 60] += 1

            # print(f'{numPairs} | {dur} | {(60 - dur) % 60}')
            # print(numLength)

        return numPairs
