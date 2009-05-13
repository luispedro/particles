import position as ps
import math 

def velocity(pos1,pos2,delta_t):
    '''
    This is a function used to calculate the mean velocity as a particle moves from position1 to
    position2.
    This fun requires four paramenters, position1, position2, time1 and time2. 
    '''
    distance = math.sqrt((pos1.x - pos2.x)**2+(pos1.y - pos2.y)**2)
    return distance/delta_t

def traj_vel(trajectory):
    '''
    This function is used to compute the average velocity of particles
    It will call the function velocity. 
    It requires input of the trajectory from trackgeneration.py.
    It will return the average velocity.
    '''

    delta_t = 1 # assume the time difference between frames is 1
    Nframes = len(trajectory)
    Ave_Vel_vector = [] # holds the average velocity for all paritles
    for i in xrange(len(trajectory)):
        Vel_vector = [] # holds the velocity of each particle
        for j in xrange(len(trajectory[i][1])-1):
            Vel_vector.append(velocity(ps.Position(trajectory[i][1][j][0],trajectory[i][1][j][1]),ps.Position(trajectory[i][1][j+1][0],trajectory[i][1][j+1][1]),delta_t))
        Ave_Vel_vector.append(sum(Vel_vector)/len(Vel_vector))
    
    return sum(Ave_Vel_vector)/len(Ave_Vel_vector)

def compute_statistics(simulated,predicted):
    '''
    This function is used to compare the average velocity of particles using
    simulated trajctory and predicted trajactory
    It will call function traj_vel and return two average velocities.
    '''
    simulated = traj_vel(simulated)
    predicted = traj_vel(predicted)
    return simulated, predicted
    
