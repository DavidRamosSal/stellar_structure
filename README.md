# stellar_structure
Solution to the stellar structure equations for a static compact object in GR given real tabulated dense matter equations of state.

# Setup
If you use conda it's always a good idea to work on a clean environment

```
conda create -n stellarStructure python=3.7
conda activate stellarStructure
```
Then, proceed to clone this repository

```
git clone https://github.com/DavidRamosSal/stellar_structure.git
```

Finally install the required libraries

```
pip install -r requirements.txt
```

# Usage
Copy any numerical equation of state of your interest (it should have three columns 1. baryon density, 2. pressure (p/c $^2$) and 3. energy density ($\epsilon$/c $^2$)) in `equationsOFState/numerical` and run:

```
python3 main.py
```

Raw data will be saved in `results/$nameOfTheEOSFile$`. The profiles corresponding to a central density of 10 $^{n}$ g/cm $^3$ will be saved as `results/$nameOfTheEOSFile$/$n$.dat` with the following columns:
 1. mass (solar masses)
 2. pressure (p/c $^2$)
 3. density (epsilon/c $^2$)
 4. $\nu$ metric function
 5. $\lambda$ metric function
 6. radius (km)

The consolidated results are saved in `results/$nameOfTheEOSFile$/$MRrhoc$.dat` with columns: 
1. radius (km)
2. mass (solar masses)
3. density (g/cm $^3$)

# Example
In `example` you can find the results obtained with the 37 dense matter EOSs included on this repository. The [RAnalysis notebook](https://nbviewer.org/github/DavidRamosSal/stellar_structure/blob/master/example/RAnalysis.ipynb) contains an analysis of those results.

# Docs
The [Stellar_structure_manual notebook](https://nbviewer.org/github/DavidRamosSal/stellar_structure/blob/master/docs/staticStructureManual.ipynb) in `example` gives an in-depth description and validation of the integration routine.
