class BooleanModel:

    def __init__(
        self, 
        inverted_index: dict
    ) -> None:
        self.inverted_index = inverted_index
        pass
    
    def _AND(self, lOp, rOp):
        """
            Performs AND operation
        """

        pass   
    
    def _OR(self, lOp, rOp):
        """
            Performs OR operation
        """

        pass 
    
    def _NOT(self, Op):
        """
            Performs NOT operation
        """

        pass 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
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

