import particles
import position as ps
import math 

def velocity(pos1,pos2,t1,t2):
    '''
    This is a function used to calculate the mean velocity as a particle moves from position1 to
    position2.
    This fun requires four paramenters, position1, position2, time1 and time2. 
    '''
    distance = math.sqrt((pos1.x - pos2.x)**2+(pos1.y - pos2.y)**2)
    return distance/abs(t2-t1)

def traj_vel(trajectory):
    '''
    This function is used to compute the average velocity of particles
    It will call the function velocity. 
    It requires input of the trajectory from trackgeneration.py.
    It will return the average velocity.
    '''
# figure out how many particles are in the system
    Nparticles = 0 # number of particles
    threshold = 1.0e-5 # criterion for equality
    t0 = trajectory[0]
    for i in xrange(0,len(trajecotry),3):
        if trajectory[i]-t0 < threshold : 
            Nparticles += 1 
        else:
            break
# calculate the velocity average
    try:
        len(trajectory)%Nparticles == 0
    except:
        print "trajectory impaired" 

    Nframes = len(trajectory)/Nparticles

#velocity vector contains the time evolution of velocities of all particles
#velocities of all particles in a delta t time span is arragned to form a vector, and these vectors are linearly binded to form the Vel_vector

    Vel_vector = [] # velocity vector
    for i in xrange(0,len(trajecotry)-1,Nparticles):
        for j in xrange(0,Nparticles,3):
            Vel_vector.append(ps.Position(trajectory[i+j+1],trajectory[i+j+2]),ps.Position(trajectory[i+Nparticles+j+1],trajectory[i+Nparticles+j+2]),trajectory[i+j],trajectory[i+Nparticles])
    
# Vel_sum contains the average velocity for each partical 
    Vel_sum = []
    for i in xrange(Nparticles):
        sum = 0 
        for j in xrange(0,len(Vel_vector),Nparticles):
            sum += Vel_vector[i+j]
        Vel_sum.append(sum)
    
    sum = 0
    for i in xrange(len(Vel_sum)):
        sum += Vel_sum[i]
    return sum/len(Vel_sum)

def compute_statistics(simulated,predicted):
    '''
    This function is used to compare the average velocity of particles using
    simulated trajctory and predicted trajactory
    It will call function traj_vel and return two average velocities.
    '''
    return traj_vel(simulated,predicted)
    
