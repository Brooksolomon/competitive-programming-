class Solution:
    def freqAlphabets(self, s: str) -> str:
        md= {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10': 'j', '11': 'k', '12': 'l', '13': 'm', '14': 'n', '15': 'o', '16': 'p', '17': 'q', '18': 'r', '19': 's', '20': 't', '21': 'u', '22': 'v', '23': 'w', '24': 'x', '25': 'y', '26': 'z'}
        stack = []
        for i in s:
            if i=='#':
                two = stack.pop()
                one = stack.pop()
                stack.append(md[one+two])
            else:
                stack.append(i)
        for i in range(len(stack)):
            if stack[i] in md:
                stack[i] = md[stack[i]]

        return "".join(stack)


            
