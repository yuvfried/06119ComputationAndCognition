
%% loading the data

clc; clear all;

y_test = loadMNISTLabels('../MNIST_data/t10k-labels-idx1-ubyte');
y_train = loadMNISTLabels('../MNIST_data/train-labels-idx1-ubyte');

X_test = loadMNISTImages('../MNIST_data/t10k-images-idx3-ubyte');
X_train = loadMNISTImages('../MNIST_data/train-images-idx3-ubyte');

%% random permutation of the input

% uncomment this to use a fixed random permutation of the images
% perm = randperm(784);
% X_test = X_test(perm,:);
% X_train = X_train(perm,:);

%% parameters

layers_sizes = [784,30,10]; % flexible, but should be [784,...,10]
epochs = 10;
eta = 0.1;
batch_size = 20;

%% training

net = FF(layers_sizes);
[steps, test_acc] = net.sgd(X_train, y_train, epochs, eta, batch_size, X_test, y_test);


%% plotting learning curve and visualizing some examples from test set

% YOUR CODE HERE
