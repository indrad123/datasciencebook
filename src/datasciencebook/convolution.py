"""Transparent two-dimensional convolution and pooling utilities."""
import numpy as np

def output_size(size,kernel,stride=1,padding=0):
    if min(size,kernel,stride)<=0 or padding<0 or (size+2*padding-kernel)<0: raise ValueError("invalid dimensions")
    return (size+2*padding-kernel)//stride+1

def convolve2d(image,kernel,stride=1,padding=0):
    x=np.asarray(image,float);k=np.asarray(kernel,float)
    if x.ndim!=2 or k.ndim!=2 or not np.all(np.isfinite(x)) or not np.all(np.isfinite(k)): raise ValueError("image and kernel must be finite matrices")
    oh=output_size(x.shape[0],k.shape[0],stride,padding);ow=output_size(x.shape[1],k.shape[1],stride,padding);xp=np.pad(x,padding);out=np.empty((oh,ow))
    for i in range(oh):
        for j in range(ow):out[i,j]=np.sum(xp[i*stride:i*stride+k.shape[0],j*stride:j*stride+k.shape[1]]*k)
    return out

def max_pool2d(image,pool=2,stride=2):
    x=np.asarray(image,float)
    if x.ndim!=2: raise ValueError("image must be a matrix")
    oh=output_size(x.shape[0],pool,stride);ow=output_size(x.shape[1],pool,stride);out=np.empty((oh,ow))
    for i in range(oh):
        for j in range(ow):out[i,j]=np.max(x[i*stride:i*stride+pool,j*stride:j*stride+pool])
    return out

def conv_parameter_count(kernel_height,kernel_width,input_channels,output_channels,bias=True):
    if min(kernel_height,kernel_width,input_channels,output_channels)<=0: raise ValueError("dimensions must be positive")
    return kernel_height*kernel_width*input_channels*output_channels+(output_channels if bias else 0)

def receptive_field(layers):
    field=1;jump=1
    for kernel,stride in layers:
        if kernel<1 or stride<1:raise ValueError("invalid layer")
        field+=(kernel-1)*jump;jump*=stride
    return field
