import random as r
import matplotlib.pyplot as plt
#ZAD1
"""
Zad2 jest ponumerowane podpunktami np 1 podpunkt -> i, 2 podpunkt -> ii
"""
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_index(self, value):
        curr = self.head
        idx = 0
        while curr is not None:
            if curr.data == value:
                return idx
            curr = curr.next
            idx += 1
        raise ValueError('Value not found in list')
    def clear_list(self):
        self.head = None
office = ["A", "A", "A", "B", "B", "B", "C", "C", "C", "E"]
tasks = ["A1", "A2", "A3", "A4", "B5", "B6", "B7", "B8", "C9", "C11", "C12"]
clients = []
for i in range(40):
    x = r.choice(tasks)
    clients.append(x)

ll = LinkedList()
ll.insert_values(clients)
ll.print()
t = 0
If_A = 1
If_B = 1
If_C = 1
If_LL = 1
clients_served = [0 for x in range(10)]
while office != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
    if If_LL == 1:
        if If_A == 1:
            for x in range(0, 3):
                curr = ll.head
                if curr is None:
                    If_LL == 0
                    break
                if office[x] == "A" or office[x] == 0:
                    while curr.data[0] != "A":
                        curr = curr.next
                        if curr is None:
                            If_A = 0
                            break
                    else:
                        office[x] = int(curr.data[1:])
                        If_A = 1
                        k = ll.get_index(curr.data)
                        ll.remove_at(k)
                        clients_served[x] += 1
        if If_B == 1:
            for x in range(3, 6):
                curr = ll.head
                if curr is None:
                    If_LL == 0
                    break
                if office[x] == "B" or office[x] == 0:
                    while curr.data[0] != "B":
                        curr = curr.next
                        if curr is None:
                            If_B = 0
                            break
                    else:
                        office[x] = int(curr.data[1:])
                        If_B = 1
                        k = ll.get_index(curr.data)
                        ll.remove_at(k)
                        clients_served[x] += 1
        if If_C == 1:
            for x in range(6, 9):
                curr = ll.head
                if curr is None:
                    If_LL == 0
                    break
                if office[x] == "C" or office[x] == 0:
                    while curr.data[0] != "C":
                        curr = curr.next
                        if curr is None:
                            If_C = 0
                            break
                    else:
                        office[x] = int(curr.data[1:])
                        If_C = 1
                        k = ll.get_index(curr.data)
                        ll.remove_at(k)
                        clients_served[x] += 1
        for x in range(9, 10):
            curr = ll.head
            if curr is None:
                If_LL == 0
                break
            if office[x] == "E" or office[x] == 0:
                office[x] = int(curr.data[1:])
                k = ll.get_index(curr.data)
                ll.remove_at(k)
                clients_served[x] += 1
    office = [x - 1 if x > 0 else 0 for x in office]
    t += 1
print(f"czas trwania {t}, Liczba obsłużonych klientów w poszczególnych okienkach {clients_served}")
"""

"""


#ZAD2 i
office_2 = ["A", "A", "A", "B", "B", "B", "C", "C", "C"]
ll_2 = LinkedList()
ll_2.insert_values(clients)
ll_2.print()
t_2 = 0
If_A = 1
If_B = 1
If_C = 1
If_ll_2 = 1

while office_2 != [0, 0, 0, 0, 0, 0, 0, 0, 0]:
    if If_ll_2 == 1:
        if If_A == 1:
            for x in range(0, 3):
                curr = ll_2.head
                if curr is None:
                    If_ll_2 == 0
                    break
                if office_2[x] == "A" or office_2[x] == 0:
                    while curr.data[0] != "A":
                        curr = curr.next
                        if curr is None:
                            If_A = 0
                            break
                    else:
                        office_2[x] = int(curr.data[1:])
                        If_A = 1
                        k = ll_2.get_index(curr.data)
                        ll_2.remove_at(k)
        if If_B == 1:
            for x in range(3, 6):
                curr = ll_2.head
                if curr is None:
                    If_ll_2 == 0
                    break
                if office_2[x] == "B" or office_2[x] == 0:
                    while curr.data[0] != "B":
                        curr = curr.next
                        if curr is None:
                            If_B = 0
                            break
                    else:
                        office_2[x] = int(curr.data[1:])
                        If_B = 1
                        k = ll_2.get_index(curr.data)
                        ll_2.remove_at(k)
        if If_C == 1:
            for x in range(6, 9):
                curr = ll_2.head
                if curr is None:
                    If_ll_2 == 0
                    break
                if office_2[x] == "C" or office_2[x] == 0:
                    while curr.data[0] != "C":
                        curr = curr.next
                        if curr is None:
                            If_C = 0
                            break
                    else:
                        office_2[x] = int(curr.data[1:])
                        If_C = 1
                        k = ll_2.get_index(curr.data)
                        ll_2.remove_at(k)
    office_2 = [x - 1 if x > 0 else 0 for x in office_2]
    t_2 += 1
