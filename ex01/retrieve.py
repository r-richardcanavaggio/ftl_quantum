from qiskit_ibm_runtime import QiskitRuntimeService
from dotenv import load_dotenv
import os


# load_dotenv()
# api_key = os.getenv("IBM_API_KEY")


# QiskitRuntimeService.save_account(
#     token=api_key,
#     name="open",
#     instance="crn:v1:bluemix:public:quantum-computing:us-east:a/675ea1bfa73048cab7730493ccc60761:785baacf-782b-4fb4-9fcd-c35745d9c9b6::",
#     set_as_default=True
# )

service = QiskitRuntimeService()

backends = service.backends()

print("Real quantum computers:")
for backend in backends:
    status = backend.status()
    print(f"{backend.name} has {status.pending_jobs} queues with {backend.num_qubits} qubits")


# print(service.jobs())
