import scipy.io.wavfile
import numpy as np
from scipy.signal import lfilter
from scipy.fft import fft, fftfreq

# [sample_rate, pcm_data] = scipy.io.wavfile.read('/Users/kayleem/Documents/english_panogram.wav')
# [sample_rate, pcm_data] = scipy.io.wavfile.read('/Users/kayleem/Downloads/Harvard list 01.wav')
[sample_rate, pcm_data] = scipy.io.wavfile.read('/Users/kayleem/aiueo.wav')


# https://clagnut.com/blog/2380/#English_phonetic_pangrams
# With tenure, Suzie’d have all the more leisure for yachting, but her publications are no good.

# https://www.kuniga.me/blog/2021/05/13/lpc-in-python.html

amplitudes = np.array(pcm_data)
print(amplitudes.shape)
amplitudes = 0.9*amplitudes/max(abs(amplitudes))
print(sample_rate)

from scipy.signal import resample
target_sample_rate = 8000
target_sample_rate = sample_rate
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
        x[offset : nw + offset] += B[i, :] * w

    return x

from scipy.signal.windows import hann

from math import floor
sym = False # periodic
# window_length = 0.03
window_length = 0.03
w = hann(floor(window_length*sample_rate), sym)

def make_matrix_X(input_signal_block, number_poles):
    """
    [ x_1,     0,   0,   0,     0]       a_1        b_1
    [ x_2,   x_1,   0,   0,     0]       a_2
    [ ...,   ..., ..., ...,   ...]       ...
    [ x_n, x_n-1, ..., ..., x_n-p]       a_p        b_n

    Xa = b
    """
    n = len(input_signal_block)
    # [x_n, ..., x_1, 0, ..., 0]
    zero_padded_input = np.concatenate([input_signal_block[::-1], np.zeros(number_poles)])

    X = np.zeros((n - 1, number_poles))
    for i in range(n - 1):
        offset = n - 1 - i
        X[i, :] = zero_padded_input[offset : offset + number_poles]
    return X

def solve_lpc(input_signal_block, number_poles, ii):
    b = input_signal_block[1:]

    X = make_matrix_X(input_signal_block, number_poles)

    a = np.linalg.lstsq(X, b.T, rcond=-1)[0]

    e = b - np.dot(X, a)

    power = np.sum(np.abs(a)) + 1
    # print('power', power)
    g = np.var(e)
    voicedness = np.max(fft(e))

    return [a, g, voicedness]

def lpc_encode(input_signal, number_poles, window):
    blocks = create_overlapping_blocks(input_signal, window)

    [number_blocks, block_length] = blocks.shape

    A = np.zeros((number_poles, number_blocks))
    G = np.zeros((1, number_blocks))
    V = np.zeros((1, number_blocks))

    for i in range(number_blocks):
        [a, g, v] = solve_lpc(blocks[i, :], number_poles, i)

        A[:, i] = a
        G[:, i] = g
        V[:, i] = v

        # check = run_source_filter(a, g, len(w))
        # print(g)
        # print(a)
        # if (np.max(check) > 1):
        #     import matplotlib.pyplot as plt
        #     plt.plot(B[i, :])
        #     plt.plot(check)
        #     plt.show()

    return [A, G, V]

def run_source_filter(a, g, v, block_size):
    from scipy import signal
    t = np.linspace(0, block_size/sample_rate, block_size, endpoint=False)
    square = np.convolve(signal.sawtooth(2 * np.pi * 200 * t), np.ones(20)/20, mode='same')
    # square = signal.gausspulse(2 * np.pi * 200 * t)
    src = np.sqrt(g)*(np.random.randn(block_size)* (1-v) + square * v) # noise
    # src = np.sqrt(g)*( square) # noise
    # src = np.random.randn(block_size) # noise

    b = np.concatenate([np.array([-1]), a])
    # from scipy import signal
    #
    # return signal.sawtooth(2 * np.pi * 5 * np.linspace(0, 1, 500))

    x_hat = lfilter([1], b.T, src.T).T
    # x_hat_2 = np.convolve(src, b, mode='same')
    if False:
        print('a', a)
        print('b', b)
        print('src', src)
        print('x_hat', x_hat)
        print('x_hat_2', x_hat_2)
        import matplotlib.pyplot as plt
        fig, axs = plt.subplots(2)
        # fig.suptitle('Vertically stacked subplots')
        axs[0].plot(src)
        axs[0].plot(x_hat, label='x_hat')
        axs[1].plot(x_hat_2, label='x_hat_2')
        plt.show()

    # return square
    # convert Nx1 matrix into a N vector
    return np.squeeze(x_hat)

def lpc_decode(A, G, V, w, lowcut = 0):

    [ne, n] = G.shape
    nw = len(w)
    [p, _] = A.shape

    B_hat = np.zeros((n, nw))

    for i in range(n):
        B_hat[i,:] = run_source_filter(A[:, i], G[:, i], V[:, i], nw)

    # recover signal from blocks
    x_hat = add_overlapping_blocks(B_hat, w); #### ADD W

    return x_hat


import sounddevice as sd
if True:
    print("encoding")
    # Encode
    p = 12 # number of poles
    [A, G, V] = lpc_encode(amplitudes, p, w)

    # Print stats
    original_size = len(amplitudes)
    model_size = A.size + G.size
    print('Original signal size:', original_size)
    print('Encoded signal size:', model_size)
    print('Data reduction:', original_size/model_size)

    xhat = lpc_decode(A, G, V/np.max(V), w)

    scipy.io.wavfile.write("example.wav", sample_rate, np.clip(xhat, -1, 1))
    print('done')


    sd.play(np.clip(xhat, -1, 1), sample_rate)
    print ('number of windows', len(G.T))