print(f"Czas trwania: {t_2}")

office_3 = ["A", "A", "B", "B", "C", "C", "E", "E", "E"]
ll_3 = LinkedList()
ll_3.insert_values(clients)
ll_3.print()
t_3 = 0
If_A = 1
If_B = 1
If_C = 1
If_LL = 1

while office_3 != [0, 0, 0, 0, 0, 0, 0, 0, 0]:
    if If_LL == 1:
        if If_A == 1:
            for x in range(0, 2):
                curr = ll_3.head
                if curr is None:
                    If_LL == 0
                    break
                if office_3[x] == "A" or office_3[x] == 0:
                    while curr.data[0] != "A":
                        curr = curr.next
                        if curr is None:
                            If_A = 0
                            break
                    else:
                        office_3[x] = int(curr.data[1:])
                        If_A = 1
                        k = ll_3.get_index(curr.data)
                        ll_3.remove_at(k)
        if If_B == 1:
            for x in range(2, 4):
                curr = ll_3.head
                if curr is None:
                    If_LL == 0
                    break
                if office_3[x] == "B" or office_3[x] == 0:
                    while curr.data[0] != "B":
                        curr = curr.next
                        if curr is None:
                            If_B = 0
                            break
                    else:
                        office_3[x] = int(curr.data[1:])
                        If_B = 1
                        k = ll_3.get_index(curr.data)
                        ll_3.remove_at(k)
        if If_C == 1:
            for x in range(4, 6):
                curr = ll_3.head
                if curr is None:
                    If_LL == 0
                    break
                if office_3[x] == "C" or office_3[x] == 0:
                    while curr.data[0] != "C":
                        curr = curr.next
                        if curr is None:
                            If_C = 0
                            break
                    else:
                        office_3[x] = int(curr.data[1:])
                        If_C = 1
                        k = ll_3.get_index(curr.data)
                        ll_3.remove_at(k)
        for x in range(6, 9):
            curr = ll_3.head
            if curr is None:
                If_LL == 0
                break
            if office_3[x] == "E" or office_3[x] == 0:
                office_3[x] = int(curr.data[1:])
                k = ll_3.get_index(curr.data)
                ll_3.remove_at(k)
    office_3 = [x - 1 if x > 0 else 0 for x in office_3]
    t_3 += 1
print(f"czas trwania {t_3}")

office_4 = ["A", "B", "B", "C", "C", "C", "E"]
ll_4 = LinkedList()
ll_4.insert_values(clients)
ll_4.print()
t_4 = 0
If_A = 1
If_B = 1
If_C = 1
If_LL = 1

while office_4 != [0, 0, 0, 0, 0, 0, 0]:
    if If_LL == 1:
        if If_A == 1:
            for x in range(0, 1):
                curr = ll_4.head
                if curr is None:
                    If_LL == 0
                    break
                if office_4[x] == "A" or office_4[x] == 0:
                    while curr.data[0] != "A":
                        curr = curr.next
                        if curr is None:
                            If_A = 0
                            break
                    else:
                        office_4[x] = int(curr.data[1:])
                        If_A = 1
                        k = ll_4.get_index(curr.data)
                        ll_4.remove_at(k)
        if If_B == 1:
            for x in range(1, 3):
                curr = ll_4.head
                if curr is None:
                    If_LL == 0
                    break
                if office_4[x] == "B" or office_4[x] == 0:
                    while curr.data[0] != "B":
                        curr = curr.next
                        if curr is None:
                            If_B = 0
                            break
                    else:
                        office_4[x] = int(curr.data[1:])
                        If_B = 1
                        k = ll_4.get_index(curr.data)
                        ll_4.remove_at(k)
        if If_C == 1:
            for x in range(3, 6):
                curr = ll_4.head
                if curr is None:
                    If_LL == 0
                    break
                if office_4[x] == "C" or office_4[x] == 0:
                    while curr.data[0] != "C":
                        curr = curr.next
                        if curr is None:
                            If_C = 0
                            break
                    else:
                        office_4[x] = int(curr.data[1:])
                        If_C = 1
                        k = ll_4.get_index(curr.data)
                        ll_4.remove_at(k)
        for x in range(6, 7):
            curr = ll_4.head
            if curr is None:
                If_LL == 0
                break
            if office_4[x] == "E" or office_4[x] == 0:
                office_4[x] = int(curr.data[1:])
                k = ll_4.get_index(curr.data)
                ll_4.remove_at(k)
    office_4 = [x - 1 if x > 0 else 0 for x in office_4]
    t_4 += 1
