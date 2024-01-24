import scipy.io.wavfile
import numpy as np
from scipy.signal import lfilter

[sample_rate, pcm_data] = scipy.io.wavfile.read('/Users/kayleem/Documents/english_panogram.wav')
# [sample_rate, pcm_data] = scipy.io.wavfile.read('/Users/kayleem/Downloads/Harvard list 01.wav')


# https://clagnut.com/blog/2380/#English_phonetic_pangrams
# With tenure, Suzie’d have all the more leisure for yachting, but her publications are no good.

# https://www.kuniga.me/blog/2021/05/13/lpc-in-python.html

amplitudes = np.array(pcm_data)
print(amplitudes.shape)
amplitudes = 0.9*amplitudes/max(abs(amplitudes))
print(sample_rate)

from scipy.signal import resample
target_sample_rate = 8000
target_size = int(len(amplitudes)*target_sample_rate/sample_rate)

print("resample")
amplitudes = resample(amplitudes, target_size)
sample_rate = target_sample_rate

def create_overlapping_blocks(x, w, R = 0.5):
    n = len(x)
    nw = len(w)
    step = floor(nw * (1 - R))
    nb = floor((n - nw) / step) + 1

    B = np.zeros((nb, nw))

    for i in range(nb):
        offset = i * step
        B[i, :] = w * x[offset : nw + offset]

    return B

def add_overlapping_blocks(B, w, R = 0.5):
    [count, nw] = B.shape ## Change X to B
    step = floor(nw * R)

    n = (count-1) * step + nw

    x = np.zeros((n, ))

    for i in range(count):
        offset = i * step
        x[offset : nw + offset] += B[i, :]

    return x

from scipy.signal.windows import hann

from math import floor
sym = False # periodic
w = hann(floor(0.03*sample_rate), sym)

def make_matrix_X(x, p):
    n = len(x)
    # [x_n, ..., x_1, 0, ..., 0]
    xz = np.concatenate([x[::-1], np.zeros(p)])

    X = np.zeros((n - 1, p))
    for i in range(n - 1):
        offset = n - 1 - i
        X[i, :] = xz[offset : offset + p]
    return X

def solve_lpc(x, p, ii):
    b = x[1:]

    X = make_matrix_X(x, p)

    a = np.linalg.lstsq(X, b.T, rcond=-1)[0]

    e = b - np.dot(X, a)

    power = np.sum(np.abs(a)) + 1
    print('power', power)
    g = min(np.var(e), 1.0/power/2)

    return [a, g]

def lpc_encode(x, p, w):
    B = create_overlapping_blocks(x, w)

    [nb, nw] = B.shape

    A = np.zeros((p, nb))
    G = np.zeros((1, nb))

    for i in range(nb):
        [a, g] = solve_lpc(B[i, :], p, i)

        A[:, i] = a
        G[:, i] = g

        check = run_source_filter(a, g, len(w))
        print(g)
        print(a)
        if (np.max(check) > 1):
            import matplotlib.pyplot as plt
            plt.plot(B[i, :])
            plt.plot(check)
            plt.show()

    return [A, G]

def run_source_filter(a, g, block_size):
    src = np.sqrt(g)*np.random.randn(block_size, 1) # noise

    b = np.concatenate([np.array([-1]), a])
    # from scipy import signal
    #
    # return signal.sawtooth(2 * np.pi * 5 * np.linspace(0, 1, 500))

    print('b', b)
    x_hat = lfilter([1], b.T, src.T).T

    # convert Nx1 matrix into a N vector
    return np.squeeze(x_hat)

def lpc_decode(A, G, w, lowcut = 0):

    [ne, n] = G.shape
    nw = len(w)
    [p, _] = A.shape

    B_hat = np.zeros((n, nw))

    for i in range(n):
        B_hat[i,:] = run_source_filter(A[:, i], G[:, i], nw)

    # recover signal from blocks
    x_hat = add_overlapping_blocks(B_hat, w); #### ADD W

    return x_hat

print("encoding")
# Encode
p = 48 # number of poles
[A, G] = lpc_encode(amplitudes, p, w)

# Print stats
original_size = len(amplitudes)
model_size = A.size + G.size
print('Original signal size:', original_size)
print('Encoded signal size:', model_size)
print('Data reduction:', original_size/model_size)

xhat = lpc_decode(A, G, w)

scipy.io.wavfile.write("example.wav", sample_rate, np.clip(xhat, -1, 1))
print('done')



B = create_overlapping_blocks(amplitudes, w)
# print(B)
# # B_hat = np.zeros((n, nw))
# x_hat = add_overlapping_blocks(B, w)
# scipy.io.wavfile.write("example.wav", sample_rate, x_hat)
# print('done')


import matplotlib.pyplot as plt
plt.plot(amplitudes)
# plt.plot(G.T)
plt.plot(xhat)
plt.show()
