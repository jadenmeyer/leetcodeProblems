from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = ['0'] * n
        for i in range(n):
            j = i + 1
            if j % 3 == 0 and j % 5 == 0:
                ans[i] = "FizzBuzz"
            elif j % 3 == 0:
                ans[i] = "Fizz"
            elif j % 5 == 0:
                ans[i] = "Buzz"
            else:
                ans[i] = str(j)
        return ans



if __name__ == '__main__':
    e = 5
    test = Solution()
    print(test.fizzBuzz(3))
    print(test.fizzBuzz(5))
    print(test.fizzBuzz(15))