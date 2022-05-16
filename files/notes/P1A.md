# 4.1.1.16: recursion

> Recursion is when a function calls itself [spam(){spam()}]
> Can be used to create infinite and defined loops

# 4.2.1.2: arrays

> Is an indexed set of related elements of the same datatype
> Arrays can have many dimensions (e.g. An array of arrays being a 2d array)
> Can be used to make a document-orientated database system

# 4.2.1.4: abstract datatypes

> They are not a core component, need to be made

# 4.2.2: queues

> Queues are first come first serve.  
> Used in printing and keyboard buffers.  
> Can use breadth first algo to search.  

> Linier queues are fixed with a start and an end pointer.  
> Adding an item moves the rear pointer along the array by 1.  
> Removing/reading an item moves the first pointer along by one.  
> Once it gets to the end, the queue is full and can no longer be used.  

> IF the queue is circular, the pointers would loop back to the start once at the end.  
> Items in a queue can be assigned priority, this makes it become a 2d queue.  
> Once all the items in the first priority array are used, you then move onto the next array.  

# 4.2.3: stacks

> Stacks are last come first serve.  
> Think of my pile of revision.  
> Items are added to the front of the pile

# 4.2.4: graphs

> Represents complex relationships between items in a dataset.  
> Nodes/vertecies are joined by arcs/lines.  
> A value can be added to arcs to imply a distance or a cost (weight).  
> Can be represented by both a matrix and a list.  

> An adjacency matrix is a tablular representation of a graph.  
> Each node is assigned a column and a row.  
> It stores every possible path.  
> Not memory efficient, but fast queerie times.  

> An adjacency list is a list of all possible routes in a graph.  
> For every node, a list of adjoning ndoes are created.  
> IT stores existing paths .  
> Memory efficient but queeries take time.  

# 4.2.5: trees

> A tree is a connected, undirected graph with no cucles.  
> Rooted trees have a common starting node.  
> Binary tree is a rooted tree where each node has no more than 2 child node.  
 