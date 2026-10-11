# Mechanistic Ocular Modelling: Vitreous Anti-VEGF Kinetics

A Python simulation modelling the pharmacokinetics and clearance rates of intravitreal ranibizumab injections using ordinary differential equations (ODEs). 

This project bridges the gap between clinical vision science (MOptom/MSc IOVS) and mechanism-driven mathematical biology, moving past purely statistical machine learning approaches to model the literal physical boundaries of the ocular environment.

## The Mathematics
The rate of drug elimination from the vitreous humor over time is modeled using a first-order kinetic decay equation:

\[\frac{dC}{dt} = -k \cdot C\]

Where:
* **C:** Concentration of the anti-VEGF agent (\(mg/L\))
* **t:** Time (\(Days\))
* **k:** Elimination rate constant (\(0.075 \text{ day}^{-1}\), derived from an average vitreous half-life of ~9 days)

## Clinical Variables Applied
* **Initial Dosage (\(C_0\)):** \(10.0 \text{ mg/L}\)
* **Simulation Timeline:** 60 Days
* **Therapeutic Floor:** Set at \(1.0 \text{ mg/L}\) to visualize the exact functional window before reinjection parameters are clinically indicated.

## How to Run
This model requires Python 3.x along with `numpy`, `scipy`, and `matplotlib`.
