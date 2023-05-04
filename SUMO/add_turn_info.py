import pandas as pd
import numpy as np

veh_info = pd.read_csv("../Data/Veh_info3.csv")
veh_info['turn_I1', 'turn_I2', 'turn_I3'] = np.nan


"S0E4","S0E6","S0E7","S0E8","S0E10","S4E0","S4E6","S4E7","S4E8","S4E10",

for index, row in veh_info.iterrows():
    #id = str(row['id'])
    if row['edge_start'][0] != 'n' and row['edge_end'][0] != 'n':
        start_edge = row['edge_start'].split('_')[0]
        end_edge = row['edge_end'].split('_')[1]
        route = 'S' + start_edge + 'E' + end_edge
        if route in route_list:
            traci.route.add(, ["I0I1", "I1M0", "M0I2", "I2M1", "M1I3", "I3I4"])
            traci.route.add( ["I0I1", "I1M0", "M0I2", "I2I6"])
            traci.route.add( ["I0I1", "I1M0", "M0I2", "I2M1", "M1I3", "I3I7"])
            traci.route.add( ["I0I1", "I1I8"])
            traci.route.add( ["I0I1", "I1M0", "M0I2", "I2M1", "M1I3", "I3I10"])

            traci.route.add( ["I4I3", "I3I2", "I2I1", "I1I0"])
            traci.route.add( ["I4I3", "I3I2", "I2I6"])
            traci.route.add( ["I4I3", "I3I7"])
            traci.route.add( ["I4I3", "I3I2", "I2I1", "I1I8"])
            traci.route.add( ["I4I3", "I3I10"])

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