# Image-Pixel-level-Preprocessing

use cv2 to do pixel reversal, histogram equalization, CLAHE(Contrast Limited Adaptive Histogram Equalization)

"""
the information about PIL and Opencv:
cv2 open file get a numpy array with shape(H,W,C)
when we need to do pytorch based transform, we need to do transpose(2,0,1)
beceuse transforms need input to be a PIL image or a tensor with shape (C,H,W)

For PIL:
with open file, we get a PILimage format file instead of an array 
when we do np.asarray(), we could get the array of the PIL image of (H,W,C)
if we want to transforms this array and use it as an tensor input for transforms, we also need to do transpose(2,0,1)
however,if we directly input PILimage into transforms ,we do not need to do transpose,because the transforms will do this automaticly
"""


