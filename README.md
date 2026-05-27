<p align="center">
  <h1 align="center">MDSimulator</h1>
  <p align="center">
    <b>A Python-Tkinter GUI for Automating GROMACS Molecular Dynamics Simulations</b><br>
    <i>Computational chemistry · GROMACS · Molecular dynamics · Linux</i>
  </p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/GROMACS-MD%20Engine-0A66C2?style=flat-square" alt="GROMACS">
  <img src="https://img.shields.io/badge/Platform-Linux-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux">
  <img src="https://img.shields.io/badge/Interface-Tkinter%20GUI-4EAA25?style=flat-square" alt="Tkinter">
  <img src="https://img.shields.io/badge/IP-Copyright%20Filed%20(IPO%20Pakistan%202023)-orange?style=flat-square" alt="IP">
</p>

---

## Overview

MDSimulator is an open-source Python desktop application that provides a guided graphical interface for running **GROMACS molecular dynamics (MD) simulations** on Linux. Rather than constructing and running GROMACS commands manually, users work through a visual, step-by-step workflow — from topology generation to production MD and analysis — with each step unlocked sequentially after the previous one completes successfully.

The application is designed for researchers who are new to MD simulation or who want a reproducible, GUI-driven workflow for routine protein or protein–ligand simulations.

> **Intellectual Property:** MDSimulator is a registered copyright (Intellectual Property Organisation of Pakistan, 2023).

---

## Key Features

| Feature | Description |
|---|---|
| **Step-by-step GUI** | Six sequential MD stages presented as clearly labelled buttons; each stage unlocks only after the previous completes |
| **Guided configuration** | MDP files directory and output directory are defined through file-browser dialogs |
| **Full GROMACS pipeline** | Covers all standard MD stages from topology to production run |
| **Integrated analysis module** | Post-simulation analysis launched from within the same interface |
| **Sequential stage locking** | Prevents out-of-order execution to avoid common user errors |
| **Linux-native** | Designed for Linux workstations and HPC login nodes with GROMACS installed |

---

## MD Simulation Workflow

MDSimulator orchestrates six standard GROMACS stages through a sequential GUI:

```
┌───────────────────────────────────────────────────────────────────┐
│                          MDSimulator GUI                          │
│                                                                   │
│  [1. Generate Topology] ──► [2. Define Box & Solvate]             │
│                                            │                      │
│                                    [3. Add Ions]                  │
│                                            │                      │
│  [6. Production MD] ◄── [5. Equilibration] ◄── [4. Energy Min.]  │
│                                                                   │
│                        [Analysis]  [Exit]                         │
└───────────────────────────────────────────────────────────────────┘
```

### Stage descriptions

| Stage | GROMACS command | Description |
|---|---|---|
| **1. Generate Topology** | `gmx pdb2gmx` | Converts input PDB to GROMACS topology and coordinate files using the selected force field |
| **2. Define Box & Solvate** | `gmx editconf` + `gmx solvate` | Defines the periodic simulation box and fills it with explicit solvent (TIP3P or user-defined) |
| **3. Add Ions** | `gmx grompp` + `gmx genion` | Neutralises the system by adding counterions; optionally adjusts salt concentration |
| **4. Energy Minimisation** | `gmx grompp` + `gmx mdrun` | Steepest-descent or L-BFGS energy minimisation to remove steric clashes before dynamics |
| **5. Equilibration** | `gmx grompp` + `gmx mdrun` | NVT and/or NPT equilibration to stabilise temperature and pressure |
| **6. Production MD** | `gmx grompp` + `gmx mdrun` | Full production dynamics run; generates trajectory for downstream analysis |
| **Analysis** | `gmx rms`, `gmx rmsf`, etc. | Post-simulation trajectory analysis |

---

## Prerequisites

| Requirement | Notes |
|---|---|
| **Linux** | Tested on Ubuntu; compatible with standard Linux distributions |
| **Python 3.x** | With `tkinter` — usually pre-installed (`python3-tk`) |
| **GROMACS** | Installed and available on `PATH`; verify with `gmx --version` |
| **MDP files** | Pre-configured GROMACS parameter files for each simulation stage |

### MDP files

MDSimulator reads MDP (molecular dynamics parameter) files from a user-defined directory. Standard MDP files for ions, energy minimisation, NVT equilibration, NPT equilibration, and production MD must be prepared before running the GUI. Example MDP files for standard protein simulations are provided in the `mdp_files/` directory of this repository.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/rashid-bioinfo/MDSimulator.git
cd MDSimulator
```

### 2. Install Python dependencies

MDSimulator uses only the Python standard library (`tkinter`, `os`). No additional packages are required.

Ensure `tkinter` is available:

```bash
sudo apt install -y python3-tk
```

### 3. Ensure GROMACS is installed

```bash
# Install GROMACS (Ubuntu/Debian)
sudo apt install -y gromacs

# Or load via module system on HPC
module load gromacs/2023

# Verify
gmx --version
```

---

## Usage

### Launch the GUI

```bash
cd MDSimulator/Source_Files
python3 MD_Simulator.py
```

### Workflow

1. **Set directories** — Define the folder containing your MDP files and the output directory where results will be written.
2. **Generate Topology** — Click the button, select your input PDB file and force field, and confirm. The button turns green on success.
3. **Define Box & Solvate** — Set box type, dimensions, and solvent model.
4. **Add Ions** — Neutralise the system; set ion concentrations if needed.
5. **Energy Minimisation** — Run steepest-descent minimisation. Monitor convergence in the terminal.
6. **Equilibration** — Run NVT then NPT equilibration using the provided MDP files.
7. **Production MD** — Launch the full MD run. This step may take hours to days depending on system size and hardware.
8. **Analysis** — Use the built-in analysis panel to calculate RMSD, RMSF, and other standard observables.

### Repository structure

```
MDSimulator/
├── Source_Files/
│   └── MD_Simulator.py       # Main application
├── MD_Simulator-app/         # Packaged application files
└── mdp_files/                # Example MDP parameter files
```

---

## Citation

If you use MDSimulator in your research or teaching, please acknowledge:

```
Hussain, R. (2023). MDSimulator: A Python-Tkinter GUI for GROMACS Molecular Dynamics Simulations.
Intellectual Property Organisation of Pakistan. Copyright Registration 2023.
```

---

## Author

**Rashid Hussain**, PhD, RSci, MRSC  
Postdoctoral Researcher in Computational Pathology  
Humanitas Research Hospital (IRCCS), Milan, Italy  
[rashid.bioinfo@gmail.com](mailto:rashid.bioinfo@gmail.com) · [https://rashid-bioinfo.github.io](https://rashid-bioinfo.github.io)

---

## License

This software is distributed for academic and non-commercial research use. All rights are reserved by the author. The registered copyright (IPO Pakistan, 2023) covers the source code and associated materials. For commercial licensing enquiries, contact [rashid.bioinfo@gmail.com](mailto:rashid.bioinfo@gmail.com).

---

<p align="center">
  <i>Molecular Dynamics · GROMACS · Computational Chemistry · Python GUI</i>
</p>