print(f"czas trwania {t_4}")


#ZAD2 ii
office = ["A", "A", "A", "B", "B", "B", "C", "C", "C", "E"]
tasks = ["A1", "A2", "A3", "A4", "B5", "B6", "B7", "B8", "C9", "C11", "C12"]
clients.clear()
for i in range(30):
    x = r.choice(tasks)
    clients.append(x)


ll.clear_list()
ll.insert_values(clients)
ll.print()
t = 0
If_A = 1
If_B = 1
If_C = 1
If_LL = 1

while office != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
    if If_LL == 1:
        if If_A == 1:
            for x in range(0, 3):
                curr = ll.head
                if curr is None:
                    If_LL == 0
                    break
                if office[x] == "A" or office[x] == 0:
                    while curr.data[0] != "A":
                        curr = curr.next
                        if curr is None:
                            If_A = 0
                            break
                    else:
                        office[x] = int(curr.data[1:])
                        If_A = 1
                        k = ll.get_index(curr.data)
                        ll.remove_at(k)
        if If_B == 1:
            for x in range(3, 6):
                curr = ll.head
                if curr is None:
                    If_LL == 0
                    break
                if office[x] == "B" or office[x] == 0:
                    while curr.data[0] != "B":
                        curr = curr.next
                        if curr is None:
                            If_B = 0
                            break
                    else:
                        office[x] = int(curr.data[1:])
                        If_B = 1
                        k = ll.get_index(curr.data)
                        ll.remove_at(k)
        if If_C == 1:
            for x in range(6, 9):
                curr = ll.head
                if curr is None:
                    If_LL == 0
                    break
                if office[x] == "C" or office[x] == 0:
                    while curr.data[0] != "C":
                        curr = curr.next
                        if curr is None:
                            If_C = 0
                            break
                    else:
                        office[x] = int(curr.data[1:])
                        If_C = 1
                        k = ll.get_index(curr.data)
                        ll.remove_at(k)
        for x in range(9, 10):
            curr = ll.head
            if curr is None:
                If_LL == 0
                break
            if office[x] == "E" or office[x] == 0:
                office[x] = int(curr.data[1:])
                k = ll.get_index(curr.data)
                ll.remove_at(k)
    office = [x - 1 if x > 0 else 0 for x in office]
    t += 1
print(f"czas trwania {t}")

office_2 = ["A", "A", "A", "B", "B", "B", "C", "C", "C"]
ll_2.clear_list()
ll_2.insert_values(clients)
ll_2.print()
t_2 = 0
If_A = 1
If_B = 1
If_C = 1
If_ll_2 = 1

while office_2 != [0, 0, 0, 0, 0, 0, 0, 0, 0]:
    if If_ll_2 == 1:
        if If_A == 1:
            for x in range(0, 3):
                curr = ll_2.head
                if curr is None:
                    If_ll_2 == 0
                    break
                if office_2[x] == "A" or office_2[x] == 0:
                    while curr.data[0] != "A":
                        curr = curr.next
                        if curr is None:
                            If_A = 0
                            break
                    else:
                        office_2[x] = int(curr.data[1:])
                        If_A = 1
                        k = ll_2.get_index(curr.data)
                        ll_2.remove_at(k)
        if If_B == 1:
            for x in range(3, 6):
                curr = ll_2.head
                if curr is None:
                    If_ll_2 == 0
                    break
                if office_2[x] == "B" or office_2[x] == 0:
                    while curr.data[0] != "B":
                        curr = curr.next
                        if curr is None:
                            If_B = 0
                            break
                    else:
                        office_2[x] = int(curr.data[1:])
                        If_B = 1
                        k = ll_2.get_index(curr.data)
                        ll_2.remove_at(k)
        if If_C == 1:
            for x in range(6, 9):
                curr = ll_2.head
                if curr is None:
                    If_ll_2 == 0
                    break
                if office_2[x] == "C" or office_2[x] == 0:
                    while curr.data[0] != "C":
                        curr = curr.next
                        if curr is None:
                            If_C = 0
                            break
                    else:
                        office_2[x] = int(curr.data[1:])
                        If_C = 1
                        k = ll_2.get_index(curr.data)
                        ll_2.remove_at(k)
    office_2 = [x - 1 if x > 0 else 0 for x in office_2]
    t_2 += 1
