import otsu as ot
import position as ps
import numpy as np

def detect_particles(video):
    '''
    this function was used to detect the position of particles. 
    otsu method is used to calculate the threshold and the the 
    coordinates of the particles will be calculated.
    
    It can be tested with following code:
    import detect_particles as dp
    import numpy as np
    A = np.array([[
                    [1,0,1,0,4,5],
                    [7,1,3,1,5,1],
                    [1,5,1,4,0,1],
                    [0,1,8,1,4,7],
                    [3,2,4,5,2,0],
                    [1,5,1,4,0,1]],
                    [[0,1,3,1,5,9],
                    [1,0,1,4,0,9],
                    [0,2,0,0,2,9],
                    [1,0,1,0,4,5],
                    [1,0,1,4,0,9],
                    [0,1,0,1,4,7]]])
    dp.detect_particles(A)
    '''
    positions = []
    for i in range(video.shape[0]):
        pos = ps.Position(0,0)
        count = 0
        slice = video[i]
        threshold = ot.otsu(video[i])
        for j in range(video.shape[1]):
            for k in range(video.shape[2]):
                if (slice[j,k] < threshold):
                    slice[j,k] = 0
                else:
                    slice[j,k] = 1
                    pos.x += j
                    pos.y += k
                    count += 1

        pos.x /= count
        pos.y /= count
        positions.append(pos)

##        print threshold
##        print slice
##        print pos.x
##        print pos.y
##        print count
    return positions

