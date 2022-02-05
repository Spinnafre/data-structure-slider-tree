import cv2
import numpy as np
from matplotlib import pyplot as plt
import os 
import copy
from tree import BinaryTree
    
def showDetailsImage(element):    
    name=element.get("name")
    year=element.get("year")
    
    
    image_height=img.shape[0]
    image_width=img.shape[1]
    
    #rectangle
    start_point=(5,image_height-60)
    end_point=(image_width-5,image_height-20)
    color = (255, 120, 120)
    thickness = -1
    
    #text
    org = (8, (image_height-60)+30)
    fontScale = 0.85
    color_font = (255, 255, 255)
    thickness_font = 1
    font = cv2.FONT_HERSHEY_DUPLEX 
    
    cache=copy.deepcopy(img)
    cv2.rectangle(img, start_point, end_point, color, thickness)
    cv2.putText(img,"{name}, {year}".format(name=name,year=year),org, font, fontScale,color_font,thickness_font,cv2.LINE_AA)

def showText(type,height=None):
    image_height=img.shape[0]
    image_width=img.shape[1]
    #rectangle
    start_point=(5,height-25 if height else 10)
    end_point=(image_width-5,height+25 if height else 45)
    color = (67,68,255)
    thickness = -1
    
    #text
    org = (8, height+5  if height else 30)
    fontScale = 0.65
    color_font = (255, 255, 255)
    thickness_font = 1
    font = cv2.FONT_HERSHEY_DUPLEX 
    
    cv2.rectangle(img, start_point, end_point, color, thickness)
    cv2.putText(img,"{type}".format(type=type),org, font, fontScale,color_font,thickness_font,cv2.LINE_AA)
    
def clearInfo():
    global img
    img = copy.deepcopy(cache)

def main():
    tree=BinaryTree()
    images=os.listdir('./images')
    length=len(images)

    images_details=[
    {"name":"1922","year":2017},
    {"name":"Army of the Dead","year":2021},
    {"name":"Awake","year":2021},
    {"name":"bird Box","year":2018},
    {"name":"Fullmetal","year":2017},
    {"name":"Imperial Dreams","year":2018},
    {"name":"IO","year":2019},
    {"name":"Iron First","year":2019},
    {"name":"Mosul","year":2019},
    {"name":"noOneGetOUtAlice","year":1980},
    {"name":"Old Guard","year":2020},
    {"name":"oxygem","year":2090},
    {"name":"punisher","year":2010},
    {"name":"Stranger Things","year":2022},
    {"name":"theHauntingOfHillHouse","year":2010},
    ]
    
    types_tranversal=['IN-ORDER','PRE-ORDER','POST-ORDER']
    
    for index in range(0,length):
        img_temp = cv2.imread('./images/' + images[index])
        h, w,_= img_temp.shape
        id_random=np.random.randint(100)+h+w
        print('INSERINDO => ',id_random)
        tree.insert({"id":id_random,"image_url":images[index],**images_details[index]})

    tt=tree.traversal(True,True,True)
    print(tt)

    
    window_name = 'Image'
    
    i = -1
    type_transition=0
    
    pointer=tt[type_transition]
    
    global img
    global cache

    img = cv2.imread('./images/' + pointer[0].get("image_url"))
    img = cv2.resize(img, (460, 420))
    showText('press "a" or "d" or "w" or "s" to start',210)
    cache=img.copy()
    cache=cv2.resize(cache, (460, 420))
    infoCount=0
    while True:
        cv2.imshow(window_name, img)
        key=cv2.waitKey(0) # Esperar qualquer tecla
        print('KEY PRESSED {}'.format(key))
        
        '''MOSTRAR INFORMAÇÃO DA IMAGEM '''
        if key == 105 and i!=-1:
            if infoCount < 1:
                showDetailsImage(pointer)
                infoCount+=1
            else:
                clearInfo()
                infoCount=0
                
        if key == 119: # Tecla W
            i=0
            pointer=tt[type_transition][i]
            img = cv2.imread('./images/' + pointer.get("image_url"))
            img = cv2.resize(img, (460, 420))
            showText(types_tranversal[type_transition])
            cache=img.copy()
                
        if key == 97: # Tecla A
            infoCount=0
            if type_transition != 0:
                print('PERCORRENDO POR EM ORDEM')
                i=0
                type_transition=0
                pointer=tt[type_transition][i]
                img = cv2.imread('./images/' + pointer.get("image_url"))
                img = cv2.resize(img, (460, 420))
                showText(types_tranversal[type_transition])
                cache=img.copy()
            else:
                i+=1
                if i<len(tt[type_transition]):
                    pointer=tt[type_transition][i]
                
                if pointer:
                    img = cv2.imread('./images/' + pointer.get("image_url"))
                    img = cv2.resize(img, (460, 420))
                    showText(types_tranversal[type_transition])
                    cache=img.copy()
            
        if key == 115: # Tecla S
            infoCount=0
            if type_transition != 1:
                print('PERCORRENDO POR PRE-ORDEM')
                i=0
                type_transition=1
                pointer=tt[type_transition][i]
                img = cv2.imread('./images/' + pointer.get("image_url"))
                img = cv2.resize(img, (460, 420))
                showText(types_tranversal[type_transition])
                cache=img.copy()
            else:
                i+=1
                if i<len(tt[type_transition]):
                    pointer=tt[type_transition][i]
                
                if pointer:
                    img = cv2.imread('./images/' + pointer.get("image_url"))
                    img = cv2.resize(img, (460, 420))
                    showText(types_tranversal[type_transition])
                    cache=img.copy()
        
        if key == 100: # Tecla D
            infoCount=0
                
            if type_transition != 2:
                print('PERCORRENDO POR PÓS-ORDEM')
                i=0
                type_transition=2
                pointer=tt[type_transition][i]
                img = cv2.imread('./images/' + pointer.get("image_url"))
                img = cv2.resize(img, (460, 420))
                showText('POST-ORDER')
                cache=img.copy()
            else:
                i+=1
                if i<len(tt[type_transition]):
                    pointer=tt[type_transition][i]
                
                if pointer:
                    img = cv2.imread('./images/' + pointer.get("image_url"))
                    img = cv2.resize(img, (460, 420))
                    showText('POST-ORDER')
                    cache=img.copy()
        
        if key == 27:
            break

    
    cv2.destroyAllWindows()
    



if __name__ == '__main__':
    main()