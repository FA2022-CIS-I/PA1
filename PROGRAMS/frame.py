import scipy.linalg as linAlg

class Frame:
    """
        Class for representing a frame
    """

    def __init__(self,R,p):
        """
            Initializing the frame, with rotational and positional matricies
            @Param R, the rotational matrix R
            @Param p, the translational matrix p 
            no return type
        """
        self.R = R
        self.p = p
    
    def inv(self):
        """ 
            method to acquire a frame with the frame's contents inverse
            @param self: represents the object itself to which to acquire its inverse
            return type Frame, which is the object frame's inverted version
        """
        R_inv = linAlg.inv(self.R)
        return Frame(R_inv,-1*R_inv.dot(self.p))

    def composition(self,F):
        """ 
            Returns the dot product of two frames 
            @param self, the object itself
            @param F, the frame in which to dot itself with  
            return type Frame, of the product of the two frames 
        """
        return Frame(self.R.dot(F.R), self.R.dot(F.p) + self.p) 