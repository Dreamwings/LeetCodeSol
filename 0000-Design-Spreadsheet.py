"""
Question:
Design a spreadsheet like object using Python. It has a max of 1000 rows and columns. 
You can insert or delete one or more empty rows or cols. It has a limited memory.

It's an interview question from MSFT:
https://leetcode.com/discuss/interview-question/1975081/Microsoft-Round-2-LLD-question

Some data structures might be relevant:

Linked List
https://stackoverflow.com/questions/66405955/best-datastructure-to-implement-excel-spreadsheet

Sparse Matrix:
https://www.javatpoint.com/sparse-matrix

B+ Tree:
https://www.javatpoint.com/b-plus-tree

"""


# ===================================================================
# To get optimal time complexity with O(1), we need to give the following prompt to ChatGPT:
# ===================================================================
"""
Design a spreadsheet like object using Python. It has a max of 1000 rows and columns. 
You can insert or delete one or more empty rows or cols. It has a limited memory. 
Use double linked list with O(1) time complexity
"""


class Node:
    def __init__(self, index):
        self.index = index
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, index):
        new_node = Node(index)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, node):
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev


class SparseSpreadsheet:
    def __init__(self):
        self.rows = LinkedList()
        self.cols = LinkedList()
        self.data = {}

    def insert_rows(self, row_index, num_rows):
        if row_index < 0 or row_index > 1000 or row_index + num_rows > 1000:
            raise ValueError("Invalid row index or number of rows")

        for i in range(row_index, row_index + num_rows):
            self.rows.insert(i)

    def delete_rows(self, row_index, num_rows):
        if row_index < 0 or row_index >= 1000 or row_index + num_rows > 1000:
            raise ValueError("Invalid row index or number of rows")

        for i in range(row_index, row_index + num_rows):
            node = self.rows.head
            while node:
                next_node = node.next
                if node.index == i:
                    self.rows.delete(node)
                    for col in range(len(self.cols)):
                        if (i, col) in self.data:
                            del self.data[(i, col)]
                    break
                node = next_node

    def insert_cols(self, col_index, num_cols):
        if col_index < 0 or col_index > 1000 or col_index + num_cols > 1000:
            raise ValueError("Invalid column index or number of columns")

        for i in range(col_index, col_index + num_cols):
            self.cols.insert(i)

    def delete_cols(self, col_index, num_cols):
        if col_index < 0 or col_index >= 1000 or col_index + num_cols > 1000:
            raise ValueError("Invalid column index or number of columns")

        for i in range(col_index, col_index + num_cols):
            node = self.cols.head
            while node:
                next_node = node.next
                if node.index == i:
                    self.cols.delete(node)
                    for row in range(len(self.rows)):
                        if (row, i) in self.data:
                            del self.data[(row, i)]
                    break
                node = next_node

    def set_value(self, row, col, value):
        if row not in range(len(self.rows)) or col not in range(len(self.cols)):
            raise ValueError("Row or column index out of range")

        self.data[(row, col)] = value

    def get_value(self, row, col):
        if row not in range(len(self.rows)) or col not in range(len(self.cols)):
            raise ValueError("Row or column index out of range")

        return self.data.get((row, col), None)


# Example usage:
spreadsheet = SparseSpreadsheet()
spreadsheet.insert_rows(0, 3)
spreadsheet.insert_cols(0, 2)
spreadsheet.set_value(0, 0, "Hello")
spreadsheet.set_value(1, 1, "World")
print(spreadsheet.get_value(0, 0))  # Output: Hello
print(spreadsheet.get_value(1, 1))  # Output: World
spreadsheet.delete_rows(0, 2)
spreadsheet.delete_cols(0, 1)

