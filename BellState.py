from qiskit import *
from qiskit.providers.basic_provider import BasicSimulator
from qiskit.visualization import plot_histogram

qc = QuantumCircuit(2, 2)  
qc.h(0) 
qc.cx(0,1);
qc.measure(0, 0);
qc.measure (1,1);
qc.draw(output='mpl')
backend = BasicSimulator()

result = backend.run(qc, shots=2000).result()   

counts = result.get_counts()                    
plot_histogram(counts)
