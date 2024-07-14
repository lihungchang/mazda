from selfdrive.car import dbc_dict
from cereal import car
Ecu = car.CarParams.Ecu


# Steer torque limits

class CarControllerParams:
  STEER_MAX = 800                 # theoretical max_steer 2047
  STEER_DELTA_UP = 10             # torque increase per refresh
  STEER_DELTA_DOWN = 25           # torque decrease per refresh
  STEER_DRIVER_ALLOWANCE = 15     # allowed driver torque before start limiting
  STEER_DRIVER_MULTIPLIER = 1     # weight driver torque
  STEER_DRIVER_FACTOR = 1         # from dbc
  STEER_ERROR_MAX = 350           # max delta between torque cmd and torque motor

class CAR:
  CX5 = "MAZDA CX-5"
  CX9 = "MAZDA CX-9"
  MAZDA3 = "MAZDA 3"
  MAZDA6 = "MAZDA 6"
  CX9_2021 = "MAZDA CX-9 2021"
  CX5_2022 = "MAZDA CX-5 2022"

class LKAS_LIMITS:
  STEER_THRESHOLD = 15
  DISABLE_SPEED = 45    # kph
  ENABLE_SPEED = 52     # kph

class Buttons:
  NONE = 0
  SET_PLUS = 1
  SET_MINUS = 2
  RESUME = 3
  CANCEL = 4


