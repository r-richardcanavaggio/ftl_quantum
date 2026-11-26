from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_distribution
import matplotlib.pyplot as plt


service = QiskitRuntimeService()

backend = service.least_busy()
sampler = SamplerV2(mode=backend)

bell_circ = QuantumCircuit(2, 1)

bell_circ.h(0)
bell_circ.cx(0, 1)
bell_circ.measure_all()

bell_circ = transpile(bell_circ, backend)
job = sampler.run([bell_circ], shots=500)

result = job.result()
counts = result[0].data['meas'].get_counts()

plot_distribution(counts)
plt.savefig("bell_distribution.png")
plt.close()
