def setup():
    size(200,300)              # set the widndow size
    background(0, 90, 172)  # set background color
    ellipse(60, 100, 50, 50)   # left eyeball
    fill(0, 0, 0)        # L pupil color
    ellipse(65, 105, 20, 20)   # left pupil
    fill(255, 255, 255)        # regulate the eyeball
    ellipse(150, 100, 50, 50)  # Right eyeball
    fill(0, 0, 0)        # R pupil color
    ellipse(155, 105, 20, 20)  # R pupil
    fill(0, 0, 0)
    ellipse(105, 180, 160, 90) # mouth
    fill(244, 164, 96)         # cookie color
    ellipse(180, 270, 70, 70)  # cookie
    fill(random(255), random(255), random(255))              # chocolate chips
    ellipse(180, 270, 7, 7)
    fill(random(255), random(255), random(255))
    ellipse(160, 281, 7, 7)
    fill(random(255), random(255), random(255))
    ellipse(199, 260, 7, 7)
    fill(random(255), random(255), random(255))
    ellipse(170, 250, 7, 7)
    fill(random(255), random(255), random(255))
    ellipse(185, 297, 7, 7)
    font = loadFont("Chiller-Regular-48.vlw")
    fill(random(255), 0, random(255))
    textFont(font, 25)
    text("Kammy2x", 10, 290)


    

    
