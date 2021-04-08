class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def insert(root, x):
    if root == None:
        return Node(x)
    if (x < root.data):
        root.left = insert(root.left, x)
    elif (x > root.data):
        root.right = insert(root.right, x)
    return root
def serialize(root):
    ans=[]
    def serializer(root):
        if root==None:
            ans.append('-1')
        else:
            ans.append(str(root.data))
            serializer(root.left)
            serializer(root.right)
    serializer(root)
    return ','.join(ans)
def deserialize(s):
    a=iter(s.split(','))
    def deserializer():
        temp=next(a)
        if temp=='-1':
            return None
        else:
            root=Node(int(temp))
            root.left=deserializer()
            root.right=deserializer()
            return root
    return deserializer()
n = int(input())
arr = list(map(int, input().split()))
root = None
for i in range(n):
    root = insert(root, arr[i])
s1=serialize(root)
print(s1)
s2=serialize(deserialize(s1))
print(s2)
assert s1==s2



