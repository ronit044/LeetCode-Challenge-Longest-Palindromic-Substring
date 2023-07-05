class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        st=""
        arr=[]
        for i in range(len(s)):
            for j in range(i,len(s)):
                for k in range(i,j+1):
                    st+=s[k]
                if(st==st[::-1]):
                    arr.append(st)
                st=""
        return max(arr,key=len)
#This algorithm is completely coded by me and has an issue of greater time complexity
#Check out the second code for a better and efficient code
