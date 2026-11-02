# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Nocturnal Core Body Temperature Min Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentNocturnalCoreBodyTemperatureMin

mcp = FastMCP("PersonalAgentNocturnalCoreBodyTemperatureMin")
client = PersonalAgentNocturnalCoreBodyTemperatureMin()

@mcp.tool()
def model_circadian_temperature_curve(
    habitual_wake_time_24h: float = 7.0,
    evening_peak_cbt_celsius: float = 37.2,
    nocturnal_nadir_cbt_celsius: float = 36.3
) -> str:
    """Calculates circadian temperature nadir (T_min) timing, rhythm amplitude, and PRC inflection boundaries."""
    import json
    return json.dumps(client.model_circadian_temperature_curve(
        habitual_wake_time_24h, evening_peak_cbt_celsius, nocturnal_nadir_cbt_celsius
    ), indent=2)

@mcp.tool()
def prescribe_distal_heat_dump_protocol(
    target_bedtime_24h: float = 23.0
) -> str:
    """Prescribes evening warm immersion window and ambient cooling to accelerate CBT decline."""
    import json
    return json.dumps(client.prescribe_distal_heat_dump_protocol(
        target_bedtime_24h
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
