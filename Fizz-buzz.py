class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        stack = []
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                stack.append('FizzBuzz')
            elif i%3==0:
                stack.append('Fizz')
            elif i%5==0:
                stack.append('Buzz')
            else:
                stack.append(str(i))
        return stack
