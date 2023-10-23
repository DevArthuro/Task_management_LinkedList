class Node: 
    def __init__(self, data: dict) -> None:
        self.__data: dict = data
        self.next: Node = None
    
    def set_edit_task(self, data: dict)-> None:
        self.__data: dict = data
    
    def get_task(self)-> dict:
        return self.__data