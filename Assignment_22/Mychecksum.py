import hashlib

def calculaltechecksum(path,blocksize = 1024):

    fobj = open(path, "rb")

    hobj = hashlib.md5()

    buffer = fobj.read(blocksize)

    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(blocksize)

    fobj.close()
    
    return hobj.hexdigest()