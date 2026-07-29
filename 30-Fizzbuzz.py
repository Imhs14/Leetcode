class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        op = []
        for n in range(1, n+1):
            if n % 3 == 0 and n % 5 == 0:
                op.append("FizzBuzz")
            elif n % 3 == 0:
                op.append("Fizz")
            elif n % 5 == 0 :
                op.append("Buzz")
            else:
                op.append(str(n))
        return op
"""
n = 3
o/p = ["1","2","Fizz"]
"""
