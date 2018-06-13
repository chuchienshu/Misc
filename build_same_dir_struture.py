import os

def isdir(x):
    return os.path.isdir(x) and x != '.svn'

#bulid a dir strutere like input
def mkfloders(src,tar):
    paths = os.listdir(src)
    paths = map(lambda name:os.path.join(src,name),paths)
    paths = filter(isdir, paths)
    if(len(paths)<=0):
        return
    for i in paths:
        (filepath, filename)=os.path.split(i)
        targetpath = os.path.join(tar,filename)
        not os.path.isdir(targetpath) and os.mkdir(targetpath)
        mkfloders(i,targetpath)
        
src = '/home/chuchienshu/Downloads/dataset/sintel/training/final/'
tar = '/home/chuchienshu/Downloads/dataset/sintel/flow_fpre/'
    
mkfloders(src, tar)
