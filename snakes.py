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
        self.sqeezing = true
	other.status = grappled

    
class BoatConstrictor(BoaConstrictor):
    """Loose snakes sink ships?"""

    def __init__(self):
        """Create a new BoatConstrictor"""
        super().__init__()
        self.size = "enormous"
