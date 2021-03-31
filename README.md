# Image-Pixel-level-Preprocessing

use cv2 to do pixel reversal, histogram equalization, CLAHE(Contrast Limited Adaptive Histogram Equalization)

"""
the information about PIL and Opencv:
cv2 open file get a numpy array with shape(H,W,C)
when we need to do pytorch based transform, Totensor() will transpose the ndarray form(H,W,C) to (C,H,W)

For PIL:
with open file, we get a PILimage format file instead of an array 
when we do np.asarray(), we could get the array of the PIL image of (H,W,C)
if we want to transforms this array and use it as an tensor input for transforms, we also need to do transpose(2,0,1)
however,if we directly input PILimage into transforms ,we do not need to do transpose,because the transforms will do this automaticly
"""

ToTensor:Converts a PIL Image or numpy.ndarray (H x W x C) in the range
    [0, 255] to a torch.FloatTensor of shape (C x H x W) in the range [0.0, 1.0]
    if the PIL Image belongs to one of the modes (L, LA, P, I, F, RGB, YCbCr, RGBA, CMYK, 1)
    or if the numpy.ndarray has dtype = np.uint8

use resize,crop or other pytorch based transforms, PIL image could use them directly and then convert to Tensor,while ndarray need to do Totensor()  before transformation. But none of them need to do transpose(2,0,1) I think.
