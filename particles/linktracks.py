import  numpy as np
import  random
import  math
from    munkres import Munkres

'''
def generate_posits(tracks):
    
    this function takes tracks and generates
    (1) a video (3D array) of particles moving and (2) a list of list of particle positions
    Both of these objects are useful for testing the LINK_TRACKS method below, where the position 
    lists are converted into a list of Tracks.
    GENERATE_POSITS should be commented out when run as part of PARTICLES.
    
    
    video = np.zeros((timesteps,L,L))
    positions = []
  
    # create video as 3D (t,x,y) array
    for i in xrange(len(tracks)):
        for j in xrange(len(tracks[i][1])):
            video[tracks[i][0] + j][tracks[i][1][j].x][tracks[i][1][j].y]= 1
    
    # print video # uncomment to show particle movement by frame
    
    # create positions as list of lists(one poslist per timepoint)
    posits = []
    for t in xrange(np.size(video,0)):
        pos = []
        for i in xrange(np.size(video,1)):
            for j in xrange(np.size(video,2)):
                if video[t][i][j] == 1:
                    pos.append(Position(i,j))
        posits.append(pos)
    
    return (posits, video)
'''

def link_tracks(Positions):
    '''
    This function takes in a list of positions, per time frame, and constructs
    particle tracks based on solutions to the 'assignment problem'. This is done 
    through the MUNKRES method by Brian Clapper, http://www.clapper.org/software/python/munkres/,
    which must be installed for LINK_TRACKS to work.
     
    The output format is identical to that from 
    TRACKGENERATION.py: a list of tuples, where the first element is the starting time of 
    the track, and the second element is a list of position objects, each having
    attributes x and y. 
    '''
    pos = Positions
    TrackList = []
    Tracks  = []
    t0      = 0
    T       = len(pos) # one list of positions per time frame 
    initNumOfTracks = len(pos[t0])
    
    # initialize all first tracks
    TrackList = []
    for i in xrange(initNumOfTracks):
        TrackList.append(EachParticle(t0,pos[t0][i])) #.give_the_track()) 
    
    # move through positions by time
    for i in xrange(T-1):
        curr_posits = pos[i]
        next_posits = pos[i+1]

        cost = make_cost(curr_posits, next_posits)
        
        m = Munkres()
        indices = m.compute(cost)

        # print indices
        
        for row, column in indices:
            for j in xrange(len(TrackList)):
                if row >= len(curr_posits): # create new track
                    TrackList.append(EachParticle(i+1,next_posits[column]))
                    #print 'track created'
                    continue
                
                if [lastElement(TrackList[j]).x, lastElement(TrackList[j]).y] == [curr_posits[row].x, curr_posits[row].y] and TrackList[j].active:

                    if column >= len(next_posits): # track deleted
                        TrackList[j].active = 0

                    else: # append new location to existing track
                        TrackList[j].poslist.append(next_posits[column])
    
    # convert tracks from EachParticle to Particle format
    Tracks = []
    for i in xrange(len(TrackList)):
        Tracks.append(TrackList[i].give_the_track())
        
    return Tracks
        
def make_cost(curr, next):
    '''
    this method uses the 2-norm (DISTANCE) to calculate
    the distance between particles
    '''
    cost = np.zeros( (max([len(curr), len(next)]), max([len(curr), len(next)])) )
    if len(curr) <= len(next):
        for c in xrange(len(curr)):
            for n in xrange(len(next)):
                cost[c][n] = distance(curr[c], next[n]) # padded with zeros when i < j
                
    if len(curr) > len(next):
        for c in xrange(len(curr)):
            for n in xrange(len(next)):
                cost[c][n] = distance(curr[c], next[n]) 
        for c in curr:
            for n in xrange(len(curr), len(next)):
                cost[c][n] = max(cost[c])   # padded with max in each row
    return cost

def distance(position_1, position_2):
    pos1 = position_1
    pos2 = position_2
    dis = np.square(pos1.x - pos2.x) + np.square(pos1.y-pos2.y)
    return np.sqrt(dis)

def lastElement(track):
    return track.give_the_track()[1][-1]

# uncomment the following lines to run LINKTRACKS independently
'''
L = 5
timesteps = 5
testTracks = generate_tracks(1, L, 1, 3, 1, timesteps - 1)
(listOfPosLists, video) = generate_posits(testTracks)
tracks = link_tracks(listOfPosLists)
'''
