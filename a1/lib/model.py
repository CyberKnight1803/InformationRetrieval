import nltk 
from nltk.tokenize import word_tokenize

from zone_index import printZoneIndex
from constants import dummy_zone_index
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
        self.operators = ["AND", "OR", "NOT", "("]

    
    def _AND(self, lOp, rOp):
        """
            Performs 'lOp AND rOp' operation
        """

        result = {
            "title": list(set(lOp["title"]) & set(rOp["title"])),
            "meta": list(set(lOp["meta"]) & set(rOp["meta"])),
            "characters": list(set(lOp["characters"]) & set(rOp["characters"])),
            "body": list(set(lOp["body"]) & set(rOp["body"]))
        }

        return result
    
    def _OR(self, lOp, rOp):
        """
            Performs 'lOp OR rOp' operation
        """
        
        result = {
            "title": list(set(lOp["title"]) | set(rOp["title"])),
            "meta": list(set(lOp["meta"]) | set(rOp["meta"])),
            "characters": list(set(lOp["characters"]) | set(rOp["characters"])),
            "body": list(set(lOp["body"]) | set(rOp["body"]))
        }

        return result
        
    
    def _NOT(self, Op):
        """
            Performs 'NOT Op' operation
        """

        docIDs = set(range(self.corpus_size))
        
        result = {
            "title": list(docIDs -  set(Op["title"])),
            "meta": list(docIDs -  set(Op["meta"])),
            "characters": list(docIDs -  set(Op["characters"])),
            "body": list(docIDs -  set(Op["body"]))
        }

        return result


    def parse_query(self, query):
        """
            Parsers the query and returns a pre-processed query
        """

        operand_stack = []
        operator_stack = []

        for term in query:
            if (term not in self.operators) and (term != ')'):
                operand_stack.append(self.inverted_index[term])
            
            elif term in self.operators:
                operator_stack.append(term)
            
            else:
                while(operator_stack[-1] != "("):
                    if (operator_stack[-1] == "NOT"):
                        Op = operand_stack.pop()
                        operator_stack.pop()
                        result = self._NOT(Op)
                        operand_stack.append(result)
                    
                    elif (operator_stack[-1] == "OR"):
                        rOp = operand_stack.pop()
                        lOp = operand_stack.pop()
                        operator_stack.pop()

                        result = self._OR(lOp, rOp)
                        operand_stack.append(result)
                    
                    else:
                        rOp = operand_stack.pop()
                        lOp = operand_stack.pop()
                        operator_stack.pop()

                        result = self._AND(lOp, rOp)
                        operand_stack.append(result)

                operator_stack.pop() # pop "("
            
        return operand_stack[-1]


    def process_query(self, query):
        """
            Processes the query and returns the result
        """

        tokenized_query = word_tokenize(query)
        return self.parse_query(tokenized_query)


if __name__=="__main__":
    
    model = BooleanModel(corpus_size=30, inverted_index=dummy_zone_index)

    
    query = "((machine OR learning) AND NOT hello)"
    result = model.process_query(query)

    print("RESULT \n")
    for zone in result.keys():
            result[zone].sort()
            print("{zone:<20}{list:<10}".format(zone=zone, list=str(result[zone])))
