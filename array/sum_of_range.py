from math import log2, ceil


class SegmentTree:
    def __init__(self, array):
        self.size = len(array)
        # Height of segment tree
        height = int(ceil(log2(self.size)))

        # Maximum size of segment tree
        max_size = 2 * (int)(2 ** height) - 1

        # Allocate memory
        self.tree = [0] * max_size
        # fill the allocated memory tree
        self.build_tree(array, 0, 0, self.size - 1)

    def build_tree(self, array, tree_index, left, right):
        if left == right:
            self.tree[tree_index] = array[left]
            return array[left]

        mid = (left + right) // 2
        self.tree[tree_index] = self.build_tree(array, 2 * tree_index + 1, left, mid) + \
                                self.build_tree(array, 2 * tree_index + 2, mid + 1, right)
        return self.tree[tree_index]

    def get_sum(self, tree_index, left, right, q_start, q_end):
        if q_start < 0 or q_end > self.size or q_start > q_end:
            return -1
        if left < q_start or right > q_end:
            return 0
        if q_start <= left and q_end >= right:
            return self.tree[tree_index]
        mid = (left + right) // 2
        return self.get_sum(2 * tree_index + 1, left, mid, q_start, q_end) + \
               self.get_sum(2 * tree_index + 2, mid + 1, right, q_start, q_end)


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(arr)
    print(st.get_sum(0, 0, len(arr) - 1, 1, 3))
