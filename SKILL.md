---
name: genpark-personal-agent-nocturnal-core-body-temperature-min-skill
version: "1.0.0"
description: "Zero-dependency circadian core body temperature (CBT) nadir modeler, distal-to-proximal vasodilation heat dump calculator, and phase response curve inflection timing scheduler."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Nocturnal Core Body Temperature Min Skill

Designed for **OpenClaw**, **Hermes**, and autonomous personal AI assistants to model circadian core body temperature (CBT) dynamics, determine the precise timing of the nocturnal temperature nadir ($T_{\min}$, the critical inflection boundary for Phase Response Curve light sensitivity), quantify circadian thermal amplitude, and prescribe evening distal arteriovenous anastomoses (AVAs) heat-dumping protocols.

## Agent In-Context Capabilities

- **Temperature Nadir ($T_{\min}$) Identification**: Projects the nocturnal temperature low point occurring $\sim 1.75$ hours before spontaneous waking.
- **Phase Response Curve (PRC) Inflection Boundary**: Enforces the photobiological law separating phase delay (light before $T_{\min}$) from phase advance (light after $T_{\min}$).
- **Distal Heat Dumping**: Prescribes warm water immersion ($40.0^\circ\text{C} - 42.5^\circ\text{C}$) exactly 90 minutes before planned bedtime to stimulate peripheral heat dissipation and expedite sleep latency.

## Tools Summary

1. `model_circadian_temperature_curve`: Calculates $T_{\min}$, $T_{\max}$, circadian amplitude, and PRC inflection boundaries.
2. `prescribe_distal_heat_dump_protocol`: Schedules warm immersion and bedroom cooling parameters for accelerated slow-wave sleep onset.
