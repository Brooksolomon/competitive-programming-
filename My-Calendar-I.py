class MyCalendar:

    def __init__(self):
        self.myarr=[]

    def book(self, start: int, end: int) -> bool:
        if not self.myarr:
            self.myarr.append([start,end])
            return True
        # left , right = 0, len(self.myarr)
        # while left <= right:
        #     m =  left + (right - left) // 2

        #     if self.myarr[m][1] < start:
        #         left =  m+1
        #     else: right = m - 1
        m = bisect.bisect_right(self.myarr,start,key = lambda x:x[1])
        if m >= len(self.myarr):
            self.myarr.append([start,end])
            return True
        if self.myarr[m][0] >= end :
            self.myarr.insert(m,[start,end])
            return True
        return False

            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
