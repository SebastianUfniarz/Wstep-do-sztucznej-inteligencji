import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

class Neuron:
    def __init__(self, n_inputs, bias=0., weights=None):
        self.b = bias
        if weights is not None:
            self.ws = np.array(weights)
        else:
            self.ws = np.random.rand(n_inputs)

    def _f(self, x):
        return max(x * .1, x)

    def __call__(self, xs): 
        return self._f(xs @ self.ws + self.b)


class Layer:
    def __init__(self, n_neurons, n_inputs_per_neuron):
        self.neurons = [Neuron(n_inputs_per_neuron) for _ in range(n_neurons)]

    def __call__(self, xs):
        return np.array([neuron(xs) for neuron in self.neurons])


class ANN:
    def __init__(self, structure):
        self.layers = []
        for i in range(1, len(structure)):
            self.layers.append(Layer(structure[i], structure[i-1]))

    def __call__(self, xs):
        for layer in self.layers:
            xs = layer(xs)
        return xs


def visualize_ann(structure):
    G = nx.DiGraph()
    
    pos = {}
    layer_names = ['input'] + [f'hidden {i+1}' for i in range(len(structure)-2)] + ['output']
    node_counter = 0
    
    for i, layer_size in enumerate(structure):
        for j in range(layer_size):
            G.add_node(node_counter, layer=layer_names[i])
            pos[node_counter] = (i, j - layer_size / 2)
            node_counter += 1
    
    for i in range(len(structure) - 1):
        for j in range(structure[i]):
            for k in range(structure[i + 1]):
                G.add_edge(sum(structure[:i]) + j, sum(structure[:i + 1]) + k)
    
    plt.figure(figsize=(12, 6))
    nx.draw(G, pos, with_labels=False, node_size=500, node_color='skyblue', edge_color='gray')
    
    for i, layer_size in enumerate(structure):
        x = i
        y = -layer_size / 2
        plt.text(x, y - 0.5, layer_names[i], ha='center', va='center', fontsize=12, bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'))
    
    plt.show()


ann_structure = [3, 4, 4, 1]
ann = ANN(ann_structure)
visualize_ann(ann_structure)
