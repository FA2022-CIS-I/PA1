import scipy.linalg as linAlg

class Frame:

    def __init__(self,R,p):
        self.R = R
        self.p = p
    
    def inv(self):
        R_inv = linAlg.inv(self.R)
        return Frame(R_inv,-1*R_inv.dot(self.p))

    def composition(self,F):
        return Frame(self.R.dot(F.R), self.R.dot(F.p) + self.p) 