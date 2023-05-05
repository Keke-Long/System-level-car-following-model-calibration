# -*- coding: utf-8 -*-
"""
@author: Keke
"""

import traci

def traci_vtype_add():
    vf, A, b, s0, T = (17.01441366, 2.11620502, 1.69595889, 1.77614233, 1.46909532)
    traci.vehicletype.setShapeClass("HV_IDM_s", "passenger")
    traci.vehicletype.setLength("HV_IDM_s", 4.6)
    traci.vehicletype.setMaxSpeed("HV_IDM_s", vf)
    traci.vehicletype.setAccel("HV_IDM_s", A)
    traci.vehicletype.setDecel("HV_IDM_s", b)
    traci.vehicletype.setMinGap("HV_IDM_s", s0)
    traci.vehicletype.setTau("HV_IDM_s", T)

    traci.vehicletype.setShapeClass("HV_IDM_l", "bus")
    traci.vehicletype.setLength("HV_IDM_l", 11)
    traci.vehicletype.setMaxSpeed("HV_IDM_l", vf)
    traci.vehicletype.setAccel("HV_IDM_l", A)
    traci.vehicletype.setDecel("HV_IDM_l", b)
    traci.vehicletype.setMinGap("HV_IDM_l", s0)
    traci.vehicletype.setTau("HV_IDM_l", T)