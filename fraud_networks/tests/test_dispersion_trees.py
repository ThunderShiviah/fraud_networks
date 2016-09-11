from fraud_networks import DispersionTree, DispersionEdges

#from utilities.dispersion_trees import DispersionTree, DispersionEdges
from fraud_networks.utilities import test_data
import networkx as nx

def test_DispersionEdges():
    disp_edges = DispersionEdges(test_data.fraud_case01())
    assert not disp_edges.edge_dataframe.empty

def test_DispersionTree():
    disp_tree = DispersionTree()
    assert not disp_tree.edge_dataframe.empty
    assert disp_tree.graph
    assert nx.is_tree(disp_tree)



    


