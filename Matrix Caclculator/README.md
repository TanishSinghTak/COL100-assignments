# Introduction 
This is a python code for doing various linear algebra calculations through matrices.
There are 2 classes in the code Matrix and SparseMatrix.
* Matrix class is to represent normal matrix with *mxn* dimensions.
* SparseMatrix class stores only the nonzero entries in each row of a given matrix.
For example, the matrix B = Matrix([[-2,0,5], [0,0,0], [0,10,0]]) can be stored as [[(0,-2), (2,5)], [], [(1,10)]], where the first integer in the tuple represent the column of that number in the row.
So, in this example, since the 0th row has -2 at the 0th position and 5 at the 2th position, B will be represented in this manner for sparse Matrix reprentation. 

## Working

There are methods created in this for the linear algebra operations: addition, subtraction and multiplication with a method to represent matrix in string format.

Methods implemented in class Matrix are: 
* **str** : Method to represent matrix object in a nice string format. 
* **add** : Method to add two matrices.
* **sub** : Method to subtract two matrices.
* **mul** : Method to multiply two matrices.
* **toSparse** : Method to convert a Matrix to sparse format.


Methods implemented in class Sparse Matrix are: 
* **elem** : Method to get any specific element of the sparse Matrix.
* **str** : Method to represent sparse matrix object in a nice string format with 0's included. 
* **add** : Method to add two sparse matrices.
* **sub** : Method to subtract two sparse matrices.
* **mul** : Method to multiply two sparse matrices.
* **toDense** : Method to convert a sparse Matrix to normal dense format with 0's included.

## Conclusion

The sparse Matrix is formed to save the space to store the elements of the matrix which is o(mn) for a normal *mxn* matrix. So, If only a
few of the entries of the matrix are nonzero, we can save a lot of space using sparse matrix to store the elements of it.
