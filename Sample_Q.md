1. If a Decision Tree is overfitting the training set, is it a good idea to try decreasing max_depth ? Briefly explain your answer.

**A**: Decreasing the max_depth parameter of a Decision Tree is a common technique to address overfitting. The max_depth parameter determines the maximum depth of the tree, controlling how many splits or decisions it can make. By reducing the maximum depth, you simplify the model and prevent it from creating overly complex decision boundaries that capture noise in the training data.

2. Briefly explain the most important difference between the AdaBoot and the Gradient Boosting methods.
 
**A**: The most important difference between AdaBoot and Gradient Boosting methods lies in how they handle the weighting of training instances during the iterative learning process. AdaBoost focuses on the instances that were misclassified in the previous iteration by assigning higher weights to them. However, Gradient Boosting fits a weak learner to the data and calculates the residuals (the differences between the predicted and actual values).

3. Briefly describe two techniques to select the right number of clusters when using K-Means

**A**: Two common techniques to determine the optimal number of clusters are the elbow method and the silhouette score: 
The elbow method involves running the K-Means algorithm on the dataset for a range of values of k (number of clusters).For each value of k, compute the sum of squared distances (inertia) of each point to its assigned cluster center.
Plot the inertia values for different values of k and look for an "elbow" point on the graph, where the rate of decrease in inertia sharply changes.

The silhouette score measures how similar an object is to its own cluster (cohesion) compared to other clusters (separation). For each value of k, calculate the average silhouette score across all data points. Choose the value of k that maximizes the silhouette score.

4. In multi-layer perceptron, does increasing the number of hidden layers improve performance? Explain your answer with reference to any dataset example from lessons or assignment

**A**: The impact of increasing the number of hidden layers in a multi-layer perceptron (MLP) on performance can vary and is highly dependent on the specific characteristics of the dataset and the complexity of the underlying patterns. Adding more hidden layers increases the capacity of the model to learn intricate representations of the data, but it also introduces the risk of overfitting, especially if the dataset is not large enough or if the added complexity is not justified.

5. Explain what is happening in the code below.

**A**: This is the backward pass progress of the neural network, it includes loss computation and gradient computation and weights update progress.

6. What are the major similarities and differences between Adam and AdaGrad? If given a regression or classification problem, which one would perform better and why? How would you evaluate them?

**A**: AdaGrad adapts the learning rates by individually scaling the learning rate for each parameter based on the historical sum of squared gradients. It effectively provides a larger learning rate for parameters with smaller historical gradients.Adam combines ideas from both momentum-based methods and RMSprop. It uses exponential moving averages of both gradients and their squared values to adaptively adjust learning rates. Adam also includes bias correction terms to account for the initialization bias in the moving averages. For a regression or classification problem, the performance of Adam and AdaGrad may depend on the characteristics of the dataset and the specific optimization landscape. They can be evaluated from the following ways:
Cross-validation: Use cross-validation to assess the generalization performance of models trained with Adam and AdaGrad on different subsets of the data.
Learning curves: Analyze the learning curves to observe convergence speed and generalization performance during training.
