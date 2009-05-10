import particles
import math 

def velocity_ave(pos1,pos2,t1,t2):
    '''
    This is a function used to calculate the mean velocity as a particle moves from position1 to
    position2.
    This fun requires four paramenters, position1, position2, time1 and time2. 
    '''
    distance = math.sqrt((pos1.x - pos2.x)**2+(pos1.y - pos2.y)**2)
    velocity = distance/abs(t2-t1)
    return velocity

def statistics(tracks):
    '''
    This function is used to compute the statistical result of particl tracking. 
    It will call the function velocity_ave. 
    It requires input of tracks
    '''
    Nframes = len(tracks)
    Result = [] # hold velocity for velocities
    for i in range(Nframes-1):
        velocity =
        velocity_ave(tracks[i][1],tracks[i+1][1],tracks[i][0],track[i+1][0])
        Result.append(velocity)
    sum = 0
    NVelocities = len(Result)
    for i in range(Nvelocities):
        sum += Result[i]
    return sum/NVelocities