print(f"Czas trwania: {t_2}")

office_3 = ["A", "A", "B", "B", "C", "C", "E", "E", "E"]
ll_3.clear_list()
ll_3.insert_values(clients)
ll_3.print()
t_3 = 0
If_A = 1
If_B = 1
If_C = 1
If_LL = 1

while office_3 != [0, 0, 0, 0, 0, 0, 0, 0, 0]:
    if If_LL == 1:
        if If_A == 1:
            for x in range(0, 2):
                curr = ll_3.head
                if curr is None:
                    If_LL == 0
                    break
                if office_3[x] == "A" or office_3[x] == 0:
                    while curr.data[0] != "A":
                        curr = curr.next
                        if curr is None:
                            If_A = 0
                            break
                    else:
                        office_3[x] = int(curr.data[1:])
                        If_A = 1
                        k = ll_3.get_index(curr.data)
                        ll_3.remove_at(k)
        if If_B == 1:
            for x in range(2, 4):
                curr = ll_3.head
                if curr is None:
                    If_LL == 0
                    break
                if office_3[x] == "B" or office_3[x] == 0:
                    while curr.data[0] != "B":
                        curr = curr.next
                        if curr is None:
                            If_B = 0
                            break
                    else:
                        office_3[x] = int(curr.data[1:])
                        If_B = 1
                        k = ll_3.get_index(curr.data)
                        ll_3.remove_at(k)
        if If_C == 1:
            for x in range(4, 6):
                curr = ll_3.head
                if curr is None:
                    If_LL == 0
                    break
                if office_3[x] == "C" or office_3[x] == 0:
                    while curr.data[0] != "C":
                        curr = curr.next
                        if curr is None:
                            If_C = 0
                            break
                    else:
                        office_3[x] = int(curr.data[1:])
                        If_C = 1
                        k = ll_3.get_index(curr.data)
                        ll_3.remove_at(k)
        for x in range(6, 9):
            curr = ll_3.head
            if curr is None:
                If_LL == 0
                break
            if office_3[x] == "E" or office_3[x] == 0:
                office_3[x] = int(curr.data[1:])
                k = ll_3.get_index(curr.data)
                ll_3.remove_at(k)
    office_3 = [x - 1 if x > 0 else 0 for x in office_3]
    t_3 += 1
print(f"czas trwania {t_3}")

office_4 = ["A", "B", "B", "C", "C", "C", "E"]
ll_4.clear_list()
ll_4.insert_values(clients)
ll_4.print()
t_4 = 0
If_A = 1
If_B = 1
If_C = 1
If_LL = 1

while office_4 != [0, 0, 0, 0, 0, 0, 0]:
    if If_LL == 1:
        if If_A == 1:
            for x in range(0, 1):
                curr = ll_4.head
                if curr is None:
                    If_LL == 0
                    break
                if office_4[x] == "A" or office_4[x] == 0:
                    while curr.data[0] != "A":
                        curr = curr.next
                        if curr is None:
                            If_A = 0
                            break
                    else:
                        office_4[x] = int(curr.data[1:])
                        If_A = 1
                        k = ll_4.get_index(curr.data)
                        ll_4.remove_at(k)
        if If_B == 1:
            for x in range(1, 3):
                curr = ll_4.head
                if curr is None:
                    If_LL == 0
                    break
                if office_4[x] == "B" or office_4[x] == 0:
                    while curr.data[0] != "B":
                        curr = curr.next
                        if curr is None:
                            If_B = 0
                            break
                    else:
                        office_4[x] = int(curr.data[1:])
                        If_B = 1
                        k = ll_4.get_index(curr.data)
                        ll_4.remove_at(k)
        if If_C == 1:
            for x in range(3, 6):
                curr = ll_4.head
                if curr is None:
                    If_LL == 0
                    break
                if office_4[x] == "C" or office_4[x] == 0:
                    while curr.data[0] != "C":
                        curr = curr.next
                        if curr is None:
                            If_C = 0
                            break
                    else:
                        office_4[x] = int(curr.data[1:])
                        If_C = 1
                        k = ll_4.get_index(curr.data)
                        ll_4.remove_at(k)
        for x in range(6, 7):
            curr = ll_4.head
            if curr is None:
                If_LL == 0
                break
            if office_4[x] == "E" or office_4[x] == 0:
                office_4[x] = int(curr.data[1:])
                k = ll_4.get_index(curr.data)
                ll_4.remove_at(k)
    office_4 = [x - 1 if x > 0 else 0 for x in office_4]
    t_4 += 1
