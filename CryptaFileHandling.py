
#Import
from CryptaCipher import enc,dec


def read_file(filename):
    f = open(filename,"r")
    data = f.read()
    f.close()
    return data

def output_file(filenameout,outdata):
    f = open(filenameout,"w")
    f.write(outdata)
    f.close()
    
def encryptfile(filein,fileout,key):
    datain = read_file(filein)
    encdata = enc(key,datain)
    output_file(fileout, encdata)

def decryptfile(filein,fileout,key):
    datain = read_file(filein)
    decdata = dec(key,datain)
    output_file(fileout, decdata)
