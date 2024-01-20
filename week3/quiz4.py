class SinLinkedList:
    # 节点的数据结构，包含一个值和一个指针
    class Node:
        __slots__ = {'_element', '_next'}

        def __init__(self, element):
            self._element = element
            self._next = None

    # head表示头节点，tail用于尾插法
    # 初始化时头节点的值设置为空，头节点的下一个也是空
    def __init__(self):
        self._head = self.Node(None)
        self._tail = self._head
        self._size = 0

    def is_empty(self):
        return self._size == 0

    # 头插法创建链表，输出的数是输入的逆序
    # 头插法就是将数据始终插入头节点后面
    def add_node_head(self, e):
        Node = self.Node(e)
        Node._next = self._head._next
        self._head._next = Node
        self._size += 1

        return self._head

    # 尾插法创建链表，输出的数是输入的逆序
    # 头插法就是将数据始终插入头节点后面
    def add_node_tail(self, e):
        Node = self.Node(e)
        self._tail._next = Node
        self._tail = Node
        self._size += 1

        return self._tail

    # 删除链表的某一个元素
    # 删除元素，需要知道至少两个节点指针，这样才能将所删元素跳过
    def remove_node(self, e):
        pre_node = self._head
        now_node = self._head._next
        while now_node is not None:
            if now_node._element == e:
                pre_node._next = now_node._next
                now_node = pre_node._next
            else:
                pre_node = now_node
                now_node = now_node._next

    # 查找节点是否存在，存在返回True，不存在返回False
    def search_node(self, e):
        now_node = self._head
        while now_node._next is not None:
            if now_node._next._element == e:
                return True
            now_node = now_node._next
        return False

    # 输出链表节点
    # 如论何时，链表最好保持头节点指针不动，所以下面now_node = self._head
    def print_link_node(self):
        now_node = self._head
        while now_node._next is not None:
            print(now_node._next._element, end='-->')
            now_node = now_node._next
        print('None')

link = SinLinkedList()


def create_link_head():
    for i in range(0, 6):
        link.add_node_head(i)


def create_link_tail():
    for i in range(0, 6):
        link.add_node_tail(i)


if __name__ == '__main__':
    # create_link_head()
    # 尾插入创建链表
    create_link_tail()
    link.print_link_node()
    # 删除链表的节点值为4的节点
    link.remove_node(4)
    link.print_link_node()
    # 查找节点值为5的节点是否存在
    print(link.search_node(5))