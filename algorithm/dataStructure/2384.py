def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def reverse_heapify(tree, index):
    """삽입된 노드를 힙 속성을 지키는 위치로 이동시키는 함수"""
    tree_size = len(tree)

    if index == 0:
        return

    parent_index = index // 2  # 삽입된 노드의 부모 노드의 인덱스 계산
    if 0 < parent_index < tree_size:
        if tree[parent_index] < tree[index]:
            swap(tree, parent_index, index)
            reverse_heapify(tree, parent_index)


class PriorityQueue:
    """힙으로 구현한 우선순위 큐"""

    def __init__(self):
        self.heap = [None]  # 파이썬 리스트로 구현한 힙

    def insert(self, data):
        """삽입 메소드"""
        self.heap.append(data)
        index_of_data = len(self.heap)-1
        reverse_heapify(self.heap, index_of_data)

    def __str__(self):
        return str(self.heap)


# 테스트 코드
priority_queue = PriorityQueue()

priority_queue.insert(6)
priority_queue.insert(9)
priority_queue.insert(1)
priority_queue.insert(3)
priority_queue.insert(10)
priority_queue.insert(11)
priority_queue.insert(13)

print(priority_queue)
