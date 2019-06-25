# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:38:21 2019

@author: ascent
"""

# unordered linked list 공부
# unordered linked list는 sorted 되지 않고 그냥 본인이 원하는 위치에 새로운 element 삽입.
# ordered linked list는 sorted 되어 있으며 새로운 element 삽입할 때도 위치에 맞게 삽입됨.
# unordered와 ordered가 단방향 양방향을 의미하는 것 아님 -> 단방향은 singly linked list, 양방향은 doubly linked list
# http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html#implementing-an-unordered-list-linked-lists


'''
The basic building block for the linked list implementation is the node. 
Each node object must hold at least two pieces of information. 
First, the node must contain the list item itself. 
We will call this the data field of the node. 
In addition, each node must hold a reference to the next node.
'''



'''
# The special Python reference value None will play an important role in the Node class and later in the linked list itself. 
# A reference to None will denote the fact that there is no next node.
Since this is sometimes referred to as “grounding the node,” we will use the standard ground symbol to denote a reference that is referring to None. 
It is always a good idea to explicitly assign None to your initial next reference values.

'''
class Node:
    def __init__(self, initdata):
        
        self.data = initdata
        self.next = None
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newData):
        self.data = newData
    
    def setNext(self, newnext):
        self.next = newnext

'''
the UnorderedList class must maintain a reference to the first node.
Note that each list object will maintain a single reference to the head of the list.
It is very important to note that the list class itself does not contain any node objects. 
Instead it contains a single reference to only the first node in the linked structure.
'''

# data 없이 맨 처음 head 역할만 하면서 그 다음 node만 가르키는 node가 따로 있는 것 아님.
# Unordered list로 object를 만들고, 이 list의 맨 처음 node가 head임
# Unordered list의 object가 head를 가리키는 정보를 갖고 있는 것이고, 
# 맨 처음 data를 가진 node만을 가르키는 node를 따로 head로 두지 않음
# 정리: UnorderedList로 linked list object를 만듬. 처음엔 list의 head에 아무 값도 없음.(추가한 Node가 없으니) list에 Node가 추가되면 Node의 head에 추가되는 Node의 reference를 할당함.

''' add function
Since this list is unordered, the specific location of the new item with respect to the other items already in the list is not important. 
The new item can go anywhere.
All of the other nodes can only be reached by accessing the first node and then following next links. 
This means that the easiest place to add the new node is right at the head, or beginning, of the list.
In other words, we will make the new item the first item of the list and the existing items will need to be linked to this new first item so that they follow.
unordered linked list여서 새로운 node는 기존 list에서 아무대나 들어가도 됨.
그러나 linked list로 접근하려면 head of the list를 통해서 accessing 해야함.
따라서 새로운 node를 head로 만들고 나머지 node들을 새로운 node의 뒤에 이어지게 함.
다른 사람 설명 보면 tail 위치를 갖게 만들어서, list의 맨 마지막에 node 추가하기도 함.
'''
class UnorderedList:
    def __init__(self):
        self.head = None
    
    #The isEmpty method simply checks to see if the head of the list is a reference to None.
    def isEmpty(self):
        return self.head == None

    def add(self, item):
        # Step 0. Create the new Node
        # Step 1. Change the next reference of the new node and places the item as its data
        # Step 2. we can modify the head of the list to refer to the new node
        # 파라미터로 넘어온 값(item)을 갖는 새로운 노드 만듬
        # head가 가리키고 있던 첫번째 node의 reference를 new node가 가리킴
        # head가 가리키는 값을 기존 첫번째 node에서 새로운 node로 변경
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    # we need to traverse the linked list and keep a count of the number of nodes that occurred.
    # head가 가리키는 첫 Node부터 마지막 Node까지 traversal 하며 count
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    # 특정 item이 linked list에 있는지 확인
    def search(self, item):
        current = self.head
        found = False
        # current가 list 끝까지 오기 전이고 아직 찾지 못했으면(found == False) 계속 탐색
        # current가 list 끝까지 오거나 원하는 값을 찾으면 그만 탐색
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        
        return found

    # if the item is not in list, error would occur
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        # If the item to be removed happens to be the first item in the list, then current will reference the first node in the linked list. 
        # This also means that previous will be None.
        # In this case, it is not previous but rather the head of the list that needs to be changed
        if previous == None:  # remove하는 item이 head node일 경우
            self.head = current.getNext()
        # remove item이 head node가 아닌 경우 previous node가 current의 다음 node를 가리킴. 
        # 그래서 previous가 current를 건너띄고 그 다음 node를 가리키므로 current node를 reference하는 변수가 없어짐.
        # 그래서 current node는 없어지고 previous
        else: 
            previous.setNext(current.getNext())
    
