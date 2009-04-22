import numpy as np
import random
import math


def generate_tracks(model,square_area_size,density,diffusion_coefficient,time_step,total_steps):
	'''
	This is the primary function that is used to generate tracks in the main program
	All other functions in this code are required by this function.
	The input values are from the configuration file
	The output is a list of tracks, each track a tuple of:
		starting time, list of positions
	for each particle in the simulation
	'''
	L = int(square_area_size)
	T = int(total_steps)
	del_t = time_step
	D = diffusion_coefficient
	sigma = math.sqrt(2*D*del_t)
	rho = density
	num = int(np.ceil(rho*L*L))
	TrackGeneratorList = []
	Tracks = []
	t0 = 0
	for i in xrange(num):
	 	TrackGeneratorList.append(EachParticle(t0,RandomPositionGenerator(L)))
	for n_step in xrange(T):
		NewTrackList = []
		t = t0 + n_step*del_t
		for TrackGen in TrackGeneratorList:
			if(TrackGen.active == 1):
				TrackGen.update(L,sigma)
				if(TrackGen.active == 0):
					NewTrackList.append(EachParticle(t,RandomPositionGenerator(L)))
		for TrackGen in NewTrackList:
			TrackGeneratorList.append(TrackGen)
	for TrackGen in TrackGeneratorList:
		Tracks.append(TrackGen.give_the_track())
	return Tracks
	
class Position(object):
	'''
	This is a position object which stores two integer value positions
	along X and Y axes respectively
	'''
	def __init__(self,x,y):
		assert (x % 1 == 0 and y % 1 == 0),"Square-size is not integral"
		self.x = x
		self.y = y

def RandomPositionGenerator(L):
	'''
	This method generates a random starting position for a particle
	between the limits 0 and L-1
	'''
	assert (L % 1 == 0), "Square-size is not integral"
	x = int(np.ceil(random.uniform(0,L-1)))
	y = int(np.ceil(random.uniform(0,L-1)))
	return Position(x,y)

class EachParticle(object):
	def __init__(self,t0,pos):
		assert (pos.x % 1 == 0 and pos.y % 1 == 0), "Non-integral positions"
		self.poslist = []
		self.t0 = t0
		self.poslist.append(pos)
		self.active = 1
		
	def update(self,L,sigma):
		'''
		Every time update() is called, a new position is added to the list
		based on Brownian dynamics
		'''
		assert len(self.poslist) > 0, "Track initialized badly"
		self.lastpos = self.poslist[-1]
		self.newX = int(np.ceil(random.gauss(self.lastpos.x,sigma)))
		self.newY = int(np.ceil(random.gauss(self.lastpos.y,sigma)))
		if(self.newX<0 or self.newX>L-1 or self.newY<0 or self.newY>L-1):
			self.active = 0
		else:
			self.poslist.append(Position(self.newX,self.newY))
	def give_the_track(self):
		'''
		give_the_track() just returns the track in the form required by the 
		main program
		'''
		return (self.t0,self.poslist)