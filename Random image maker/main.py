from PIL import Image
import random
import cv2
import numpy as np
class main():
    def __init__(self, size, variety):
        self.size = size
        self.variety = variety

    def image(self):
        n = Image.new("RGB",tuple(self.size))
        if self.variety == None:
            for i in range(self.size[0]):
                for j in range(self.size[1]):
                    n.putpixel((i,j),(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            return(n)
        elif self.variety == "square":
            radius = self.size[1]
            self.square(0,None)
        
    def video(self,time,fps):
        videodims = (self.size[0],self.size[1])
        fourcc = cv2.VideoWriter_fourcc(*'avc1')    
        video = cv2.VideoWriter("test1.mp4",fourcc, fps,videodims)
        #draw stuff that goes on every frame here
        for i in range(0,time*fps):
            video.write(cv2.cvtColor(np.array(self.image()), cv2.COLOR_RGB2BGR))
            print(f'{i+1} out of {time*fps}')
        video.release()    
    def change(self,time,fps):
        videodims = (self.size[0],self.size[1])
        fourcc = cv2.VideoWriter_fourcc(*'avc1')    
        video = cv2.VideoWriter("test6.mp4",fourcc, fps,videodims)
        #draw stuff that goes on every frame here
        j=0
        for i in range(0,time*fps):
            video.write(cv2.cvtColor(np.array(self.square(i+8,None)), cv2.COLOR_RGB2BGR))
            print(f'{i+1} out of {time*fps}') 
        video.release()    

    
    
    
    
    
    
    
    
    
    def square(self,x,color):
        if color == None:
            color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        n = Image.new("RGB",tuple(self.size))
        #top 
        for i in range(self.size[0]-2*x):
            n.putpixel((i+x,x),color)
        
        #left
        for j in range(self.size[1]-2*x):
            n.putpixel((x,j+x),color)
        #bottom
        for i in range(self.size[0]-2*x):
            n.putpixel((i+x,self.size[1]-1-x),color)
        #right
        for j in range(self.size[1]-2*x):
            n.putpixel((self.size[0]-1-x,j+x),color)
        #n.show()
        return(n)
    def triangle(self,x,color):
        if color == None:
            color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        n = Image.new("RGB",tuple(self.size))
        #top 
        
        #left
        for j in range(self.size[1]-2*x):
            n.putpixel((x-j,j-x),color)
        for j in range(self.size[1]-2*x):
            n.putpixel((int(x+100/(j+1)),int(x+100/(j+1))),color)
        #bottom
        #n.show()
        #n.show()
        return(n)

    def rip(self,x,color):
        if color == None:
            color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        n = Image.new("RGB",tuple(self.size))
        #top 
        for i in range(self.size[0]):
            n.putpixel((i%x,x),color)
        
        #left
        for j in range(self.size[1]):
            n.putpixel((x,j%x),color)
        #bottom
        for i in range(self.size[0]-2*x):
            n.putpixel((i%x,self.size[1]-1-x),color)
        #right
        for j in range(self.size[1]-2*x):
            n.putpixel((self.size[0]-1-x,j%x),color)
            
        n.show()
        return(n)



#1920 x 1080

if __name__ == "__main__":
    main([1920,1080],variety='square').change(20,30)
    #main([1920,1080],variety='square').triangle(10,None)