print(f"czas trwania {t_4}")
#zad2 iii
office = ["A", "A", "A", "B", "B", "B", "C", "C", "C", "E"]
office_3 = ["A", "A", "B", "B", "C", "C", "E", "E", "E"]
office_4 = ["A", "B", "B", "C", "C", "C", "E"]
office_2 = ["A", "A", "A", "B", "B", "B", "C", "C", "C"]
tasks = ["A1", "A2", "A3", "A4", "B5", "B6", "B7", "B8", "C9", "C11", "C12"]
clients = []
data = [0 for x in range(4)]
ll = LinkedList()
ll_2 = LinkedList()
ll_3 = LinkedList()
ll_4 = LinkedList()
first_office_times = []
second_office_times = []
third_office_times = []
fourth_office_times = []
t, t_2, t_3, t_4 = 0, 0,0 , 0
for d in range(100):
    T = 0
    clients.clear()
    ll.clear_list()
    ll_2.clear_list()
    ll_3.clear_list()
    ll_4.clear_list()
    for i in range(100):
        x = r.choice(tasks)
        clients.append(x)
    ll.insert_values(clients)
    office = ["A", "A", "A", "B", "B", "B", "C", "C", "C", "E"]
    If_A = 1
    If_B = 1
    If_C = 1
    If_LL = 1
    New_A = 0
    New_B = 0
    New_C = 0
    while office != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
        if If_LL == 1:
            if If_A == 1:
                for x in range(0, 3):
                    curr = ll.head
                    if curr is None:
                        If_LL == 0
                        break
                    if office[x] == "A" or office[x] == 0:
                        while curr.data[0] != "A":
                            curr = curr.next
                            if curr is None:
                                If_A = 0
                                break
                        else:
                            office[x] = int(curr.data[1:])
                            If_A = 1
                            k = ll.get_index(curr.data)
                            ll.remove_at(k)
            if If_B == 1:
                for x in range(3, 6):
                    curr = ll.head
                    if curr is None:
                        If_LL == 0
                        break
                    if office[x] == "B" or office[x] == 0:
                        while curr.data[0] != "B":
                            curr = curr.next
                            if curr is None:
                                If_B = 0
                                break
                        else:
                            office[x] = int(curr.data[1:])
                            If_B = 1
                            k = ll.get_index(curr.data)
                            ll.remove_at(k)
            if If_C == 1:
                for x in range(6, 9):
                    curr = ll.head
                    if curr is None:
                        If_LL == 0
                        break
                    if office[x] == "C" or office[x] == 0:
                        while curr.data[0] != "C":
                            curr = curr.next
                            if curr is None:
                                If_C = 0
                                break
                        else:
                            office[x] = int(curr.data[1:])
                            If_C = 1
                            k = ll.get_index(curr.data)
                            ll.remove_at(k)
            for x in range(9, 10):
                curr = ll.head
                if curr is None:
                    If_LL == 0
                    break
                if office[x] == "E" or office[x] == 0:
                    office[x] = int(curr.data[1:])
                    k = ll.get_index(curr.data)
                    ll.remove_at(k)
        office = [x - 1 if x > 0 else 0 for x in office]
        t += 1
        T += 1
    first_office_times.append(T)
    print(f"czas trwania {t}")

    office_2 = ["A", "A", "A", "B", "B", "B", "C", "C", "C"]
    ll_2.insert_values(clients)
    ll_2.print()
    If_A_2 = 1
    If_B_2 = 1
    If_C_2 = 1
    If_ll_2 = 1
    New_A = 0
    New_B = 0
    New_C = 0
    T = 0
    while office_2 != [0, 0, 0, 0, 0, 0, 0, 0, 0]:
        if If_ll_2 == 1:
            if If_A_2 == 1:
                for x in range(0, 3):
                    curr = ll_2.head
                    if curr is None:
                        If_ll_2 == 0
                        break
                    if office_2[x] == "A" or office_2[x] == 0:
                        while curr.data[0] != "A":
                            curr = curr.next
                            if curr is None:
                                If_A_2 = 0
                                break
                        else:
                            office_2[x] = int(curr.data[1:])
                            If_A_2 = 1
                            k = ll_2.get_index(curr.data)
                            ll_2.remove_at(k)
            if If_B_2 == 1:
                for x in range(3, 6):
                    curr = ll_2.head
                    if curr is None:
                        If_ll_2 == 0
                        break
                    if office_2[x] == "B" or office_2[x] == 0:
                        while curr.data[0] != "B":
                            curr = curr.next
                            if curr is None:
                                If_B_2 = 0
                                break
                        else:
                            office_2[x] = int(curr.data[1:])
                            If_B_2 = 1
                            k = ll_2.get_index(curr.data)
                            ll_2.remove_at(k)
            if If_C_2 == 1:
                for x in range(6, 9):
                    curr = ll_2.head
                    if curr is None:
                        If_ll_2 == 0
                        break
                    if office_2[x] == "C" or office_2[x] == 0:
                        while curr.data[0] != "C":
                            curr = curr.next
                            if curr is None:
                                If_C_2 = 0
                                break
                        else:
                            office_2[x] = int(curr.data[1:])
                            If_C_2 = 1
                            k = ll_2.get_index(curr.data)
                            ll_2.remove_at(k)
        office_2 = [x - 1 if x > 0 else 0 for x in office_2]
        t_2 += 1
        T += 1
    second_office_times.append(T)
    print(f"Czas trwania: {t_2}")

    office_3 = ["A", "A", "B", "B", "C", "C", "E", "E", "E"]

    ll_3.insert_values(clients)
    ll_3.print()
    If_A_3 = 1
    If_B_3 = 1
    If_C_3 = 1
    If_LL_3 = 1
    New_A = 0
    New_B = 0
    New_C = 0
    T = 0
    while office_3 != [0, 0, 0, 0, 0, 0, 0, 0, 0]:
        if If_LL_3 == 1:
            if If_A_3 == 1:
                for x in range(0, 2):
                    curr = ll_3.head
                    if curr is None:
                        If_LL_3 == 0
                        break
                    if office_3[x] == "A" or office_3[x] == 0:
                        while curr.data[0] != "A":
                            curr = curr.next
                            if curr is None:
                                If_A_3 = 0
                                break
                        else:
                            office_3[x] = int(curr.data[1:])
                            If_A_3 = 1
                            k = ll_3.get_index(curr.data)
                            ll_3.remove_at(k)
            if If_B_3 == 1:
                for x in range(2, 4):
                    curr = ll_3.head
                    if curr is None:
                        If_LL_3 == 0
                        break
                    if office_3[x] == "B" or office_3[x] == 0:
                        while curr.data[0] != "B":
                            curr = curr.next
                            if curr is None:
                                If_B_3 = 0
                                break
                        else:
                            office_3[x] = int(curr.data[1:])
                            If_B_3 = 1
                            k = ll_3.get_index(curr.data)
                            ll_3.remove_at(k)
            if If_C_3 == 1:
                for x in range(4, 6):
                    curr = ll_3.head
                    if curr is None:
                        If_LL_3 == 0
                        break
                    if office_3[x] == "C" or office_3[x] == 0:
                        while curr.data[0] != "C":
                            curr = curr.next
                            if curr is None:
                                If_C_3 = 0
                                break
                        else:
                            office_3[x] = int(curr.data[1:])
                            If_C_3 = 1
                            k = ll_3.get_index(curr.data)
                            ll_3.remove_at(k)
            for x in range(6, 9):
                curr = ll_3.head
                if curr is None:
                    If_LL_3 == 0
                    break
                if office_3[x] == "E" or office_3[x] == 0:
                    office_3[x] = int(curr.data[1:])
                    k = ll_3.get_index(curr.data)
                    ll_3.remove_at(k)
        office_3 = [x - 1 if x > 0 else 0 for x in office_3]
        t_3 += 1
        T += 1
    third_office_times.append(T)
    print(f"czas trwania {t_3}")

    office_4 = ["A", "B", "B", "C", "C", "C", "E"]

    ll_4.insert_values(clients)
    ll_4.print()
    If_A_4 = 1
    If_B_4 = 1
    If_C_4 = 1
    If_LL_4 = 1
    New_A = 0
    New_B = 0
    New_C = 0
    T = 0
    while office_4 != [0, 0, 0, 0, 0, 0, 0]:
        if If_LL_4 == 1:
            if If_A_4 == 1:
                for x in range(0, 1):
                    curr = ll_4.head
                    if curr is None:
                        If_LL_4 == 0
                        break
                    if office_4[x] == "A" or office_4[x] == 0:
                        while curr.data[0] != "A":
                            curr = curr.next
                            if curr is None:
                                If_A_4 = 0
                                break
                        else:
                            office_4[x] = int(curr.data[1:])
                            If_A_4 = 1
                            k = ll_4.get_index(curr.data)
                            ll_4.remove_at(k)
            if If_B_4 == 1:
                for x in range(1, 3):
                    curr = ll_4.head
                    if curr is None:
                        If_LL_4 == 0
                        break
                    if office_4[x] == "B" or office_4[x] == 0:
                        while curr.data[0] != "B":
                            curr = curr.next
                            if curr is None:
                                If_B_4 = 0
                                break
                        else:
                            office_4[x] = int(curr.data[1:])
                            If_B_4 = 1
                            k = ll_4.get_index(curr.data)
                            ll_4.remove_at(k)
            if If_C_4 == 1:
                for x in range(3, 6):
                    curr = ll_4.head
                    if curr is None:
                        If_LL_4 == 0
                        break
                    if office_4[x] == "C" or office_4[x] == 0:
                        while curr.data[0] != "C":
                            curr = curr.next
                            if curr is None:
                                If_C_4 = 0
                                break
                        else:
                            office_4[x] = int(curr.data[1:])
                            If_C_4 = 1
                            k = ll_4.get_index(curr.data)
                            ll_4.remove_at(k)
            for x in range(6, 7):
                curr = ll_4.head
                if curr is None:
                    If_LL_4 == 0
                    break
                if office_4[x] == "E" or office_4[x] == 0:
                    office_4[x] = int(curr.data[1:])
                    k = ll_4.get_index(curr.data)
                    ll_4.remove_at(k)
        office_4 = [x - 1 if x > 0 else 0 for x in office_4]
        t_4 += 1
        T += 1
    fourth_office_times.append(T)
    print(f"czas trwania {t_4}")
