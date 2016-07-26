from pydsa.detecting_cyclicgraph import detecting_cyclicgraph


def test_detecting_cyclicgraph():
    assert detecting_cyclicgraph({1: (2,), 2: (3,), 3: (1,)}) == True
    assert detecting_cyclicgraph({1: (2,), 2: (3,), 3: (4,)}) == False
