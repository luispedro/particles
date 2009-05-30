====================
Basic Architechture
====================

This is the result of the in-class discussion of the general architechture of particles.

The main body should look like:

::

    tracks = generate_tracks(modelparams)
    video = generate_video(tracks)
    positions = detect_particles(video)
    results = link_tracks(positions)
    compute_print_statistics(tracks,results)

*Tracks* will be a list of tracks.

Each track will consist of a 2-element tuple *(t0,positions)* where *t0* is an integer (representing the starting
time of that track) and positions is a list of positions. Each position will be an instance of class Position.

::

    class Position(object):
        '''
        pos = Position(x,y)

        Represents a position.
        '''
        def __init__(self,x,y):
            self.x = x
            self.y = y

The argument for a special class to represent a position (instead of a simple tuple) was to make it more extensible
(in the future, it's easier to add properties to the position, such as shape and size of particles, or a 3rd dimension).

*video* will be a simple numpy 3-D array (2-D images + time) of uint8 numbers.

*positions* will simply be a list of lists of positions (objects of type class Position).

*results* should have the same form as *tracks*.

