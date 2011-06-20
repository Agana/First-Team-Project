class Team:

    def __init__(self):
        """ Asks for the user input for a noun and stores the noun in
        the instance variable self.word.  Remember a noun is a person,
        place, or thing. """
        # TODO by person 3

	self.word = raw_input("Please enter a noun:")
	
	#'
        pass

     def reverse_input(self):
                
        print self.word.join([word[::-1] for word in self.word.split()])
	
        pass
    
    def print_in_sentence(self):
        print "Today I dreamt of",self.word,"while walking on the beach."
		        
	  # TODO by person 2
        pass

t = Team()
t.reverse_input()
t.print_in_sentence()
