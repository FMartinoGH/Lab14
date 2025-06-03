from model.model import Model

myModel = Model()
myModel.buildGraph("Santa Cruz Bikes", 5)
print(myModel.getNumNodes(), myModel.getNumEdges())
print(myModel)