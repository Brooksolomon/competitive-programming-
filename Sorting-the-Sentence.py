class Solution:
    def sortSentence(self, s: str) -> str:
        x=len(s)
        arr=[]
        for i in range(10):
            y=[]
            word=""
            for j in range(x):
                if  s[j].isdigit():
                    if int(s[j]) == i:
                        counter=0
                        while s[j]!=" " and j!=-1:
                            y.append(s[j])
                            j-=1
                            counter+=1
                        y.reverse()
                        y.remove(y[counter-1])
                        for k in y:
                            word +=k
                        arr.append(word)
                        break
        sentence=""
        for a in arr:
            sentence+=a
            sentence+=" "
        sentence= sentence[:-1]
        return sentence