data[0] = t
data[1] = t_2
data[2] = t_3
data[3] = t_4
data = list(map(lambda x : x/100, data))
print("Średnie czasy:", *data)


plt.hist(first_office_times, color='green', alpha=0.5)
plt.hist(second_office_times, color='orange', alpha=0.5)
plt.hist(third_office_times, color='red', alpha=0.5)
plt.hist(fourth_office_times, color='blue', alpha=0.5)

plt.xlabel('time')
plt.ylabel('frequency')
plt.show()
#2 iiii)
"""
Okienka "E" skracają czas obsługi klientów.
"""
#zad2 iiiii)

office = ["A", "A", "A", "B", "B", "B", "C", "C", "C", "E"]
tasks = ["A1", "A2", "A3", "A4", "B5", "B6", "B7", "B8", "C9", "C11", "C12"]
clients = []
for i in range(40):
    x = r.choice(tasks)
    clients.append(x)
sorted_clients = sorted(clients, key=lambda x: int(str(x)[1:]))

ll = LinkedList()
ll.insert_values(clients)
ll.print()
t = 0
If_A = 1
If_B = 1
If_C = 1
If_LL = 1
clients_served = [0 for x in range(10)]
while office != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
    if If_LL == 1:
        if If_A == 1:
            for x in range(0, 3):
                curr = ll.head
                if curr is None:
                    If_LL == 0
                    break
                if office[x] == "A" or office[x] == 0:
                    while curr.data[0] != "A":
                        curr = curr.next
                        if curr is None:
                            If_A = 0
                            break
                    else:
                        office[x] = int(curr.data[1:])
                        If_A = 1
                        k = ll.get_index(curr.data)
                        ll.remove_at(k)
                if office[x] == 1:
                    clients_served[x] += 1
        if If_B == 1:
            for x in range(3, 6):
                curr = ll.head
                if curr is None:
                    If_LL == 0
                    break
                if office[x] == "B" or office[x] == 0:
                    while curr.data[0] != "B":
                        curr = curr.next
                        if curr is None:
                            If_B = 0
                            break
                    else:
                        office[x] = int(curr.data[1:])
                        If_B = 1
                        k = ll.get_index(curr.data)
                        ll.remove_at(k)
                if office[x] == 1:
                    clients_served[x] += 1
        if If_C == 1:
            for x in range(6, 9):
                curr = ll.head
                if curr is None:
                    If_LL == 0
                    break
                if office[x] == "C" or office[x] == 0:
                    while curr.data[0] != "C":
                        curr = curr.next
                        if curr is None:
                            If_C = 0
                            break
                    else:
                        office[x] = int(curr.data[1:])
                        If_C = 1
                        k = ll.get_index(curr.data)
                        ll.remove_at(k)
                if office[x] == 1:
                    clients_served[x] += 1
        for x in range(9, 10):
            curr = ll.head
            if curr is None:
                If_LL == 0
                break
            if office[x] == "E" or office[x] == 0:
                office[x] = int(curr.data[1:])
                k = ll.get_index(curr.data)
                ll.remove_at(k)
            if office[x] == 1:
                clients_served[x] += 1
    office = [x - 1 if x > 0 else 0 for x in office]
    t += 1
