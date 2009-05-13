import particles.trackgeneration
import particles.statisticalsummary
import particles.position

def test_statisticalsummary():
    '''
    General test for the compute_statistics function
    '''
    tracks = particles.trackgeneration.generate_tracks('brownian',10,.4,.2,1,100)
    simulated,predicted = particles.statisticalsummary.compute_statistics(tracks,tracks)
    assert simulated == predicted
    assert simulated >= 0

def test_shortlived():
    '''
    This is to test the velocity function for particles that only show up in one
    frame
    '''
    flag = 0
    while 1 : 
        tracks = particles.trackgeneration.generate_tracks('brownian',10,.4,.2,1,100)
        zerotracks = []
        for i in xrange(len(tracks)):
            if len(tracks[i][1]) == 1:
                 zerotracks.append(tracks[i])
        if len(zerotracks) >= 2 : 
            flag = 1
        if flag :
            vel  = particles.statisticalsummary.traj_vel(zerotracks)
            break
    assert vel == 0 



