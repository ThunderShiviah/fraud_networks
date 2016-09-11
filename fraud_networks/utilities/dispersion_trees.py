import pandas as pd
import networkx as nx

class DispersionEdges(object):
    def __init__(self, fraud_case):
        self.edge_dataframe = pd.DataFrame(fraud_case)

class DispersionTree(object): #TODO: Should this be inheriting from nx.DiGraph?

    def __init__(self, fraud_case, **kwargs): # Should I put the actual macro parameters instead of kwargs?
        """Takes in a fraud instance and returns a dispersion arborescence tree."""

        self.edge_dataframe = DispersionEdges(fraud_case).edge_dataframe
        self.graph = nx.from_pandas_dataframe(self.edge_dataframe, source='source', target='target') 
        
        
