from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram, plot_distribution
from qiskit_aer.primitives import SamplerV2
import matplotlib.pyplot as plt

sampler = SamplerV2()

circ = QuantumCircuit(2, 1)

circ.h(0)
circ.cx(0, 1)
circ.measure_all()

circ.draw("mpl")

result = sampler.run([circ], shots=500).result()
counts = result[0].data['meas'].get_counts()

plot_distribution(counts)
plt.show()