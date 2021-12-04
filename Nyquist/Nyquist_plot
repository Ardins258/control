import matplotlib.pyplot as plt
import scipy.signal as signal

rndm = signal.TransferFunction([1],[1,2,15], dt = 0.06)
w, H = signal.dfreqresp(rndm)

plt.figure()
plt.plot(H.real, H.imag, "b")
plt.plot(H.real, -H.imag, "r")
plt.title("Nyquist Plot")
plt.show()
