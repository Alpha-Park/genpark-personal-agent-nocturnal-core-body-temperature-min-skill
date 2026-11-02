# -*- coding: utf-8 -*-
"""Personal Agent Nocturnal Core Body Temperature Min Skill.

Zero-dependency circadian core body temperature (CBT) nadir modeler, distal-to-proximal
vasodilation heat dump calculator, and phase response curve inflection timing scheduler.
"""

import math
from typing import Dict, Any, Optional

class PersonalAgentNocturnalCoreBodyTemperatureMin:
    """Quantitative circadian thermoregulation and nocturnal temperature nadir (T_min) engine
    based on human circadian phase response curve and arteriovenous anastomoses vasodilation models."""

    def model_circadian_temperature_curve(
        self,
        habitual_wake_time_24h: float = 7.0,
        evening_peak_cbt_celsius: float = 37.2,
        nocturnal_nadir_cbt_celsius: float = 36.3
    ) -> Dict[str, Any]:
        """Calculates circadian temperature nadir (T_min) timing, rhythm amplitude,
        phase response curve advance/delay inflection point, and thermal entrainment status."""
        wake = habitual_wake_time_24h % 24.0
        t_peak = max(36.8, min(37.8, float(evening_peak_cbt_celsius)))
        t_nadir = max(35.5, min(t_peak - 0.2, float(nocturnal_nadir_cbt_celsius)))

        # Circadian Temperature Nadir (T_min) occurs ~1.75 hours prior to spontaneous awakening
        t_min_hour = (wake - 1.75) % 24.0

        # Circadian Peak (Acrophase) occurs ~12 hours from nadir (typically late afternoon ~16:00-18:00)
        t_max_hour = (t_min_hour + 12.0) % 24.0

        # Circadian Amplitude A = (T_peak - T_nadir) / 2
        amplitude = round((t_peak - t_nadir) / 2.0, 2)
        total_drop = round(t_peak - t_nadir, 2)

        # Robust circadian amplitude benchmark: 0.7 - 1.0 C drop
        if total_drop >= 0.75:
            amplitude_tier = "Robust Circadian Thermoregulatory Amplitude"
            entrainment_status = "Strong autonomic circadian drive; optimal nocturnal melatonin secretion"
        elif total_drop >= 0.50:
            amplitude_tier = "Moderate Circadian Amplitude"
            entrainment_status = "Acceptable nocturnal cooling; mild circadian phase dispersion"
        else:
            amplitude_tier = "Blunted Circadian Temperature Rhythm"
            entrainment_status = "Sub-clinical autonomic or metabolic friction; delayed sleep onset risk"

        def _fmt(h_float: float) -> str:
            h = int(h_float) % 24
            m = int(round((h_float - int(h_float)) * 60))
            if m >= 60:
                h = (h + 1) % 24
                m = 0
            return f"{h:02d}:{m:02d}"

        return {
            "habitual_wake_time": _fmt(wake),
            "projected_t_min_nadir_time": _fmt(t_min_hour),
            "projected_t_max_acrophase_time": _fmt(t_max_hour),
            "nocturnal_temperature_drop_celsius": total_drop,
            "circadian_temperature_amplitude_celsius": amplitude,
            "thermoregulatory_amplitude_tier": amplitude_tier,
            "circadian_entrainment_status": entrainment_status,
            "prc_inflection_boundary": (
                f"CRITICAL LIGHT RULE: Bright light BEFORE {_fmt(t_min_hour)} causes PHASE DELAYS (drifts sleep later); "
                f"bright light AFTER {_fmt(t_min_hour)} causes PHASE ADVANCES (anchors earlier waking)."
            )
        }

    def prescribe_distal_heat_dump_protocol(
        self,
        target_bedtime_24h: float = 23.0
    ) -> Dict[str, Any]:
        """Prescribes evening warm bath / sauna peripheral vasodilation heat-dump protocol
        to accelerate nocturnal core temperature decline."""
        bedtime = target_bedtime_24h % 24.0
        # Optimal warm bath timing: 90 minutes before planned sleep onset (Kräuchi et al.)
        bath_start = (bedtime - 1.5) % 24.0
        bath_end = (bath_start + 0.33) % 24.0  # 20 minutes

        def _fmt(h_float: float) -> str:
            h = int(h_float) % 24
            m = int(round((h_float - int(h_float)) * 60))
            if m >= 60:
                h = (h + 1) % 24
                m = 0
            return f"{h:02d}:{m:02d}"

        return {
            "target_bedtime": _fmt(bedtime),
            "prescribed_warm_immersion_window": f"{_fmt(bath_start)} - {_fmt(bath_end)} (90 mins pre-sleep)",
            "water_temperature_specification": "40.0 C - 42.5 C (Warm-to-hot)",
            "physiological_heat_dump_mechanism": (
                "Warm water triggers selective vasodilation of glabrous skin arteriovenous anastomoses (AVAs) in hands and feet, "
                "rapidly dumping core heat to the periphery and lowering CBT by ~0.3 C to hasten slow-wave sleep onset."
            ),
            "bedroom_ambient_target": "18.0 C - 19.5 C with light, breathable bedding."
        }
