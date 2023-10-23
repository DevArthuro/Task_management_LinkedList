from .node import Node
from typing import List

# Data Structure
class LinkedList:
    # Inicialize the data structure and components
    def __init__(self) -> None:
        self.head: Node = None
        self.lenght: int = 0
    
    # Function add new node with its data
    def set_new_node(self, data)-> None:
        node: Node = Node(data)
        # Add the head 
        if self.head == None:
            self.head = node
            self.lenght += 1
            return
        
        self.get_node_current().next = node
        self.lenght += 1

    # Get the last node 
    def get_node_current(self)-> Node:
        node_current: Node = self.head
        while node_current.next != None:
            node_current = node_current.next
        return node_current

    # Get the node for index, this start with 0
    def get_node_for_index(self, index: int)-> Node:
        index_current: int = 0
        node_current: Node = self.head
        
        while node_current != None and (index >= 0 and index < self.lenght):
            if index_current == index:
                return {
                    "message": "Encontrada",
                    "value": node_current
                }
            node_current = node_current.next
            index_current += 1
        
        return {
            "message": "Fuera de rango",
            "value": None
        }

    # Get the values in the list structure 
    def get_values_nodes(self)-> List[dict]:
        list_nodes: list = []
        node_current: Node = self.head
        while node_current.next != None:
            list_nodes.append(node_current.get_task())
            node_current = node_current.next
        list_nodes.append(node_current.get_task())
        return {
            "message": "Encontradas",
            "value": list_nodes
        }

    # Function to delete the especifict node for an index
    def set_delete_task(self, index: int)-> None:
        if index < 0 or index >= self.lenght:
            return {
                "message": "Fuera de rango"
            }
        
        # Delete the head linked List
        if index == 0:
            node_delete = self.head
            node_change = node_delete.next
            self.head = node_change
            node_delete.next = None
            self.lenght -= 1
            return {
                "message": "Eliminado con éxito"
            }

        # Get the connections of node for the success change
        node: Node = self.get_node_for_index(index).get("value")
        node_before: Node = self.get_node_for_index(index - 1).get("value")
        node_after: Node = node.next

        # Refactor to nodes 
        node.next = None
        node_before.next = node_after
        self.lenght -= 1
        return {
            "message": "Eliminado con éxito"
        }

    # Load the edit task 
    def set_edit_task(self, index: int, data: dict):
        if index < 0 or index >= self.lenght:
            return {
                "message": "Fuera de rango"
            }
        # Catch the current task 
        node_current: Node = self.get_node_for_index(index).get("value")
        node_current.set_edit_task(data)
        return {
            "message": "Cambiado con éxito"
        }

# Code to text the data structure
"""lkls = LinkedList()
lkls.set_new_node({"name": "juan", "age": 15})
lkls.set_new_node({"name": "juan pablo", "age": 19})
lkls.set_new_node({"name": "carlos", "age": 18})
lkls.set_new_node({"name": "pedro", "age": 18})
lkls.set_new_node({"name": "julian", "age": 22})
lkls.set_new_node({"name": "cghifd", "age": 22})
lkls.set_new_node({"name": "fsdfds", "age": 23})
print(lkls.get_values_nodes())
print(lkls.get_node_for_index(2).get("value").get_task())
print(lkls.set_delete_task(1).get("message"))
print(lkls.set_delete_task(10).get("message"))
print(lkls.set_delete_task(0).get("message"))
print(lkls.set_delete_task(5).get("message"))
lkls.set_new_node({"name": "gggg", "age": 18})
lkls.set_new_node({"name": "aaaa", "age": 22})
print(lkls.get_values_nodes())
print(lkls.lenght)
print(lkls.set_delete_task(6).get("message"))
print(lkls.lenght)
lkls.set_edit_task(3, {"name": "paco", "age": 24})
print(lkls.get_values_nodes())
lkls.set_edit_task(4, {"name": "pacopedro", "age": 30})
print(lkls.get_values_nodes())"""
