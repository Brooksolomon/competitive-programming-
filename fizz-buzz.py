class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n+1):
            answer.insert(i,str(i))
        for i in range(1, n+1):
            if i % 3 == 0:
                answer[i - 1] = "Fizz"
            if i % 5 ==0:
                answer[i - 1] = "Buzz"
            if i % 3 == 0 and i % 5 == 0 :
                answer[i - 1] = "FizzBuzz"
            else
        return answer
