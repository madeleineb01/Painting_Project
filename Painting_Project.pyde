canvas_x = 600
canvas_y = 600
rectangle_count = 3
rectangle_height = 70
rectangle_width = canvas_x / rectangle_count
value = 0
print(rectangle_width)


def setup (): #runs one time
    size(601, 601)
    background(255, 255, 255)
    #rect(0, 0, 167, 70)
    #fill(255, 232, 252)
    #rect(167, 0, 166, 70)
    #fill(219, 233, 255)
    #rect(333, 0, 166, 70)
    
    noFill()
    rect(0, 0, rectangle_width, rectangle_height)
    
    fill(255, 232, 252)
    rect(rectangle_width, 0, rectangle_width, rectangle_height)
    
    fill(219, 233, 255)
    rect(2*rectangle_width, 0, rectangle_width, rectangle_height)
    
    fill(255, 255, 255)
    rect(0, 70, 600, 530) #canvas
    
    noStroke()
    
def draw (): # Runs over and over
    if mousePressed and mouseY > 85:
        #fill(value)
        #fill(219, 233, 255)
        ellipse(mouseX, mouseY, 20, 20)
    
    if keyPressed and key == 'c' or key == 'C':
       fill(255, 255, 255)
       rect(1, 71, 599, 530)
    
    if (mouseX > rectangle_width and mouseX < rectangle_width*2 
            and mouseY < rectangle_height):
        print("in box 2")
        fill(255, 232, 252)
   
    elif mouseX > 2*rectangle_width and mouseY < rectangle_height:
        print("in box 3")
        fill(219, 233, 255)
    
    if mouseX > 0 and mouseX < rectangle_width and mouseY < 70:
        print("in box 1")
        fill(255, 255, 255)
        
    else:
        print("")

# #if mousePressed:
#     fill(value)
# global value
# if value == 0:
#     value = 67
# else:
#     value = 0
    
        
    # Box2 is at Top Left:(200, 0), Top Right:(400,0), Bottom Left:(200, 70), Bottom Right(400, 70)
    #200-400 in X
    # 0-70 in Y
    
    
