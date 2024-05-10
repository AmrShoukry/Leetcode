class Solution:

    def custom_key(self, fraction):
        numerator, denomirator = map(int, (fraction.split('/')))
        return numerator / denomirator

    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        length = len(arr)
        fractions = []
        for i in range(length):
            for j in range(i + 1, length):
                fractions.append(f'{arr[i]}/{arr[j]}')
        fractions = sorted(fractions, key=self.custom_key)
        num1, num2 = fractions[k - 1].split('/')
        return [int(num1), int(num2)]