# B = create_overlapping_blocks(amplitudes, w)
# print(B)
# # B_hat = np.zeros((n, nw))
# x_hat = add_overlapping_blocks(B, w)
# scipy.io.wavfile.write("example.wav", sample_rate, x_hat)
# print('done')


# import matplotlib.pyplot as plt
# N = len(amplitudes)
# T = 1/sample_rate
# yf = fft(amplitudes)
# xf = fftfreq(N, T)[:N//2]
# plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
# plt.show()
#
# plt.plot(amplitudes)
# plt.plot(xhat)
# plt.show()
#
#
# plt.plot(V.T / np.max(V.T))
# plt.plot(G.T / np.max(G.T))
# plt.show()



parse_coeff = lambda s: np.array(np.matrix(s)).reshape((12,))

c_th =  parse_coeff(
    "2.43923636 -2.64129344  2.15005271 -1.55283568  1.13906817 -0.69582556 0.19063709 -0.29383354  0.55420677 -0.41895927  0.1725741  -0.04795764"
)
c_a =  parse_coeff(
    "1.8448447  -1.23389746  1.40104654 -1.74555808  1.16050924 -1.14664295 1.42746685 -1.06478313  0.72169741 -0.72590777  0.36427365 -0.01407909"
)
c_i = parse_coeff(
    "1.6663576  -0.88822612  0.98289525 -1.45009406  1.1248583  -1.13859395 1.16073052 -0.7706534   0.68836604 -0.57902417  0.40804387 -0.20902199"
)
c_u = parse_coeff(
    " 1.38080136 -0.61115419  0.99048757 -1.09019545  0.83681947 -0.97022035 0.83768675 -0.76752959  0.69292654 -0.48661999  0.3274398  -0.14552513"
) #90
c_e = parse_coeff(
    " 2.31505662 -2.38902875  2.56148133 -2.73287668  2.11523497 -2.05637972 2.14978711 -1.66866073  1.32213137 -0.96315903  0.48444859 -0.14547988"
)
c_o = parse_coeff(
    " 1.6239518  -0.79864799  1.02957642 -1.33435367  0.98065684 -1.14542472 1.04408385 -0.76258512  0.56975085 -0.49693079  0.54559587 -0.26560834"
)
c_k = parse_coeff(
    " 1.54987431e+00 -1.68776583e+00  2.21520437e+00 -1.94132396e+00 2.15324671e+00 -1.99725320e+00  1.43383996e+00 -1.29800187e+00 7.12071493e-01 -5.20947705e-01  3.05154201e-01 -6.07391156e-04"
)
c_s = parse_coeff(
    "1.14479255 -2.01286373  2.22742901 -2.74898426  3.11997732 -2.67087954 2.69430462 -2.01652382  1.58509054 -1.10118652  0.53964641 -0.36632058"
)
c_sh = parse_coeff(
    "1.65047921 -2.26174702  2.63395928 -3.00464413  2.91749197 -2.70693571 2.49675472 -2.01051868  1.4739271  -1.03165426  0.56659214 -0.16553336"
)
c_t = parse_coeff(
    " 1.59637194 -0.98981317  1.3499289  -1.65344189  1.32625628 -1.30360825 1.10031068 -1.10267924  0.89656564 -0.4265637   0.52905503 -0.35174282"
)

start, end = 1, 1
while True:
    windowstring = input('window number: ')
    if (windowstring == ""):
        tmp = end - start
        start = end
        end = end + tmp
    elif ('-' in windowstring):
        start, end = windowstring.split('-')
        start = int(start)
        end = int(end)
    elif ('th' in windowstring):
        B_hat = np.zeros((50, len(w)))
        for i in range(50):
            # print(A[:, start], c_th, A[:, start].shape, c_th.shape)
            result = run_source_filter(c_th, G[:, start], V[:, start], len(w))
            B_hat[i,:] = result
        x_hat = add_overlapping_blocks(B_hat, w)
        sd.play(np.clip(x_hat, -1, 1), sample_rate)
        continue
    elif 'aiueo' in windowstring:
        B_hat = np.zeros((200, len(w)))
        output_index = 0
        for coeffindex, coeff in enumerate((c_a, c_o, c_i, c_k, c_u, c_u, c_k, c_i, c_i)):
            is_vowel = coeff is c_a or coeff is c_i or coeff is c_u or coeff is c_e or coeff is c_o
            for i in range(output_index,output_index+10):
                B_hat[i,:] = run_source_filter(
                    coeff,
                    0.00001,
                    0.99  if is_vowel else 0.0,
                    len(w)
                )
            if is_vowel:
                output_index += 10
            else:
                output_index += 5

        x_hat = add_overlapping_blocks(B_hat, w)
        sd.play(np.clip(x_hat, -1, 1), sample_rate)
        continue
    elif ('r' in windowstring):
        B_hat = np.zeros((50, len(w)))
        print('repeating window', start)
        print('  coefficients=', A[:, start])
        print('  gain=', G[:, start])
        for i in range(50):
            result = run_source_filter(A[:, start], G[:, start], 0.5, len(w))
            B_hat[i,:] = result
        x_hat = add_overlapping_blocks(B_hat, w)
        sd.play(np.clip(x_hat, -1, 1), sample_rate)
        continue;
    else:
        start = int(windowstring)
        end = start + 1
    print ('play window ', start, end)


    B_hat = np.zeros((end - start, len(w)))
    for i in range(end - start):
        result = run_source_filter(A[:, start+i], G[:, start+i], 0.5, len(w))
        B_hat[i,:] = result
    x_hat = add_overlapping_blocks(B_hat, w)
    sd.play(np.clip(x_hat, -1, 1), sample_rate)

