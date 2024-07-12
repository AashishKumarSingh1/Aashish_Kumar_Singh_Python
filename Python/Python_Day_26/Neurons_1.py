Inputs = [1, 2, 3, 2.5] 
weights = [[0.2, 0.8, -0.5, 1], 
           [0.5, -0.91, 0.26, -0.5], 
           [-0.26, -0.27, 0.17, 0.87]] 
biases = [2, 3, 0.5] 

layer_output=[]

for weight,bias in zip(weights,biases):
    neuron_output=[]
    res=0
    for w,i in zip(Inputs,weight):
        res=i*w
    res+=bias

    layer_output.append(res)

print(layer_output)
