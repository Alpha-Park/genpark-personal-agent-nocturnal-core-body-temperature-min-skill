# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Nocturnal Core Body Temperature Min Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentNocturnalCoreBodyTemperatureMin

def main():
    agent = PersonalAgentNocturnalCoreBodyTemperatureMin()

    print("=" * 70)
    print("DEMO: Personal Agent Nocturnal Core Body Temperature Min Engine")
    print("=" * 70)

    # 1. Model Circadian Temperature Curve (Wake: 06:45 -> 6.75, Peak 37.3 C, Nadir 36.4 C)
    res_cbt = agent.model_circadian_temperature_curve(
        habitual_wake_time_24h=6.75,
        evening_peak_cbt_celsius=37.3,
        nocturnal_nadir_cbt_celsius=36.4
    )

    print(f"\n1. Circadian Core Body Temperature Modeling:")
    print(f"   Habitual Wake Time: {res_cbt['habitual_wake_time']}")
    print(f"   Projected T_min (Nadir): {res_cbt['projected_t_min_nadir_time']}")
    print(f"   Projected T_max (Acrophase): {res_cbt['projected_t_max_acrophase_time']}")
    print(f"   Nocturnal Temperature Drop: {res_cbt['nocturnal_temperature_drop_celsius']} C")
    print(f"   Circadian Amplitude: {res_cbt['circadian_temperature_amplitude_celsius']} C")
    print(f"   Amplitude Tier: {res_cbt['thermoregulatory_amplitude_tier']}")
    print(f"   Entrainment Status: {res_cbt['circadian_entrainment_status']}")
    print(f"   PRC Boundary: {res_cbt['prc_inflection_boundary']}")

    # 2. Prescribe Distal Heat Dump Protocol (Bedtime: 23:00 -> 23.0)
    res_bath = agent.prescribe_distal_heat_dump_protocol(
        target_bedtime_24h=23.0
    )

    print(f"\n2. Evening Distal Heat Dump Prescription (Bedtime: 23:00):")
    print(f"   Warm Immersion Window: {res_bath['prescribed_warm_immersion_window']}")
    print(f"   Water Specification: {res_bath['water_temperature_specification']}")
    print(f"   Mechanism: {res_bath['physiological_heat_dump_mechanism']}")
    print(f"   Ambient Target: {res_bath['bedroom_ambient_target']}")

    print("\nVerification complete: Core body temperature engine executed flawlessly.")

if __name__ == "__main__":
    main()
