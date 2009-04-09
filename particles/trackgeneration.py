''' as of now, track generation is just random assignment of coordinates'''
''' will soon import brownian basis'''
import numpy as np
import random

model = 'brownian'
square_area_size = 1000
density = 0.0005
diffusion_coefficient = 1
time_step = 1
total_steps = 1000



def generate_tracks(model,square_area_size,density,diffusion_coefficient,time_step,total_steps):
	L = square_area_size
	T = total_steps
	del_t = time_step
	D = diffusion_coefficient
	rho = density
	num = np.ceil(rho*L*L)
	TrackGeneratorList = []
	Tracks = []
	t0 = 0
	for i in xrange(num):
	 	TrackGeneratorList.append(EachTrackGenerator(t0,RandomPositionGenerator(L)))
	for n_step in xrange(T):
		for TrackGen in TrackGeneratorList:
			if(TrackGen.active == 1):
				TrackGen.update(L)
	for TrackGen in TrackGeneratorList:
		Tracks.append(TrackGen.give_the_track())
	return Tracks
	
class Position(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

def RandomPositionGenerator(L):
	x = np.ceil(random.uniform(0,L-1))
	y = np.ceil(random.uniform(0,L-1))
	return Position(x,y)

class EachTrackGenerator(object):
	poslist = []
	def __init__(self,t0,pos):
		self.t0 = t0
		self.poslist.append(pos)
		self.active = 1
	def update(self,L):
		self.nextpos = RandomPositionGenerator(L)
		self.poslist.append(self.nextpos)
	def give_the_track(self):
		return (self.t0,self.poslist)
