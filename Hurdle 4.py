def turnRight():
    turn_left()
    turn_left()
    turn_left()
def forwardJump():
    turnRight()
    move()
    turnRight()
def jump():
    turn_left()
    while not right_is_clear():
        move()
    forwardJump()
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    elif front_is_clear():
        move()
    else: 
        pass;
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turnRight():
    turn_left()
    turn_left()
    turn_left()