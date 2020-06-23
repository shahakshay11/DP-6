"""
// Time Complexity : O(n)
// Space Complexity : O(n) or O(1) based on the constraint
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

// Your code here along with comments explaining your approach
Algorithm Explanation
Given below
"""
import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        n = 10
        s -[1,2,3,5,6,10,15,8,20,18,30,24,40,45,27,50]
        h - [12,15,16,18,20,24,27,30,40,45,50]
        We use Hashset to maintain non duplication of ugly numbers 
        and min heap to maintain the order of ugly numbers
        
        """
        arr = [1]
        visited = set([1])
        i = 1
        while i<=n:
            #get the latest ugly number
            curr = heapq.heappop(arr)
            for j in [2,3,5]:
                #add the prime factor numbers of ugly number
                if curr*j not in visited:
                    visited.add(curr*j)
                    heapq.heappush(arr,curr*j)
            i+=1
        return curr
    
    
        """
        DP approach
        We keep track of minimum ugly number(base) at each stage, so that when it is spawned with prime factors multipliers, we ensure that order is maintained and duplication is avoided
        So idea is to have a result array which keeps track of the ugly numbers based on which position(from 2,3 and 5 ptr) is minimum
        Return the n-1'th element from result array
        """
        result = [1]
        i2,i3,i5 = 0,0,0
        for i in range (1,1960):
            ugly = min(result[i2]*2,result[i3]*3,result[i5]*5)
            result.append(ugly)
            if ugly == result[i2]*2:
                i2+=1
            if ugly == result[i3]*3:
                i3+=1
            if ugly == result[i5]*5:
                i5+=1
        return result[n-1]