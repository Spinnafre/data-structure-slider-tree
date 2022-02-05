from abc import ABC, abstractmethod


class TreeADT(ABC):

    @abstractmethod
    def insert(self, value):
        """Insere <value> na Ã¡rvore"""
        pass

    @abstractmethod
    def empty(self):
        """Verifica se a Ã¡rvore estÃ¡ vazia"""
        pass

    @abstractmethod
    def root(self):
        """Retorna o nÃ³ raiz da Ã¡rvore"""
        pass


class Node:

    def __init__(self, data=None, parent=None, left=None, right=None):
        self._data = data
        self._parent = parent
        self._left = left
        self._right = right

    def empty(self):
        return not self._data

    def __str__(self):
        return self._data.__str__()


class BinaryTree(TreeADT):

    def __init__(self, data=None):
        self._root = Node(data)

        #           root(11,_,9,15)
        #   node(9,11,_,_)      node(15,11,_,_)
        # node(8,9,_,_)     node(13,15,_,_)  node(18,15,_,_)


    def empty(self):
        return not self._root._data

    def root(self):
        return self._root

    def insert(self, elem): # 18
        node = Node(elem) # node(18,_,_,_)
        if self.empty():
            self._root = node
        else:
            self.__insert_children(self._root, node)

    def __insert_children(self, root, node): # root(15,11,_,18) - node(18,15,_,_)
        if node._data['id'] <= root._data['id']:
            if not root._left:  # nÃ£o existe nÃ³ a esquerda (caso base)
                root._left = node
                root._left._parent = root
            else:
                self.__insert_children(root._left, node) # sub-Ã¡rvore esquerda
        else:
            if not root._right: # nÃ£o existe nÃ³ a direta (caso base)
                root._right = node
                root._right._parent = root
            else:
                self.__insert_children(root._right, node) # sub-Ã¡rvore direta

    def traversal(self, in_order=True, pre_order=False, post_order=False):
        result = list()
        if in_order:
            in_order_list = list()
            result.append(self.__in_order(self._root, in_order_list))
        else:
            result.append(None)

        if pre_order:
            pre_order_list = list()
            result.append(self.__pre_order(self._root, pre_order_list))
        else:
            result.append(None)

        if post_order:
            post_order_list = list()
            result.append(self.__post_order(self._root, post_order_list))
        else:
            result.append(None)

        return result

    def __in_order(self, root, lista):
        if not root:
            return
        self.__in_order(root._left, lista)
        lista.append(root._data)  # modificar para o trabalho parte 2???
        self.__in_order(root._right, lista)
        return lista

    def __pre_order(self, root, lista):
        if not root:
            return
        lista.append(root._data) # modificar para o trabalho parte 2???
        self.__pre_order(root._left, lista)
        self.__pre_order(root._right, lista)
        return lista

    def __post_order(self, root, lista):
        if not root:
            return
        self.__post_order(root._left, lista)
        self.__post_order(root._right, lista)
        lista.append(root._data) # modificar para o trabalho parte 2???
        return lista

    def print_binary_tree(self):
        if self._root:
            print(self.traversal(False, True, False)[1])


if __name__ == '__main__':
    t = BinaryTree()
    t.insert(11)
    t.insert(9)
    t.insert(15)
    t.insert(13)
    t.insert(3)
    t.insert(10)
    t.print_binary_tree()
    l = t.traversal(True, True, True)
    print(l)