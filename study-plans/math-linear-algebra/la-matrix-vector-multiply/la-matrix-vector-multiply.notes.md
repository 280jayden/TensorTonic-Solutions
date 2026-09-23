Matrix Vector multiplication is one of the most fundamental operations in linear algebra and the backbone of nearly every neural network computation. 



Given a matrix A of shape (m, n) and a vector x of shape (n, ), the product of Ax is a vector of shape (m, )



Each element of the output vector is the **dot product** of the corresponding row of A with the vector x.



As a refresher, the dot product of two vectors is a single number (a scalar), computed by multiplying the corresponding entries of the two vectors together, then summing all of those products up into one running total.