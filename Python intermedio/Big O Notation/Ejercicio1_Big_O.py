def bubble_sort(self): # O(n^2)
        if self.head is None or self.head.next is None: # O(1)
            return # O(1)
        
        swapped = True # O(1)

        while swapped: # O(n)

            swapped = False # O(1)

            current = self.head # O(1)  

            while current.next is not None: # O(n^2)

                if current.data > current.next.data: # O(1) 
                    current.data, current.next.data = current.next.data, current.data # O(1)

                    swapped = True # O(1)

                current = current.next # O(1)

# El algoritmo analizado es O(n^2)