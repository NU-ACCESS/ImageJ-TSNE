from ij import IJ, ImagePlus
from ij.plugin import ImageCalculator
from ij.process import ImageProcessor
from ij.process import FloatProcessor
from fiji.util.gui  import GenericDialogPlus


#Input parameters
gd = GenericDialogPlus("Input Parameters")  
gd.addDirectoryOrFileField("Select composite color image, 32-bit","")
gd.addNumericField("Pixel size", 4, 0)  # show 3 decimals
gd.addNumericField("Background color", 150, 0)  # show 3 decimals
gd.showDialog()  

directory_w = gd.getNextString()
px = int(gd.getNextNumber())  
bc = int(gd.getNextNumber())  



#path to RGB image
IJ.open(str(directory_w))
imp = IJ.getImage()
IJ.run("8-bit")
IJ.run("32-bit")

n_slicesa = imp.getStack().getSize()
L =[]
for i in range(1, n_slicesa+1):
  imp.setSlice(i) 
  n = imp.getProcessor().getPixels()   
  n2 = [int(val) for val in n]
  L.append(n2)
imp.changes = False
imp.close()



#get initial dictionary D and construct matrix
imp2 = IJ.getImage()
IJ.run("Enhance Contrast...", "saturated=0 normalize process_all use")
IJ.run("Multiply...", "value="+str(500)+" stack")
#IJ.run("Add...", "value="+str(10)+" stack")
n_slices = imp2.getStack().getSize()
X =[]
for i in range(1, n_slices+1):
  imp2.setSlice(i) 
  n = imp2.getProcessor().getPixels()   
  n2 = [val for val in n]
  X.append(n2)

IJ.newImage("Untitled", "RGB white", 512, 512, 1)
IJ.run("Select All")
IJ.setForegroundColor(bc, bc, bc)
IJ.run("Fill", "slice")
imp3 = IJ.getImage()


for i in range(0,len(X[0])):  
	IJ.makeRectangle(X[0][i]+4, X[1][i]+4, px, px)
	IJ.setForegroundColor(L[0][i], L[1][i], L[2][i])
	IJ.run("Fill", "slice")