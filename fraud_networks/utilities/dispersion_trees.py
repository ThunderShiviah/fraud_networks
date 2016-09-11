import pandas as pd
import networkx as nx
from fraud_networks.utilities import test_data

class DispersionEdges(object):
    def __init__(self, fraud_case):
        self.edge_dataframe = pd.DataFrame(fraud_case)

class DispersionTree(nx.DiGraph): #TODO: Should this be inheriting from nx.DiGraph?

    def __init__(self, fraud_case=None, **kwds): # Should I put the actual macro parameters instead of kwargs?
        """Takes in a fraud instance and returns a dispersion arborescence tree."""

        if fraud_case == None:
            self.example = fraud_case=test_data.fraud_case01()
        self.graph = nx.from_pandas_dataframe(df=fraud_case, source='source', target='target', create_using=nx.DiGraph())
        self.edge_dataframe = nx.to_pandas_dataframe(self.graph)

        #self.edge_dataframe = DispersionEdges(fraud_case).edge_dataframe #TODO: Should DispersionTree take DispersionEdges as input rather than fraud_case?
        #self = nx.from_pandas_dataframe(self.edge_dataframe, source='source', target='target') 
        
        
