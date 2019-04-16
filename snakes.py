class Snake:
    """A dangerous and/or harmless serpent."""
    pass


class Cobra(Snake):
    """Definitely dangerous, yup."""
    def __init__(self,venom):
	self.venom = venom    

    def bite(self, other):
        """Deliver a dose of venom."""
        if other.immune == False:
		other.poisoned == True
		other.poison_timer = 10 * self.venom

    
class BoaConstrictor(Snake):
    """This one gives really good hugs."""
    
    def squeeze(self, other):
        """Give a hug."""
        pass

    
class BoatConstrictor(BoaConstrictor):
    """Loose snakes sink ships?"""
    pass
