class Node:
    def __init__(self, value, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev
    def __str__(self):
        return str(self.value)
class LinkedList:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur = self.head
        ans = ''
        while cur.next != None:
            ans += str(cur.value) + ' -> '
            cur = cur.next
        ans += str(cur.value)
        return ans
    def isEmpty(self):
        return self.head == None
    def append(self, value):
        if self.isEmpty():
            self.head = self.tail = Node(value)
        else:
            self.tail.next = new_node = Node(value, None, self.tail)
            self.tail = new_node
    def addHead(self, value):
        if self.isEmpty():
            self.head = self.tail = Node(value)
        else:
            self.head.prev = new_node = Node(value, self.head, None)
            self.head = new_node
    def size(self):
        cur = self.head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count
    def pop_head(self):
        return_node = self.head
        self.head = self.head.next
        return return_node.value
    
history = {}
nodes = {}
inp = input("Enter edges: ").split(",")
for i in inp:
    data1 = int(i.split(">")[0])
    data2 = int(i.split(">")[1])
    
    if data1 not in nodes.keys():
        fnode = Node(data1)
        nodes[data1] = fnode
    else:
        fnode = nodes[data1]

    if data2 not in nodes.keys():
        snode = Node(data2)
        nodes[data2] = snode
    else:
        snode = nodes[data2]

    fnode.next = snode

    if fnode not in history.keys():
        history.update({fnode:0})
    
    if snode not in history.keys():
        history.update({snode:1})
    else:
        history.update({snode:history[snode] + 1})

heads = []
targets = []
traget_size = {}
for node in nodes.values():
    if history[node] >= 2:
        target = node
        targets.append(target)
        visited = []
        cnt = 0
        curr = target
        while curr != None and curr not in visited:
            cnt += 1
            visited.append(curr)
            curr = curr.next
        traget_size[target] = cnt

for target in targets:
    if target != None and target.next != None :
        history.update({target.next:history[target.next] - 1})

for node in nodes.values():
    if node.next in targets:
        node.next = None
    if history[node] == 0:
        heads.append(node)

List_ll = [LinkedList(head=head) for head in heads]

List_ll.sort(key=lambda LL: LL.head.value )

answer = LinkedList()

rounds = 0
for ll in List_ll:
    # print(ll)
    rounds = max(rounds,ll.size())

for i in range(rounds):
    for ll in List_ll:
        if not ll.isEmpty():
            answer.append(ll.pop_head())

if len(targets) == 0 or answer.isEmpty():
    print("No intersection")
else:
    targets.sort(key=lambda target: target.value)
    for target in targets:
        print(f"Node({target}, size={traget_size[target]})")
    print("Delete intersection then swap merge:")
    print(answer)