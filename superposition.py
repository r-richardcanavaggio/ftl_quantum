from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram, plot_distribution
from qiskit_aer.primitives import SamplerV2
import matplotlib.pyplot as plt


circ = QuantumCircuit(1, 1)

circ.h(0)
circ.measure_all()

circ.draw("mpl")

sampler = SamplerV2()
job = sampler.run([circ], shots=500)

result = job.result()
counts = result[0].data['meas'].get_counts()

# as_probabilities = dict((key, value / 500) for (key, value) in counts.items())
# plot_histogram(as_probabilities)
plot_distribution(counts)

plt.show()
