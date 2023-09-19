
import math
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 3e8  # Speed of light (m/s)
frequency = 2.4e9  # Frequency (e.g., 2.4 GHz for WiFi)
wavelength = c / frequency  # Wavelength (m)



def FSPL(d, f):
    c = 3 * 10**8  # Speed of light in meters per second
    FSPL = 20 * np.log10(d) + 20 * np.log10(f) + 20 * np.log10(c) - 147.55
    return FSPL


def generate_rician_channel(K_factor, N):
    """Generate a Rician fading channel coefficient."""
    h_los = np.sqrt(K_factor / (K_factor + 1))
    h_nlos = (np.random.randn(N) + 1j*np.random.randn(N)) / np.sqrt(2)
    h = h_los + np.sqrt(1 / (2*(K_factor + 1))) * h_nlos
    return h

def generate_rayleigh_channel(N):
    """Generate a Rayleigh fading channel coefficient."""
    h = (np.random.randn(N) + 1j*np.random.randn(N)) / np.sqrt(2)
    return h

# Beamforming weights for transmitter to focus energy towards the user
def beamforming_weights(angle, N):
    """Compute weights to steer a beam in the specified direction."""
    n = np.arange(N)
    weights = np.exp(-1j * k * n * d * np.sin(angle))
    return weights / np.sqrt(N)  # Normalized weights


# calculate euclidean distance between two points
def euclidean_distance(coords1, coords2):
    """Compute the Euclidean distance between two points."""
    return np.sqrt(np.sum((coords1 - coords2)**2))

# calculate angle of arrival
def angle_of_arrival(coords1, coords2):
    """Compute the angle of arrival between two points."""
    x1, y1 = coords1
    x2, y2 = coords2
    return np.arctan2(y2 - y1, x2 - x1)

# calculate BER between two signals
def ber(s1, s2):
    """Compute the bit error rate (BER) between two signals."""
    return np.sum(s1 != s2) / len(s1)



# generate a BPSK signal 
def generate_bpsk(N):
    """Generate a random BPSK symbol."""
    return 2 * np.random.randint(2, size=N) - 1

# generate a QPSK signal
def generate_qpsk(N):
    """Generate a random QPSK symbol."""
    return (2 * np.random.randint(2, size=N) - 1) / np.sqrt(2)

# generate a QAM signal
def generate_qam(N):
    """Generate a random QAM symbol."""
    return (2 * np.random.randint(2, size=N) - 1) / np.sqrt(2)