class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tokenTime = timeToLive
        self.holder = {}
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.holder[tokenId] = currentTime + self.tokenTime
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.holder and self.holder[tokenId] > currentTime:
            self.holder[tokenId] = currentTime + self.tokenTime
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for i in self.holder:
            if self.holder[i] > currentTime:
                count+=1
        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
