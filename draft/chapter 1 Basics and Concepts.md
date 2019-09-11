# Chapter 1: Basics and Concepts

This chapter introduces the basic concepts for typical process of deep learning development and how are these concepts are mapped to the concepts in paddle.

## Basic Concepts of Deep Learning Developments

Fundamentally, deep learning involves defining a trainable model and train it with respect to some targets. The trainability of the model resides in the trainable parameters (and for some cases, the structure of the model and hyper parameter is also tuned, but now we just focus on a series of models which only differ in the paramters they hold.) and the target is typically related to a loss function which we want to minimize for some given training data. 

The key part of minimize the error is gradient descent algorithm. So the most important part of a deep learning framework is auto-grad. In practice, deep learning framworks offer a lot of functions with grad functionality, with the help of which we can build complicated models but when can still be easily differntiated. There is no magic of auto-grad. When basic functions are concerned, the grad functionality has to be implemented by the framework. So the more functions are implemented, the more expressive the framework is.

Since deep learning frameworks all leverages the concept of computation graph, how graph is maintained is also an important part of the framework. Some 

Dataset has its management is not the core part of a deep learning framework, but is handles many stuffs the user should otherwise do themselves. Data processing, shuffling, spliting, sampling, iterating, saving and loading may not be the most difficult part of deep learning, but it takes many lines of code to do so.

Also handling the process of training, recording, visualization, validation and model selection is an necessary part of the framework to make it usable.

Model saving and loading means a lot for the deployment of deep learning models. If the model is to be deployed without the client language runtime where it is created, a intermediate representation for all language has to be used. Many deep learning frameworks use protobuf to to this, by this strategy, the computation graph is saved (it means that a program is saved without explicitly been written in a specific langugae). If the model is not to be deployed without the original client language runtime, just saving the parameters is fine because the model can be defined again to the target runtime and load the saved parameters. This strategy will require the framework to have many bindings or frontends for many languages. This difference also affects which part of the model and how the model is saved. For the former stratedy, model means parameters and the computation logic, and both are saved. When used for inference, the graph is trimmed. For the latter, only parameters are conasidered the model, the computation logic is the code itself, it comes into the graph while the code is run. The computation logic is not saved, it is the source code.

## Basic Concepts of Paddle







