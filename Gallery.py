import os
import re
import cv2
import face_recognition
from face_recognition.api import compare_faces, face_encodings

i=0

def movefile(path, pi, si):
    global i
    newperson='{}/person{}'.format(path,i)
    try:
        fpi=open('{}/{}'.format(path,pi),'rb')
        picture=fpi.read()
        fpi.close()
        fpo=open('{}/{}'.format(newperson,pi),'wb')
        fpo.write(picture)
        fpo.close()
    except:
        print('')
    try:
        fsi=open('{}/{}'.format(path,si),'rb')
        picture=fsi.read()
        fsi.close()
        fso=open('{}/{}'.format(newperson,si),'wb')
        fso.write(picture)
        fso.close()
    except:
        print('')
    print('Grouping this person')

def makeperson(path, pi):
    global i
    i=i+1
    newperson='{}/person{}'.format(path,i)
    os.mkdir(newperson,1)
    try:
        fpi=open('{}/{}'.format(path,pi),'rb')
        picture=fpi.read()
        fpi.close()
        fpo=open('{}/{}'.format(newperson,pi),'wb')
        fpo.write(picture)
        fpo.close()
    except:
        print('')
    print('new person added')


def clearjunk(path, images,):
    for name in images:
        if os.path.exists('{}/{}'.format(path,name)):
            os.remove('{}/{}'.format(path,name))
            print('{}-deleted'.format(name))
        else:
            print('{} not found'.format(name))


if __name__=="__main__":
    path=input("Enter Folder address:")
    images=tuple(os.listdir(path))
    data={}
    count=0
    for image in images:
        name=image
        image=cv2.imread('{}/{}'.format(path,name))
        encodes=face_recognition.face_encodings(image)[0]
        if count==0:
            count+=1
            data[name]=encodes
            print("first entry",end="-")
            makeperson(path, name)
            continue
        else:
            count+=1
            for n in data.keys():
                match=face_recognition.compare_faces([data[n]], encodes)
            if match[0]==True:
                print("matched",end="-")
                movefile(path, name, n)
                continue
            else:
                data[name]=encodes
                print("not matched",end="-")
                makeperson(path, name)

    clearjunk(path,images)