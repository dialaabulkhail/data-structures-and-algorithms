from grapghs.graphs import Graph

def test_add_node():
    g = Graph()
    g.add_node(10)
    assert [10] == g.get_node()



def test_add_edge():
    g = Graph()
    a =  g.add_node(1)
    b = g.add_node(2)
    g.add_edge(a, b)
    assert [[2,0]] == g.get_neighbors(a)



def test_get_node():
    g = Graph()
    a =  g.add_node(1)
    b = g.add_node(2)
    g.add_edge(a, b)
    assert [1,2] == g.get_node()



def test_size():
    g = Graph()
    a =  g.add_node(1)
    b = g.add_node(2)
    g.add_edge(a, b)
    assert 2 == g.size()



