from utilities.dispersion_trees import DispersionTree, DispersionEdges
from utilities import test_data

def test_DispersionEdges():
    disp_edges = DispersionEdges(test_data.fraud_case01())
    assert not disp_edges.edge_dataframe.empty

def test_DispersionTree():
    disp_tree = DispersionTree(test_data.fraud_case01())
    assert not disp_tree.edge_dataframe.empty
    assert disp_tree.graph



    


