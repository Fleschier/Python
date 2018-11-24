
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ELEMENT NUMBERspecies_list : species_list speciesspecies_list : speciesspecies : ELEMENTspecies : ELEMENT NUMBER'
    
_lr_action_items = {'ELEMENT':([0,1,2,3,4,5,],[3,3,-2,-3,-1,-4,]),'$end':([1,2,3,4,5,],[0,-2,-3,-1,-4,]),'NUMBER':([3,],[5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'species_list':([0,],[1,]),'species':([0,1,],[2,4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> species_list","S'",1,None,None,None),
  ('species_list -> species_list species','species_list',2,'p_parse1','ch7.py',65),
  ('species_list -> species','species_list',1,'p_parse2','ch7.py',69),
  ('species -> ELEMENT','species',1,'p_parse3','ch7.py',73),
  ('species -> ELEMENT NUMBER','species',2,'p_parse4','ch7.py',77),
]
