class Node:
    """이진 트리 노드를 나타내는 클래스"""

    def __init__(self, data):
        """이진 트리 노드는 데이터와 두 자식 노드에 대한 레퍼런스를 갖는다"""
        self.data = data
        self.left_child = None
        self.right_child = None


def traverse_inorder(node):
    """in-order 순회 함수"""
    if node is not None:
        # 왼쪽 자식 순회
        traverse_inorder(node.left_child)

        # 뿌리 노드 순회
        print(node.data)

       # 오른쪽 자식 순회
        traverse_inorder(node.right_child)


# 여러 노드 인스턴스 생성
node_A = Node("A")
node_B = Node("B")
node_C = Node("C")
node_D = Node("D")
node_E = Node("E")
node_F = Node("F")
node_G = Node("G")
node_H = Node("H")
node_I = Node("I")

# 생성한 노드 인스턴스들 연결
node_F.left_child = node_B  # type: ignore
node_F.right_child = node_G  # type: ignore

node_B.left_child = node_A  # type: ignore
node_B.right_child = node_D  # type: ignore

node_D.left_child = node_C  # type: ignore # type: ignore
node_D.right_child = node_E  # type: ignore

node_G.right_child = node_I  # type: ignore

node_I.left_child = node_H  # type: ignore

# 노드 F를 root 노드로 만든다
root_node = node_F

# 만들어 놓은 트리를 in-order로 순회한다
traverse_inorder(root_node)
