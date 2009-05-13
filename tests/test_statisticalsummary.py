import particles.trackgeneration
import particles.statisticalsummary
import particles.position

def test_statisticalsummary():
    tracks = particles.trackgeneration.generate_tracks('brownian',10,.4,.2,1,100)
    simulated,predicted = particles.statisticalsummary.compute_statistics(tracks,tracks)
    assert simulated == predicted
    assert simulated >= 0

def test_singleframe():
    tracks = (0,[particles.position.Position(0,0)])
    simulated,predicted = particles.statisticalsummary.compute_statistics(tracks,tracks)
    assert simulated == predicted == 0 