print(f"czas trwania {t}")
sorted_clients = sorted(clients, key=lambda x: int(str(x)[1:]))
office = ["A", "A", "A", "B", "B", "B", "C", "C", "C", "E"]
ll = LinkedList()
ll.insert_values(sorted_clients)
ll.print()
t = 0
If_A = 1
If_B = 1
If_C = 1
If_LL = 1
clients_served = [0 for x in range(10)]
while office != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
    if If_LL == 1:
        if If_A == 1:
            for x in range(0, 3):
                curr = ll.head
                if curr is None:
                    If_LL == 0
                    break
                if office[x] == "A" or office[x] == 0:
                    while curr.data[0] != "A":
                        curr = curr.next
                        if curr is None:
                            If_A = 0
                            break
                    else:
                        office[x] = int(curr.data[1:])
                        If_A = 1
                        k = ll.get_index(curr.data)
                        ll.remove_at(k)
                if office[x] == 1:
                    clients_served[x] += 1
        if If_B == 1:
            for x in range(3, 6):
                curr = ll.head
                if curr is None:
                    If_LL == 0
                    break
                if office[x] == "B" or office[x] == 0:
                    while curr.data[0] != "B":
                        curr = curr.next
                        if curr is None:
                            If_B = 0
                            break
                    else:
                        office[x] = int(curr.data[1:])
                        If_B = 1
                        k = ll.get_index(curr.data)
                        ll.remove_at(k)
                if office[x] == 1:
                    clients_served[x] += 1
        if If_C == 1:
            for x in range(6, 9):
                curr = ll.head
                if curr is None:
                    If_LL == 0
                    break
                if office[x] == "C" or office[x] == 0:
                    while curr.data[0] != "C":
                        curr = curr.next
                        if curr is None:
                            If_C = 0
                            break
                    else:
                        office[x] = int(curr.data[1:])
                        If_C = 1
                        k = ll.get_index(curr.data)
                        ll.remove_at(k)
                if office[x] == 1:
                    clients_served[x] += 1
        for x in range(9, 10):
            curr = ll.head
            if curr is None:
                If_LL == 0
                break
            if office[x] == "E" or office[x] == 0:
                office[x] = int(curr.data[1:])
                k = ll.get_index(curr.data)
                ll.remove_at(k)
            if office[x] == 1:
                clients_served[x] += 1
    office = [x - 1 if x > 0 else 0 for x in office]
    t += 1
print(f"czas trwania {t}")

"""
Po przperowadzeniu paru prób czasowych dla kolejek posortowanych oraz nie, stwierdzam,
że sortowanie nic nie zmienia w kwesti zmniejszenia czasu.
"""
#zad2 iiiiii)
"""
Dodanie więcej okienek "E" oraz dawanie okienku więcej zadań typu "C" ponieważ te zadania wymagają dużo czasu.
Większość kolejek kończyła się szybko przy okienkach "A" a okienka "C" wyznaczały koniec obsługi.
Takie rozwiązanie skróciło by znacznie czas obsługi.
"""




