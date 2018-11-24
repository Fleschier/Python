
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIVIDE LPAREN MINUS NUMBER PLUS RPAREN TIMESexpression : expression PLUS termexpression : expression MINUS termexpression : termterm : term TIMES factorterm : term DIVIDE factorterm : factorfactor : NUMBERfactor : LPAREN expression RPAREN'
    
_lr_action_items = {'RPAREN':([1,2,4,8,11,12,13,14,15,],[-3,-7,-6,13,-5,-4,-8,-1,-2,]),'DIVIDE':([1,2,4,11,12,13,14,15,],[6,-7,-6,-5,-4,-8,6,6,]),'NUMBER':([0,3,6,7,9,10,],[2,2,2,2,2,2,]),'TIMES':([1,2,4,11,12,13,14,15,],[7,-7,-6,-5,-4,-8,7,7,]),'PLUS':([1,2,4,5,8,11,12,13,14,15,],[-3,-7,-6,9,9,-5,-4,-8,-1,-2,]),'LPAREN':([0,3,6,7,9,10,],[3,3,3,3,3,3,]),'MINUS':([1,2,4,5,8,11,12,13,14,15,],[-3,-7,-6,10,10,-5,-4,-8,-1,-2,]),'$end':([1,2,4,5,11,12,13,14,15,],[-3,-7,-6,0,-5,-4,-8,-1,-2,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'term':([0,3,9,10,],[1,1,14,15,]),'expression':([0,3,],[5,8,]),'factor':([0,3,6,7,9,10,],[4,4,11,12,4,4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','yacc_example.py',7),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','yacc_example.py',11),
  ('expression -> term','expression',1,'p_expression_term','yacc_example.py',15),
  ('term -> term TIMES factor','term',3,'p_term_times','yacc_example.py',19),
  ('term -> term DIVIDE factor','term',3,'p_term_div','yacc_example.py',23),
  ('term -> factor','term',1,'p_term_factor','yacc_example.py',27),
  ('factor -> NUMBER','factor',1,'p_factor_num','yacc_example.py',31),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','yacc_example.py',35),
]
