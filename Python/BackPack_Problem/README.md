# BackPack Problem v1.0

A software that can take as input a collection of Tetris pieces and a container, then places the pieces inside the container at the next available space (from the bottom left corner) and finally returns the resulting configuration. Let’s review one by one these concepts.

1. In the input, the container is represented by two values M and N. In the software, the container is represented by a matrix C=M x N whit 0 at all positions when initialized. In the example below, a container C with size M = 7 and N = 8 on the left, and the initialized state of the matrix on the right.

2. In the input, the Tetris pieces are represented by multi-dimensional arrays as follows:

1 = [[1, 0, 0], [1, 1, 1]] 
2 = [[1, 1, 1], [1, 0, 0]] 
3 = [[1, 1], [0, 1], [0, 1]] 
4 = [[1, 1], [1, 0], [1, 0]] 
5 = [[1, 1, 0], [0, 1, 1]]
6 = [[0,1,1],[1,1,0]] 
7 = [[0,1,0],[1,1,1]] 
8 = [[1,1],[1,1]]
9 = [[1], [1], [1], [1]] 
10 =[[1,1,1,1]]

3. The algorithm should place the pieces in the order they are specified in the input.Starting from the lower left corner, from left to right, from bottom to top.



