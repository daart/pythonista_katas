# import heapq

# k = 10
# buffer = [numbers[:k]]  # heap
# heapq.heapify(buffer)  # O(log(k))

# for n in numbers[k:]:  # O(n)
#     if n > buffer[0]:  # O(1)
#         heapq.heappop(buffer, buffer[0])  # O(log(k))
#         heapq.heappush(buffer, n)  # O(log(k))

# return buffer[0]  # O(n * log(k))


# buffer plain list
# k = 10
# log(n) > k

# implement using self class MinHeap
# advanced** knowing that the sequence is integers means pow(2, 32)


class MinHeap:
    def __init__(self, list):
        self._size = len(list)  # current el
        self._heap = [0] * self._size  # fill empty list with zeros

    def getLeftChildIndex(self, parentIndex):
        return (parentIndex * 2) + 1

    def getRightChildIndex(self, parentIndex):
        return (parentIndex * 2) + 2

    def getParentIndex(self, childIndex):
        return (childIndex - 1) // 2

    def hasLeftChild(self):
        return self.getLeftchildIndex() < self._size

    def hasRightChild(self):
        return self.getRightchildIndex() < self._size

    def hasParent(self):
        return getParentIndex >= 0

    def leftChild(self, leftChildIndex):
        return self._heap[getLeftChildIndex(leftChildIndex)]

    def rightChild(self, rightChildIndex):
        return self._heap[getRightChildIndex(rightChildIndex)]

    def parent(self, parentIndex):
        return self._heap[getParentIndex(parentIndex)]

    def swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def ensureExtraCapacity(self):
        if self._size == self._capacity:
            self._heap = self._heap + [0] * self._capacity

    def peak(self):
        if self._size == 0:
            print('Error, ')
        return self._heap[0]

    def pop(self):
        if self._size == 0:
            print('Error, ')

        item = self.peak()
        self._heap[0] = self._heap[self._size - 1]
        self._size -= 1
        self.bubbleUp()
        return item

    def insert(self, new_node):
        self._heap.append(new_node)
        self.bubbleDown()

    def bubbleUp(self):
        index = self._size - 1
        while self.hasParent() and self.parent(index) > self._heap[index]:
            self._swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)

    def bubbleDown(self):
        index = 0
        while self.hasLeftChild(index):
            smallerChildIndex = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.getRightChildIndex(index) < self.leftChild(index):
                smallerChildIndex = self.getRightChildIndex(index)

            if self._heap[index] < self._heap[smallerChildIndex]:
                break
            else:
                self.swap(index, smallerChildIndex)
                index = smallerChildIndex

    def heapify(self):
        
        return self._heap


def kth_largest(numbers, k):
    """
    See https://leetcode.com/problems/kth-largest-element-in-an-array/
    >>> kth_largest([3, 2, 1, 5, 6, 4], 2)
    5
    >>> kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    4
    >>> kth_largest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)
    9
    >>> kth_largest([10, 9, 5, 6, 4, 7, 2, 1, 3, 8], 3)
    8
    """

    res = [0] * k
    min = 0
    # how to fill the list when it's empty
    # temp min value
    # how to switch prev min element with the new min
