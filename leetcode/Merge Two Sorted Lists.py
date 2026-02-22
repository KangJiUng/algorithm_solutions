# 검색 도움


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # dummy는 “가짜 시작 노드”라는 의미로 관습처럼 쓰이곤 함
        dummy = ListNode()

        # current는 포인터로 쓰임
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        # 남은 리스트 붙이기
        current.next = list1 if list1 else list2

        return dummy.next
