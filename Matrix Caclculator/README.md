# Introduction 
This is a python code for doing various linear algebra calculations through matrices.
There are 2 classes in the code Matrix and SparseMatrix.
* Matrix class is to represent normal matrix with *mxn* dimensions.
* SparseMatrix class stores only the nonzero entries in each row of a given matrix.
For example, the matrix B = Matrix([[-2,0,5], [0,0,0], [0,10,0]]) can be stored as [[(0,-2), (2,5)], [], [(1,10)]], where the first integer in the tuple represent the column of that number in the row.
So, in this example, since the 0th row has -2 at the 0th position and 5 at the 2th position, B will be represented in this manner for sparse Matrix reprentation. 

We use the sparse Matrix to save the space which is o(mn) for a normal *mxn* matrix which will be very inefficient if there are many zero entries in it.

<!-- ## Working

There are methods created in this for all the linear algebra operations to  -->
