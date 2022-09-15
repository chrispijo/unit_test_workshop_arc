from my_package.my_application_components import component_one_create_data, component_two_create_graph


def my_application(scale_value):

    # Get data
    xs, ys = component_one_create_data(scale_value=scale_value)

    # Create graph
    fig = component_two_create_graph(xs, ys)

    return fig
