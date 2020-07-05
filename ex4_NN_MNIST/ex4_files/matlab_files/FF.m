classdef FF < handle
    
    properties
        weights
    end
    
    methods
        function obj = FF(layerDims)
            %   layerDims is an array of [n_0,..,n_M]. Note that n_0 is the
            %   input dimension and n_M is the output dimension
            n_weights = length(layerDims)-1;
            obj.weights = cell(n_weights,1);
            for i=1:n_weights
                obj.weights{i} = 0.1*randn(layerDims(i+1),layerDims(i));
            end
        end
        
        function yhat = predict(obj,x)
            a = x;
            for i=1:length(obj.weights)
                a = obj.activation(obj.weights{i}*a);
            end
            yhat = a;
        end
        
        function [steps,test_acc] = sgd(obj, X, y, epochs, eta, mb_size, Xtest, ytest)
            N = size(X,2);
            n_mbs = ceil(N/mb_size);
            acc = obj.eval_test(Xtest,ytest);
            
            updates = 0;
            steps = [updates];
            test_acc = [acc];
            
            fprintf('Starting training, test accuracy: %f\n',acc);
            for i=1:epochs
                perm = randperm(N);
                for j=0:(n_mbs-1)
                    idxs = ((mb_size*j)+1):min(((mb_size)*(j+1)),N);
                    X_mb = X(:,perm(idxs));
                    y_mb = y(:,perm(idxs));
                    grads = obj.backprop(X_mb,y_mb);
                    
                    for k=1:length(obj.weights)
                        obj.weights{k} = obj.weights{k} - (eta/mb_size)*grads{k};
                    end
                    updates = updates+1;
                    
                    if mod(updates,50)==0
                        steps = [steps updates];
                        acc = obj.eval_test(Xtest,ytest);
                        test_acc = [test_acc acc];
                    end
                    
                end
                acc = obj.eval_test(Xtest,ytest);
                fprintf('Done epoch %d, test accuracy: %f\n',i,acc);
            end
            steps = steps/n_mbs;
        end
        
        
        function grads = backprop(obj,X,y)
            
            % X is a matrix of size input_dim*mb_size
            % y is a matrix of size output_dim*mb_size
            % you should return a cell 'grads' of dims (length(weights),1) such
            % that grads{i} is a matrix containing the gradients of the
            % loss with respect to weights{i}.
            
            
            % ForwardPass
            
            % YOUR CODE HERE
            
            % BackwardPass:
            
            % YOUR CODE HERE
            
            % gradients:
            
            % YOUR CODE HERE
            
        end
        
        function acc = eval_test(obj,Xtest,ytest)
            ypred = obj.predict(Xtest);
            ypred = ypred==max(ypred);
            acc = mean(all((ytest==ypred)));
        end
        
    end
    
    methods(Static)
        function z=activation(x)
            z = tanh(x);
        end
        
        function z=activation_deriv(x)
            z = 1-tanh(x).^2;
        end
        
        function z=loss_deriv(output, target)
            % Derivative of loss function with respect to the activations
            % in the output layer.
            % we use quadratic loss, where L=0.5*||output-target||^2
            
            % YOUR CODE HERE
            
        end
        
    end
end