FW_VERSIONS = {
  CAR.CX5_2022 : {
    (Ecu.eps, 0x730, None): [
      b'KSD5-3210X-C-00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'PX2G-188K2-H\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PGK3-188K2-A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdRadar, 0x764, None): [
      b'K131-67XK2-F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.esp, 0x760, None): [
      b'KSD5-437K2-A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdCamera, 0x706, None): [
      b'GSH7-67XK2-S\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'GSH7-67XK2-T\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',	  
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'PYB2-21PS1-H\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PG69-21PS1-A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
  },
  CAR.CX5: {
    (Ecu.eps, 0x730, None): [
      b'K070-3210X-C-00\x00\x00\x00\x00\x00\x00\x00\x00\x00',    
      b'K319-3210X-A-00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'KCB8-3210X-B-00\x00\x00\x00\x00\x00\x00\x00\x00\x00',   
      b'KJ01-3210X-F-00\x00\x00\x00\x00\x00\x00\x00\x00\x00',       
      b'KJ01-3210X-G-00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'KJ01-3210X-J-00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'KJ01-3210X-M-00\x00\x00\x00\x00\x00\x00\x00\x00\x00',  
      b'KSD5-3210X-C-00\x00\x00\x00\x00\x00\x00\x00\x00\x00', #from CX5_2022
    ],
    (Ecu.engine, 0x7e0, None): [
      b'PA53-188K2-A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PA68-188K2-A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 
      b'PAR4-188K2-D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PAR4-188K2-E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',   
      b'PAR5-188K2-D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 
      b'PGK4-188K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PSH7-188K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',        
      b'PSJ5-188K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',      
      b'PSME-188K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',    
      b'PSMF-188K2-A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',       
      b'PSMF-188K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',      
      b'PX2F-188K2-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PX2G-188K2-D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PX2H-188K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PX2H-188K2-D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PX2H-188K2-G\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PX2K-188K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PX38-188K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PX42-188K2-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PX68-188K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYFA-188K2-J\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',   
      b'PYFC-188K2-J\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYFD-188K2-J\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYNF-188K2-F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',      
      b'SH7P-188K2-F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'SHEA-188K2-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',    
      b'SHKT-188K2-D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',  
      b'SHKT-188K2-F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdRadar, 0x764, None): [
      b'K123-67XK2-F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'K131-67XK2-A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'K131-67XK2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'K131-67XK2-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'K131-67XK2-E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'K131-67XK2-F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'G46L-67XA1-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.esp, 0x760, None): [
      b'K123-437K2-E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'KA0G-437AS-0-03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',      
      b'KBJ5-437K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'KL2H-437K2-A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'KL2K-437K2-A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'KN0W-437K2-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdCamera, 0x706, None): [
      b'B61L-67XK2-K\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'B61L-67XK2-M\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',      
      b'B61L-67XK2-R\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'B61L-67XK2-S\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'B61L-67XK2-T\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'B61L-67XK2-V\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'GMG6-67XK2-F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',  
      b'GMG6-67XK2-G\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 		  
      b'GSH7-67XK2-J\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'GSH7-67XK2-M\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'GSH7-67XK2-N\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'GSH7-67XK2-R\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'PA66-21PS1-A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PA66-21PS1-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',  
      b'PA66-21PS1-D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',        
      b'PS53-21PS1-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PSKX-21PS1-A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',      
      b'PX39-21PS1-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PX39-21PS1-D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PX68-21PS1-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYB1-21PS1-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYB1-21PS1-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYB1-21PS1-G\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYB2-21PS1-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYB2-21PS1-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYB2-21PS1-D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYB2-21PS1-G\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYB2-21PS1-H\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYNC-21PS1-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'SH6S-21PS1-D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',     
      b'SH9T-21PS1-D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'SH9T-21PS1-F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'SHEG-21PS1-A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
  },

  CAR.CX9 : {
    (Ecu.eps, 0x730, None): [
      b'K070-3210X-C-00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'KJ01-3210X-G-00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'KJ01-3210X-L-00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'PX23-188K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PX24-188K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PXB8-188K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',      
      b'PXN8-188K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PXN8-188K2-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYD7-188K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYD8-188K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYFM-188K2-F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYFM-188K2-H\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdRadar, 0x764, None): [
      b'K123-67XK2-F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'K131-67XK2-A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'K131-67XK2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'K131-67XK2-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'TK80-67XK2-E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'TK80-67XK2-F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.esp, 0x760, None): [
      b'TA0B-437K2-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'TK79-437K2-E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'TK79-437K2-F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'TM53-437K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'TN40-437K2-A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdCamera, 0x706, None): [
      b'B61L-67XK2-P\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'B61L-67XK2-T\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',      
      b'B61L-67XK2-V\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'GSH7-67XK2-K\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'TK80-67XK2-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
   ],
    (Ecu.transmission, 0x7e1, None): [
      b'PXM7-21PS1-A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PXM7-21PS1-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYD5-21PS1-A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYD5-21PS1-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYD6-21PS1-A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYD6-21PS1-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',	  
      b'PYE8-21PS1-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYFM-21PS1-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYFM-21PS1-D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
  },

  CAR.MAZDA3: {
    (Ecu.eps, 0x730, None): [
      b'BHN1-3210X-F-00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'BHN1-3210X-J-00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'K070-3210X-C-00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'KR11-3210X-K-00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'P5JD-188K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PS1E-188K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',	  
      b'PS7V-188K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PS8B-188K2-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PY2P-188K2-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYJW-188K2-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYKC-188K2-D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYKE-188K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdRadar, 0x764, None): [
      b'B63C-67XK2-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'GHP9-67Y10---41\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'K131-67XK2-A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'K131-67XK2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'K131-67XK2-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'K131-67XK2-E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'K131-67XK2-F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'G46L-67XA1-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.esp, 0x760, None): [
      b'B45A-437AS-0-05\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'B45A-437AS-0-08\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdCamera, 0x706, None): [
      b'B61L-67XK2-D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'B61L-67XK2-G\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',      
      b'B61L-67XK2-P\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'B61L-67XK2-Q\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'B61L-67XK2-S\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',      
      b'B61L-67XK2-T\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'GMG6-67XK2-F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',   
      b'GMG6-67XK2-G\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 
      b'BHS2-67XCX\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'P52G-21PS1-F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PEFR-21PS1-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PS6M-21PS1-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PS6M-21PS1-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 
      b'PY2S-21PS1-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYKA-21PS1-A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYKE-21PS1-A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYKE-21PS1-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',    
    ],
  },

  CAR.MAZDA6: {
    (Ecu.eps, 0x730, None): [
      b'GBEF-3210X-B-00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'GFBC-3210X-A-00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'GHT2-3210X-G-00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 
      b'G46D-3210X-B-00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'PX4F-188K2-D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYH7-188K2-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'SH2H-188K2-P\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'SHYT-188K2-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 
      b'PXAL-188K2-A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',	 
      b'PXAL-188K2-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdRadar, 0x764, None): [
      b'G46L-67XA1-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'GHP9-67Y10---44\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',      
      b'K131-67XK2-A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'K131-67XK2-E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'K131-67XK2-F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',	  
    ],
    (Ecu.esp, 0x760, None): [
      b'GBVH-437K2-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'GDDM-437K2-A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'GHR1-437AS-3-60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'GMM1-437AS-0-70\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdCamera, 0x706, None): [
      b'B61L-67XK2-S\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'GHP9-67XCX\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'GMG6-67XK2-F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',  
      b'GMG6-67XK2-G\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',	  
      b'GSH7-67XK2-P\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'GSH7-67XK2-S\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',	
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'PYH3-21PS1-D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYH7-21PS1-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'SH08-21PS1-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'SHBX-21PS1-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'SHBX-21PS1-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PYM1-21PS1-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
  },

  CAR.CX9_2021 : {
    (Ecu.eps, 0x730, None): [
      b'TC3M-3210X-A-00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'PXM4-188K2-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'PXM4-188K2-D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdRadar, 0x764, None): [
      b'K131-67XK2-E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'K131-67XK2-F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.esp, 0x760, None): [
      b'TA0B-437K2-C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdCamera, 0x706, None): [
      b'GSH7-67XK2-M\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'GSH7-67XK2-N\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
      b'GSH7-67XK2-P\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'PXM4-21PS1-B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
  }
}


DBC = {
  CAR.CX5: dbc_dict('mazda_2017', None),
  CAR.CX9: dbc_dict('mazda_2017', None),
  CAR.MAZDA3: dbc_dict('mazda_2017', None),
  CAR.MAZDA6: dbc_dict('mazda_2017', None),
  CAR.CX9_2021: dbc_dict('mazda_2017', None),
  CAR.CX5_2022: dbc_dict('mazda_2017', None),
}

# Gen 1 hardware: same CAN messages and same camera
GEN1 = {CAR.CX5, CAR.CX9, CAR.CX9_2021, CAR.MAZDA3, CAR.MAZDA6, CAR.CX5_2022}
