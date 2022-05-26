```
class Tree:
	def __init__(self, node_value):
		self.data = node_value
		self.children = []
		self.parent = None
	
	def add_child(self, child_name):
		self.parent = self
		self.children.append(child_name)

	def print_tree(self, level):
		print("\t"*level,self.data)
		if self.children:
			for child in self.children:
				child.print_tree(level+1)


def build_tree(	):
    root = Tree("school")
    class_1 = Tree("class1")
    class_2 = Tree("class2")
    class_3 = Tree("class3")    
    root.add_child(class_1)
    root.add_child(class_2)
    root.add_child(class_3)
	
    ankit = Tree("ankit")
    uk = Tree("uk")
    praveen = Tree("praveen")
    class_1.add_child(ankit)
    class_1.add_child(uk)
    class_1.add_child(praveen)
    
    atul = Tree("atul")
    priya = Tree("priya")
    class_2.add_child(atul)
    class_2.add_child(priya)
    
    rekha = Tree("rekha")
    sarita = Tree("sarita")
    yakshit = Tree("yakshit")
    class_3.add_child(rekha)
    class_3.add_child(sarita)
    class_3.add_child(yakshit)
    
    return root

if __name__ == "__main__":
    root = build_tree()
    root.print_tree(0)
```


## output
``` 
  school
   class1
     ankit
     uk
     praveen
   class2
     atul
     priya
   class3
     rekha
     sarita
     yakshit
```     
