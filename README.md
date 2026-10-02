# DWSIM Process Simulation Portfolio

**Status: study specifications prepared; no DWSIM simulation has been executed or validated in this repository.**

This collection starts with a transparent study basis and an independent hand-check for a simple mixing case. It does not include a completed `.dwxmz` model, simulated results or screenshots.

## Initial study: adiabatic water mixing

See `01-water-mixing.md`. Two invented liquid-water streams mix at an assumed common pressure with no heat loss. A constant-heat-capacity hand calculation predicts the mixed temperature. A future DWSIM run must record its actual property model and compare the energy balance against this approximation.

Run `python hand_check.py` for the theoretical baseline. Its output is **not a DWSIM result**.

## Reproducibility standard

For a future completed study include simulator version, compounds, property method and rationale, unit system, feed specifications, flowsheet file, convergence status, exported results, independent balance check, sensitivity range and limitations. Fill `validation-record.md` only after execution.

Official resource: [DWSIM](https://dwsim.org/), accessed 2026-10-01.

## Español

Bases de simulación y validación. El primer caso propone mezclar dos corrientes de agua y comparar el modelo con un balance ideal. La simulación DWSIM está pendiente; no se presenta como trabajo concluido ni como dominio acreditado del software.
