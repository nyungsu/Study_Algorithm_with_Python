class Node():
    def __init__(self,val=None) -> None:
        self.val = val
        self.next = None
        
    def __str__(self):
        return str(self.key)    # magic method key 값 return
                                # print(v.val)안 해도
                                # print(v)만 해도

a = Node(3)
b = Node(9)
c = Node(-1)
a.next = b
b.next = c
c.next = None # 애초에 self.next = None이라 x


class SinglyLinkedList():
    def __init__(self) -> None:
        self.head = None
        self.size = 0
    
    def pushfront(self,val):
        new_node = Node(val)            # 새로운 노드 객체 생성
        new_node.next = self.head       # 맨 앞에 넣는 거니까
                                        # 새로운 노드 다음을 head
        self.head = new_node            # head 재설정
        self.size += 1

    def pushback(self,val):
        new_node = Node(val)            # 새로운 노드 객체 생성
        if len(self) == 0:              # 처음 집어넣을 때는
            self.head = new_node        # head로 세팅
        else :
            tail_node = self.head           # head부터
            while tail_node.next != None:   # next가 None 될 때까지
               tail_node = tail_node.next   # 타고가라
        self.size += 1       
    def search(self,val):
        v = self.head
        while v != None:
            if v.val == val:
                return v
            v = v.next
        return None



         
# 파이썬 연결리스트 라이브러리를 계속 찾았더니
# 리스트에서 연결리스트 기능까지 다 제공한다네 -_-
a = list()

a.append(1)
a.append(2)
a.append(3)
print(a)

a.insert(1,4)
print(a)