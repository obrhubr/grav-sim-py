import numpy as np

class Save(): 
    def __init__(self):
        self.posxarr, self.posyarr = np.delete(np.array([0], dtype='int64'), 0), np.delete(np.array([0], dtype='int64'), 0)

    def save(self, pointx, pointy):
        self.posxarr = np.append(self.posxarr, pointx)
        self.posyarr = np.append(self.posyarr, pointy)

    def export(self, totaltime, numofplan, filename):
        self.posxarr, self.posyarr = np.reshape(self.posxarr, (totaltime, numofplan)), np.reshape(self.posyarr, (totaltime, numofplan))
        np.savez_compressed(filename, posxarr=self.posxarr, posyarr=self.posyarr)