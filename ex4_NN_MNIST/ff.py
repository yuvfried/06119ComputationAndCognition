import numpy as np

class FF(object):
	"""A simple FeedForward neural network"""
	def __init__(self, layerDims):
		super(FF, self).__init__()
		n_weights = len(layerDims)-1
		self.weights = []
		for i in range(n_weights):
			self.weights.append(0.1*np.random.randn(layerDims[i+1], layerDims[i]))



	def sgd(self, X, y, epochs, eta, mb_size, Xtest, ytest):
		N = X.shape[1]
		n_mbs = int(np.ceil(N/mb_size))
		acc = self.eval_test(Xtest, ytest)

		updates = 0
		steps = [updates]
		test_acc = [acc]
		print("Starting training, test accuracy: {0}".format(acc))

		for i in range(epochs):
			perm = np.random.permutation(N);
			for j in range(n_mbs):
				X_mb = X[:,perm[j*mb_size:(j+1)*mb_size]]
				y_mb = y[:,perm[j*mb_size:(j+1)*mb_size]]

				grads = self.backprop(X_mb, y_mb)

				for k,grad in enumerate(grads):
					self.weights[k] = self.weights[k] - (eta/mb_size)*grad

				updates = updates + 1
				if updates%50 == 0:
					steps.append(updates)
					test_acc.append(self.eval_test(Xtest, ytest))

			acc = self.eval_test(Xtest, ytest)
			print("Done epoch {0}, test accuracy: {1}".format(i+1, acc))

		steps = np.asarray(steps)
		steps = steps/n_mbs

		return steps, test_acc

	def backprop(self,X,y):
		# X is a matrix of size input_dim*mb_size
		# y is a matrix of size output_dim*mb_size
		# you should return a list 'grads' of length(weights) such
		# that grads[i] is a matrix containing the gradients of the
		# loss with respect to weights[i].

		# ForwardPass

		# YOUR CODE HERE
		neurons = [X]  # neurons[i] is a matrix: layer[i]_size X MB_size (S)
		inputs = []  # inputs[i] is a matrix: layer[i]_size X MB_size (H)
		g = self.activation  # activation function: from H[i] to S[i]
		dg = self.activation_deriv  # derivative of activation function
		for i in range(len(self.weights)):  # weights idx: (as showed in class)-1
			h = np.dot(self.weights[i], neurons[i])
			inputs.append(h)
			neurons.append(g(h))

		# BackwardPass
		
		# YOUR CODE HERE
		deltas = []
		delta_m = self.loss_deriv(neurons[len(neurons)-1],y) * dg(inputs[len(inputs)-1])
		deltas.append(delta_m)
		for i in range(len(self.weights)-1):  # i from
			delta = np.dot(self.weights[-(i+1)].T,deltas[i]) * dg(inputs[-(i+2)])
			deltas.append(delta)
		deltas = deltas[::-1]

		# Gradients

		# YOUR CODE HERE
		grads = []
		for i in range(len(self.weights)):
			grads.append(np.dot(deltas[i],neurons[i].T))

		return grads



	def predict(self,x):
		a = x
		for w in self.weights:
			a = FF.activation(self, np.dot(w,a))

		return a

	def eval_test(self,Xtest, ytest):
		ypred = self.predict(Xtest)
		ypred = ypred==np.max(ypred,axis=0)
		
		return np.mean(np.all(ypred==ytest,axis=0))


	def activation(self, x):
		return np.tanh(x)

	def activation_deriv(self, x):
		return 1-(np.tanh(x)**2)

	def loss_deriv(self, output, target):
		# Derivative of loss function with respect to the activations
		# in the output layer.
		# we use quadratic loss, where L=0.5*||output-target||^2
		
		# YOUR CODE HERE
		return output-target


