class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        cs=0
        clips.sort()
        myarr=[]
        i=0
        count=0
        while clips:
            i=0
            while i < len(clips) and clips[i][0] <= cs :
                myarr.append(clips[i][1])
                i+=1
            if len(myarr)==0:return -1
            heapify(myarr)
            while len(myarr) - 1:
                heappop(myarr)
            x=heappop(myarr)
            cs=x
            count+=1
            clips=clips[i:]
            if cs >= time:return count
        if cs<time:
            return -1
        return count
