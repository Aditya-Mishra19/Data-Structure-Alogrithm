class Node:
	def __init__(self, info, prev=None, next=None):
		self.info = info
		self.prev = prev
		self.next = next

class LinkedList:

	def __init__(self):
		self.head = None

	def insert_at_begining(self, ele):
		newNode = Node(ele)
		if self.head == None:
			self.head = newNode
		else:
			newNode.next = self.head
			self.head.prev = newNode
			self.head = newNode

	def insert_at_end(self, ele):
		newNode = Node(ele)
		if self.head == None:
			self.head = newNode
		else:
			current = self.head
			while current.next !=None:
				current = current.next
			current.next = newNode
			newNode.prev = current

	def delete_node(self, ele):
		#base case
		if self.head == None:
			print("List is empty")
			return

		#if only one node is present
		if self.head.next == None:
			if self.head.info == ele:
				temp = self.head
				self.head = None 
				temp = None 
				return
			else:
				print("Element is not found in our list")
				return

		#delete node in between
		temp = self.head.next 
		while temp.next != None:
			if temp.info == ele:
				temp.prev.next = temp.next
				temp.next.prev = temp.prev 
				temp = None
				return 
			temp = temp.next
		#delete last node
		if temp.info == ele:
			temp.prev.next = None 
			temp = None
			return
		print("Element is not found in the list")

	def display(self):
		if self.head == None:
			print("List is empty")
			return
		current = self.head
		while current != None:
			print(current.info)
			current = current.next 

ll = LinkedList()
ll.insert_at_begining(10)
ll.insert_at_begining(5)
ll.display()
print("******")
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.display()
ll.delete_node(20)
ll.display()
ll.delete_node(30)
ll.display()
ll.delete_node(40)