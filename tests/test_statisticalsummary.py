import particles.trackgeneration
import particles.statisticalsummary

def test_statisticalsummary():
    tracks = particles.trackgeneration.generate_tracks('brownian',10,.4,.2,1,100)
    simulated,predicted = particles.statisticalsummary.compute_statistics(tracks,tracks)
    assert simulated == predicted
    assert simulated >= 0

