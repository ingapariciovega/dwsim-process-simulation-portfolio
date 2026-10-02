# Study 01 — Adiabatic mixing baseline

All numbers below are invented for a teaching example.

| Input | Stream A | Stream B |
| --- | --- | --- |
| Material | Pure liquid water | Pure liquid water |
| Mass flow | 1,000 kg/h | 500 kg/h |
| Temperature | 20 °C | 60 °C |
| Pressure basis | 2 bar absolute | 2 bar absolute |

Independent hand-check assumptions: steady state; no reaction; no heat exchange; negligible kinetic/potential energy changes; one liquid phase; identical constant specific heat; no modeled pressure loss.

Mass balance: outlet = 1,500 kg/h.

Ideal mixing temperature = (1,000 × 20 + 500 × 60) / 1,500 = **33.333 °C**. This is a constant-Cp theoretical baseline, not a simulator result. Temperature-dependent enthalpy can yield a small difference.

For the future model: choose and justify an appropriate water property package, configure units consistently, preserve the pressure basis and compare mass/energy closure. Document tolerance before accepting the run. Do not force simulator results to equal the ideal calculation by changing physical inputs.
