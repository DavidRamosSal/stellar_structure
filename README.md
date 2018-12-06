# stellar_structure
Solution to the structure equations on GR given real tabulated dense matter equations of state.
# Files
* Static_SLy.ipynb - Solves the TOV equations for an specific EOS (SLy in this case) and computes the derivatives of the energy density profiles, okay results (derivatives always have problems).
* Sequences.ipynb - Solves the TOV equations using many equations of state for a range of central densities, generating different static sequences, good results.
* Numeric static solution_one.ipynb - Original integration method for the TOV equations using scipy methods, overkill and little control. Better documented than the rest (for now).
* Numeric static solution_two.ipynb - An attemp to solve the problem in a Lagrangian fluid description with the old methd, unsatisfactory.
* Physical_Const.py - File with all physical constants on cgs units.
