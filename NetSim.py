



import numpy as np 


from utils import * 







# a class to represent a node in the network
class Node (object) : 

    def __init__(self, coords, N, f, G_t, G_r) : 
        self.coords = coords
        self.N = N # number of antennas
        self.G_t = G_t # Tx antenna gain (dBi)
        self.G_r = G_r # Rx antenna gain (dBi)
        self.f = f # frequency (Hz)
        self.wavelength = c / f
        self.d = 0.5 * self.wavelength # antenna spacing (half-wavelength)
        self.signal = None # signal to transmit

    def add_signal(self, signal = None) : 
        if signal is None : 
            self.signal = generate_bpsk(self.N)
        else : 
            self.signal = signal
    

    

# a class to represent a network of nodes
class NetSim (object) : 

    def __init__(self, nodes) : 
        self.nodes = nodes
    



def transmit(node1, node2, P_t) : 

    distance = euclidean_distance(node1.coords, node2.coords)
    angle = angle_of_arrival(node1.coords, node2.coords)
    
    PL = FSPL(distance, node1.f)
    h = generate_rayleigh_channel(node1.N)
    
    w_tx = beamforming_weights(angle, node1.N)
    w_rx = beamforming_weights(-angle, node2.N)

    # compute received signal
    signal = np.dot(w_rx, h * np.dot(w_tx, node1.signal))
    signal = np.sqrt(P_t) * signal / np.sqrt(PL)
    
