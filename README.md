# ipms-test-instances

Contains all of the test instances used to benchmark the **Hybrid SMA+ABM** algorithm developed in the paper: ***Towards hybridization of multi-agent simulation and metaheuristics applied to selective deconstruction***.

## Printing results

File `./printResults.py` displays all of the informations about runs.
Requires lib :
   - `matplotlib`
   - `numpy`
   - `statistics`
  
It also plots a boxplot graph representing the evolution of the fitness during the resolution.

Utilisation : `./printResults.py folder-of-to-print`