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
        return max(x * 0.1, x)

    def __call__(self, xs):  
        return self._f(xs @ self.ws + self.b)

class ANN:
    def __init__(self, structure):
        self.layers = []
        for i in range(1, len(structure)):
            layer = [Neuron(structure[i-1]) for _ in range(structure[i])]
            self.layers.append(layer)

    def __call__(self, x):
        for layer in self.layers:
            x = np.array([neuron(x) for neuron in layer])
        return x

    def visualize(self):
        G = nx.DiGraph()

        pos = {}
        layer_id = 0

        input_size = len(self.layers[0][0].ws)
        for j in range(input_size):
            node_id = f"L0_N{j}"
            G.add_node(node_id)
            pos[node_id] = (layer_id, -j)
        layer_id += 1

        for i, layer in enumerate(self.layers):
            for j in range(len(layer)):
                node_id = f"L{layer_id}_N{j}"
                G.add_node(node_id)
                pos[node_id] = (layer_id, -j)
            layer_id += 1

        for i in range(len(self.layers)):
            for j, neuron in enumerate(self.layers[i]):
                for k in range(len(neuron.ws)):
                    src = f"L{i}_N{k}"
                    dst = f"L{i+1}_N{j}"
                    G.add_edge(src, dst)

        plt.figure(figsize=(12, 8))
        color_map = []
        for node in G:
            if 'L0' in node:
                color_map.append('lightcoral')
            elif 'L1' in node:
                color_map.append('lightblue')
            elif 'L2' in node:
                color_map.append('lightblue')
            elif 'L3' in node:
                color_map.append('lightgreen')

        nx.draw(G, pos, node_color=color_map, with_labels=True, node_size=1000, edge_color='gray', width=1.5, font_size=8, font_weight="bold")
        plt.text(0, -0.5, "input\nlayer", ha='center', va='center', fontsize=12, bbox=dict(facecolor='lightcoral', alpha=0.5))
        plt.text(1, -0.5, "hidden\nlayer 1", ha='center', va='center', fontsize=12, bbox=dict(facecolor='lightblue', alpha=0.5))
        plt.text(2, -0.5, "hidden\nlayer 2", ha='center', va='center', fontsize=12, bbox=dict(facecolor='lightblue', alpha=0.5))
        plt.text(3, -0.5, "output\nlayer", ha='center', va='center', fontsize=12, bbox=dict(facecolor='lightgreen', alpha=0.5))

        plt.show()

structure = [3, 4, 4, 1]
ann = ANN(structure)
ann.visualize()
