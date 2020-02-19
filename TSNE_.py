from com.jujutsu.tsne.barneshut import  BHTSne, ParallelBHTsne, BarnesHutTSne
from com.jujutsu.utils import TSneUtils, MatrixUtils, MatrixOps
from ij import IJ, ImagePlus
from ij.plugin import ImageCalculator
from ij.process import ImageProcessor
from ij.process import FloatProcessor
import cmath, math
import random
import datetime



#get initial dictionary D and construct matrix
imp2 = IJ.getImage()
n_slices = imp2.getStack().getSize()
X =[]
for i in range(1, n_slices+1):
  imp2.setSlice(i) 
  n = imp2.getProcessor().getPixels()   
  n2 = [val for val in n]
  X.append(n2)
X = zip(*X)#transpose signal X

initial_dims = n_slices
perplexity = 30.0
iters = 1000

config = TSneUtils.buildConfig(X, 2, initial_dims, perplexity, iters)

#tsne = BHTSne()
tsne = ParallelBHTsne()

j = tsne.tsne(config)

#Result = [val.tolist() for val in j]

Result = zip(*[val.tolist() for val in j])

#print(len(zip(*Result)))

X_dim = ImagePlus("X", FloatProcessor(imp2.width,imp2.height,Result[0]))
Y_dim = ImagePlus("Y", FloatProcessor(imp2.width,imp2.height,Result[1]))
#Z_dim = ImagePlus("Z", FloatProcessor(imp2.width,imp2.height,Result[2]))

X_dim.show()
Y_dim.show()
#Z_dim.show()

print(datetime.datetime.now())