from math import pi
import numpy as np
import matplotlib.pyplot as plt


def component_one_create_data(scale_value=2):
    xs = np.arange(0, 10, 0.1)  # x values from 0 to 10 in steps of 0.1
    ys = np.sin(xs)
    ys = ys / scale_value  # Scale by two (default) such that max values are half
    return xs, ys


def component_two_create_graph(xs=None, ys=None):
    # Retrieve dummy data if no data provided
    if xs is None or ys is None:
        xs, ys = component_one_create_data()

    # Create graph
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(xs, ys)

    return fig
