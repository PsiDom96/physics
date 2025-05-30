# Vibr

**Vibr** is a Python-based tool for simulating mechanical vibrations in physical systems. It aims to provide an accessible, modular framework for importing 3D geometries, defining material and boundary conditions, and solving for vibrational behavior in time or frequency domains.

## 🚧 Project Status

Vibr is currently under active development. Early versions focus on 2D and 3D geometries built from standard primitives or imported CAD files. Future releases will expand into acoustic wave coupling, visualization, and real-time interactivity.

---

## ✨ Features (In Progress)

### ✅ Current Features
- **Import CAD Geometry**
  - Load `.STEP`, `.STL`, or programmatically generated geometries
  - Associate material properties and define geometry metadata
  - Optional meshing tools using `pygmsh`, `meshio`

- **Simulation Modes**
  - Specify the type of vibration analysis to perform:
    - Free vibration / modal analysis
    - Forced vibration with external sources
    - Time-domain propagation under initial or boundary conditions

- **Temporal Setup**
  - Define initial displacement or velocity fields
  - Apply time-dependent boundary conditions or driving functions

- **Visualization**
  - Plot displacement, velocity, or modal profiles
  - Animate time-domain results with `matplotlib` or export to HTML

---

## 🛠️ Installation

Clone the repo and set up a virtual environment:

```bash
git clone https://github.com/yourusername/vibr.git
cd vibr
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
