import scipy.linalg as linAlg

class Frame:
    """
        Class that represents a coordinate frame
    """

    def __init__(self,R,p):
        """
            Initialize rotational and positional elements for a frame

            :param r: Rotation Matrix 
            :param p: Translational vector

            :type r: numpy.array([][]), NxN
            :type P: numpy.array([][]), Nx1
        """
        self.R = R
        self.p = p
    
    def inv(self):
        """ 
           Inverting a coordinate frame
           :return: A frame with components inverted

           :rtype: Frame
        """
        R_inv = linAlg.inv(self.R)
        return Frame(R_inv,-1*R_inv.dot(self.p))

    def composition(self,F):
        """ 
          Frame composition with another frame

          :param F: Frame to conduct a composition with 
          :type f: Frame

          :return: A frame that is comprised of a composition of the two Frames inputed
          :rtype: Frame
        """
        return Frame(self.R.dot(F.R), self.R.dot(F.p) + self.p) 