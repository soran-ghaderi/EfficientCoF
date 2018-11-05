# NUSCCF
An new eficient subspace based method to improve Collaborative Filtering  

This was implemented as B.Sc's final thesis written in python. A good level of modularity is considered while coding; same as previous, mostly an architecture has been defined in order to keep simplicity and avoid any confusion.

Soran Ghadri summer 2018

### Documentation will be uploaded subsequently.
### How to use codes will be upload subsequently.

## Abstract
In order to reduce the amount of time that people are spending to find their needed items, Recommender Systems are quite helpful.
Collaborative filtering is one of the most popular techniques being used to find customer's related items. It finds the most similar users to the target user based on the target user's activities. High dimensionality and data sparsity are two common problems which affect its performance negatively. The proposed method solves these problems in an efficient way which has been derived from K-Means and Subspace clustering approaches. In the suggested way, firstly users will be clustered into different clusters and then three subspaces will be extracted based on ratings of users namely Interested, Neither Interested Nor Uninterested, and Uninterested. With respect to subspaces, three tree structures will be constructed for target user. Furthermore, the first and second neighbors will be considered to calculate their similarities based on Pearson similarity. The Movielens 100k dataset has been used to train and test the Proposed technique. The results have illustrated that this technique can dramaticlly improve the performance of the collaborative filtering.
## Keywords
### Collaborative Filtering; Sparsity; High dimensionality; Subspace clustering; K-Means clustering
