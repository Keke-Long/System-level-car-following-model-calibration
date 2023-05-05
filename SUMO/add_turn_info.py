import pandas as pd
import numpy as np

veh_info = pd.read_csv("../Data/Veh_info3.csv")
veh_info['turn_I1'] = np.nan
veh_info['turn_I2'] = np.nan
veh_info['turn_I3'] = np.nan

route_list = {"S0E4":['s','s','s'],"S0E6":['s','l','n'],"S0E7":['s','s','l'],"S0E8":['r','n','n'],"S0E10":['s','s','r'],
              "S4E0":['s','s','s'],"S4E6":['n','r','s'],"S4E7":['n','n','r'],"S4E8":['l','s','s'],"S4E10":['n','n','l'],
              "S5E0":['r','n','n'],"S5E4":['l','s','s'],"S5E6":['l','l','n'],"S5E7":['l','s','l'],"S5E8":['s','n','n'],"S5E10":['l','s','r'],
              "S7E0":['s','s','r'],"S7E4":['n','n','l'],"S7E6":['n','r','r'],"S7E8":['l','s','r'],"S7E10":['n','n','s'],
              "S9E0":['s','l','n'],"S9E4":['n','r','l'],"S9E6":['n','s','n'],"S9E7":['n','r','l'],"S9E8":['l','l','n'],"S9E10":['n','r','r'],
              "S10E0":['s','s','l'],"S10E4":['n','n','r'],"S10E6":['n','r','l'],"S10E7":['n','n','s'],"S10E8":['l','s','l']}

for index, row in veh_info.iterrows():
    #id = str(row['id'])
    if row['edge_start'][0] != 'n' and row['edge_end'][0] != 'n':
        start_edge = row['edge_start'].split('_')[0]
        end_edge = row['edge_end'].split('_')[1]
        route = 'S' + start_edge + 'E' + end_edge
        # 添加车辆转向信息
        if route in route_list.keys():
            veh_info.loc[index, 'turn_I1'] = route_list[route][0]
            veh_info.loc[index, 'turn_I2'] = route_list[route][1]
            veh_info.loc[index, 'turn_I3'] = route_list[route][2]

print(veh_info)
veh_info.to_csv('../Data/veh_info3.csv', index=False)