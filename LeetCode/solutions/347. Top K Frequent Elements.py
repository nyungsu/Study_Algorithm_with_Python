'''
문제 이름 : 347. Top K Frequent Elements
문제 링크 : https://leetcode.com/problems/top-k-frequent-elements/
문제 풀이 : collections Counter 이용 most_common(k)
시간 복잡도 : O(NlogN)
공간 복잡도 : O(1)

Counter.most_common(k)의 시간 복잡도는
k가 1보다 큰 경우는 O(NlogN)
k = 1 일 때는 O(N)이라고 한다.
참조 : https://stackoverflow.com/questions/29240807/python-collections-counter-most-common-complexity
'''




from collections import Counter

class Solution:
    def topKFrequent(self,nums: list[int], k: int) -> list[int]:
        temp = Counter(nums)
        most_common = temp.most_common(k)                           # [(key,val), (key,val)] 형태로 반환
        result = [most_common[i][0] for i in range(k)]
        return result


