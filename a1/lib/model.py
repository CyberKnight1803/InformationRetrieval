class BooleanModel:

    def __init__(
        self, 
        corpus_size: int,
        inverted_index: dict
    ) -> None:

        """
            Initializing necessary parameters and indexes
        """

        self.corpus_size = corpus_size
        self.inverted_index = inverted_index

    
    def _AND(self, lOp, rOp):
        """
            Performs 'lOp AND rOp' operation
        """

        lPostingList = self.inverted_index[lOp]
        rPostingList = self.inverted_index[rOp]

        return list(set(lPostingList) & set(rPostingList))
    
    def _OR(self, lOp, rOp):
        """
            Performs 'lOp OR rOp' operation
        """
        
        lPosting  = self.inverted_index[lOp]
        rPosting = self.inverted_index[rOp]

        return list(set(lPosting) | set(rPosting))
        
    
    def _NOT(self, Op):
        """
            Performs 'NOT Op' operation
        """

        docIDs = set(range(self.corpus_size))
        return list(docIDs - set(self.inverted_index[Op])) 


    def parse_query(self, query):
        """
            Parsers the query and returns a pre-processed query
        """

        pass 

    def process_query(self, query):
        """
            Processes the query and returns the result
        """

        pass 


