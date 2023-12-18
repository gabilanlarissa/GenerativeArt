TOTAL_DEGREES = 360 #degrees in a circle
radius = 0
r = 255
g = 255
b = 255


def setup():
    size(displayWidth, displayHeight, radius)
    size(displayWidth/2, displayHeight)
    background(0)
    noFill()
    stroke(180, 30)
    radius = height/2

def draw():
    #colours to be printed in the frame
    r = random(255)
    g = random(255)
    b = random(255)
    
    #each time you click the mouse button, a new colour will appear
    if mousePressed:
        stroke(r,g,b, 40)
    
    #sketch's centre point
    center_x = width/2
    center_y = height/2
    
    global TOTAL_DEGREES, radius
    
    beginShape()
    #to create a looping
    for i in range(TOTAL_DEGREES):
        noiseFactor = noise(i*0.04, float(frameCount)/180) #the 'float' parameter will create a smooth animation / the 'frameCount' will print frames
        x = center_x + radius * cos(radians(i)) * noiseFactor  #or + random(100)
        y = center_y + radius * sin(radians(i)) * noiseFactor
        curveVertex(x,y) #connects the vertex in a circle
    endShape(CLOSE)
    
    radius -= 1
    
    if radius == 0:
        noLoop()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
