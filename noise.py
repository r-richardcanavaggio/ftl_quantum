from qiskit_aer.primitives import SamplerV2
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


circ = QuantumCircuit(1, 1)

circ.z(0)
circ.measure_all()

sampler = SamplerV2()
job = sampler.run([circ], shots=500)

result = job.result()
counts = result[0].data.meas.get_counts()

plot_histogram(counts)
plt.show()
