from pyclothoids import Clothoid
import math 

def calculate_path(initial_position, destination):
    """
    Use Clothoid library to create drivable path
    """
    destination['orientations'][0] = (destination['orientations'][0]/1000)%(2*math.pi) 
    clothoid0 = Clothoid.G1Hermite(initial_position['x'], initial_position['y'], initial_position['orientations'][0],
                                        destination['x'],       destination['y'],      destination['orientations'][0])
    
    trajectory = [];  npts = 80
    sample_points = [clothoid0.length * m/(npts-1) for m in range(0,npts)]
    for i in sample_points:
        theta = clothoid0.Theta(i)%(2*math.pi)*1000
        trajectory.append ({ 'x':clothoid0.X(i), 'y':clothoid0.Y(i), 'orientations':[theta,0], 'time': None})

    return {'trajectory': trajectory, 'operation':'driving'}  
