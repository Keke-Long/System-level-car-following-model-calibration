# -*- coding: utf-8 -*-
"""
@author: Keke
"""

import traci

def traci_route_add():
    traci.route.add("S0E4", ["I0I1", "I1M0", "M0I2", "I2M1", "M1I3", "I3I4"])
    traci.route.add("S0E6", ["I0I1", "I1M0", "M0I2", "I2I6"])
    traci.route.add("S0E7", ["I0I1", "I1M0", "M0I2", "I2M1", "M1I3", "I3I7"])
    traci.route.add("S0E8", ["I0I1", "I1I8"])
    traci.route.add("S0E10", ["I0I1", "I1M0", "M0I2", "I2M1", "M1I3", "I3I10"])

    traci.route.add("S4E0", ["I4I3", "I3I2", "I2I1", "I1I0"])
    traci.route.add("S4E6", ["I4I3", "I3I2", "I2I6"])
    traci.route.add("S4E7", ["I4I3", "I3I7"])
    traci.route.add("S4E8", ["I4I3", "I3I2", "I2I1", "I1I8"])
    traci.route.add("S4E10", ["I4I3", "I3I10"])

    traci.route.add("S5E0", ["I5I1", "I1I0"])
    traci.route.add("S5E4", ["I5I1", "I1M0", "M0I2", "I2M1", "M1I3", "I3I4"])
    traci.route.add("S5E6", ["I5I1", "I1M0", "M0I2", "I2I6"])
    traci.route.add("S5E7", ["I5I1", "I1M0", "M0I2", "I2M1", "M1I3", "I3I7"])
    traci.route.add("S5E8", ["I5I1", "I1I8"])
    traci.route.add("S5E10", ["I5I1", "I1M0", "M0I2", "I2M1", "M1I3", "I3I10"])

    traci.route.add("S7E0", ["I7I3", "I3I2", "I2I1", "I1I0"])
    traci.route.add("S7E4", ["I7I3", "I3I4"])
    traci.route.add("S7E6", ["I7I3", "I3I2", "I2I6"])
    traci.route.add("S7E8", ["I7I3", "I3I2", "I2I1", "I1I8"])
    traci.route.add("S7E10", ["I7I3", "I3I10"])

    traci.route.add("S9E0", ["I9I2", "I2I1", "I1I0"])
    traci.route.add("S9E4", ["I9I2", "I2M1", "M1I3", "I3I4"])
    traci.route.add("S9E6", ["I9I2", "I2I6"])
    traci.route.add("S9E7", ["I9I2", "I2M1", "M1I3", "I3I7"])
    traci.route.add("S9E8", ["I9I2", "I2I1", "I1I8"])
    traci.route.add("S9E10", ["I9I2", "I2M1", "M1I3", "I3I10"])

    traci.route.add("S10E0", ["I10I3", "I3I2", "I2I1", "I1I0"])
    traci.route.add("S10E4", ["I10I3", "I3I4"])
    traci.route.add("S10E6", ["I10I3", "I3I2", "I2I6"])
    traci.route.add("S10E7", ["I10I3", "I3I7"])
    traci.route.add("S10E8", ["I10I3", "I3I2", "I2I1", "I1I8"])

