
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "BREAK ELIF ELSE FOR IF LEN NUMBER PRINT VARIABLE WHILEprogram : statementsstatements : statements statement\n                  | statement statement : assignment\n                  | operation\n                  | print\n                  | if\n                  | elif\n                  | while\n                  | for\n                  | else\n                  assignment : VARIABLE '=' NUMBER\n                    | VARIABLE '=' list\n                    | VARIABLE '=' len\n                    | VARIABLE '=' VARIABLE\n                    | VARIABLE '=' '(' expr ')' '/' '/' NUMBER\n    list : '[' nums ']'  nums : nums ',' NUMBER\n            | NUMBER\n     len : LEN '(' VARIABLE ')' operation : VARIABLE '=' expr\n    expr : expr '+' term\n            | expr '-' term\n            | term\n    term : term '*' factor\n            | term '/' factor\n            | factor\n    factor : VARIABLE\n            | NUMBER\n    print : PRINT '(' values ')'\n    values : VARIABLE\n                | values ',' VARIABLE\n     conditions : conditions ';' condition\n                    | condition\n     condition : VARIABLE '>' VARIABLE\n                 | VARIABLE '<' VARIABLE\n                 | VARIABLE '<' '=' VARIABLE\n                 | VARIABLE '>' '=' VARIABLE\n                 | assignment\n                 | VARIABLE '+' '+'\n                if : IF '(' condition ')' '{' statements '}'\n    elif : ELIF '(' condition ')' '{' statements '}' else : ELSE '{' BREAK '}'    while : WHILE '(' condition ')' '{' statements '}'  for : FOR '(' conditions ')' '{' statements '}'\n    "
    
_lr_action_items = {'VARIABLE':([0,2,3,4,5,6,7,8,9,10,11,19,20,21,22,23,24,25,27,28,29,30,31,32,35,36,47,49,50,51,54,55,56,57,58,60,61,62,67,68,70,71,72,75,76,78,80,82,86,87,88,92,93,96,97,98,100,101,102,103,104,],[12,12,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,27,38,40,40,40,40,-15,-12,-13,-14,47,-21,-24,-27,-28,-29,47,47,74,47,47,-30,77,79,81,83,40,-43,-22,-23,-17,-25,-26,12,94,95,12,12,12,-20,12,12,12,12,-41,-42,-44,-45,-16,]),'PRINT':([0,2,3,4,5,6,7,8,9,10,11,19,27,28,29,30,32,35,36,47,49,57,68,70,71,72,75,76,78,86,87,88,92,93,96,97,98,100,101,102,103,104,],[13,13,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,-15,-12,-13,-14,-21,-24,-27,-28,-29,-30,-43,-22,-23,-17,-25,-26,13,13,13,13,-20,13,13,13,13,-41,-42,-44,-45,-16,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,19,27,28,29,30,32,35,36,47,49,57,68,70,71,72,75,76,78,86,87,88,92,93,96,97,98,100,101,102,103,104,],[14,14,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,-15,-12,-13,-14,-21,-24,-27,-28,-29,-30,-43,-22,-23,-17,-25,-26,14,14,14,14,-20,14,14,14,14,-41,-42,-44,-45,-16,]),'ELIF':([0,2,3,4,5,6,7,8,9,10,11,19,27,28,29,30,32,35,36,47,49,57,68,70,71,72,75,76,78,86,87,88,92,93,96,97,98,100,101,102,103,104,],[15,15,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,-15,-12,-13,-14,-21,-24,-27,-28,-29,-30,-43,-22,-23,-17,-25,-26,15,15,15,15,-20,15,15,15,15,-41,-42,-44,-45,-16,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,11,19,27,28,29,30,32,35,36,47,49,57,68,70,71,72,75,76,78,86,87,88,92,93,96,97,98,100,101,102,103,104,],[16,16,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,-15,-12,-13,-14,-21,-24,-27,-28,-29,-30,-43,-22,-23,-17,-25,-26,16,16,16,16,-20,16,16,16,16,-41,-42,-44,-45,-16,]),'FOR':([0,2,3,4,5,6,7,8,9,10,11,19,27,28,29,30,32,35,36,47,49,57,68,70,71,72,75,76,78,86,87,88,92,93,96,97,98,100,101,102,103,104,],[17,17,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,-15,-12,-13,-14,-21,-24,-27,-28,-29,-30,-43,-22,-23,-17,-25,-26,17,17,17,17,-20,17,17,17,17,-41,-42,-44,-45,-16,]),'ELSE':([0,2,3,4,5,6,7,8,9,10,11,19,27,28,29,30,32,35,36,47,49,57,68,70,71,72,75,76,78,86,87,88,92,93,96,97,98,100,101,102,103,104,],[18,18,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,-15,-12,-13,-14,-21,-24,-27,-28,-29,-30,-43,-22,-23,-17,-25,-26,18,18,18,18,-20,18,18,18,18,-41,-42,-44,-45,-16,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,19,27,28,29,30,32,35,36,47,49,57,68,70,71,72,75,76,92,100,101,102,103,104,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,-15,-12,-13,-14,-21,-24,-27,-28,-29,-30,-43,-22,-23,-17,-25,-26,-20,-41,-42,-44,-45,-16,]),'}':([3,4,5,6,7,8,9,10,11,19,27,28,29,30,32,35,36,46,47,49,57,68,70,71,72,75,76,92,93,96,97,98,100,101,102,103,104,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-2,-15,-12,-13,-14,-21,-24,-27,68,-28,-29,-30,-43,-22,-23,-17,-25,-26,-20,100,101,102,103,-41,-42,-44,-45,-16,]),'=':([12,40,60,61,],[20,62,80,82,]),'(':([13,14,15,16,17,20,34,62,],[21,22,23,24,25,31,54,31,]),'{':([18,59,64,65,66,],[26,78,86,87,88,]),'NUMBER':([20,31,33,50,51,55,56,62,73,99,],[28,49,53,49,49,49,49,84,91,104,]),'[':([20,62,],[33,33,]),'LEN':([20,62,],[34,34,]),'BREAK':([26,],[46,]),'*':([27,28,35,36,47,49,70,71,75,76,],[-28,-29,55,-27,-28,-29,55,55,-25,-26,]),'/':([27,28,35,36,47,49,69,70,71,75,76,90,],[-28,-29,56,-27,-28,-29,90,56,56,-25,-26,99,]),'+':([27,28,32,35,36,40,47,48,49,63,70,71,75,76,],[-28,-29,50,-24,-27,63,-28,50,-29,85,-22,-23,-25,-26,]),'-':([27,28,32,35,36,47,48,49,70,71,75,76,],[-28,-29,51,-24,-27,-28,51,-29,-22,-23,-25,-26,]),')':([29,30,35,36,37,38,39,41,42,43,44,45,47,48,49,70,71,72,74,75,76,77,79,81,83,84,85,89,92,94,95,104,],[-13,-14,-24,-27,57,-31,59,-39,64,65,66,-34,-28,69,-29,-22,-23,-17,92,-25,-26,-32,-35,-36,-15,-12,-40,-33,-20,-38,-37,-16,]),';':([29,30,41,44,45,72,79,81,83,84,85,89,92,94,95,104,],[-13,-14,-39,67,-34,-17,-35,-36,-15,-12,-40,-33,-20,-38,-37,-16,]),',':([37,38,52,53,77,91,],[58,-31,73,-19,-32,-18,]),'>':([40,],[60,]),'<':([40,],[61,]),']':([52,53,91,],[72,-19,-18,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements':([0,78,86,87,88,],[2,93,96,97,98,]),'statement':([0,2,78,86,87,88,93,96,97,98,],[3,19,3,3,3,3,19,19,19,19,]),'assignment':([0,2,22,23,24,25,67,78,86,87,88,93,96,97,98,],[4,4,41,41,41,41,41,4,4,4,4,4,4,4,4,]),'operation':([0,2,78,86,87,88,93,96,97,98,],[5,5,5,5,5,5,5,5,5,5,]),'print':([0,2,78,86,87,88,93,96,97,98,],[6,6,6,6,6,6,6,6,6,6,]),'if':([0,2,78,86,87,88,93,96,97,98,],[7,7,7,7,7,7,7,7,7,7,]),'elif':([0,2,78,86,87,88,93,96,97,98,],[8,8,8,8,8,8,8,8,8,8,]),'while':([0,2,78,86,87,88,93,96,97,98,],[9,9,9,9,9,9,9,9,9,9,]),'for':([0,2,78,86,87,88,93,96,97,98,],[10,10,10,10,10,10,10,10,10,10,]),'else':([0,2,78,86,87,88,93,96,97,98,],[11,11,11,11,11,11,11,11,11,11,]),'list':([20,62,],[29,29,]),'len':([20,62,],[30,30,]),'expr':([20,31,],[32,48,]),'term':([20,31,50,51,],[35,35,70,71,]),'factor':([20,31,50,51,55,56,],[36,36,36,36,75,76,]),'values':([21,],[37,]),'condition':([22,23,24,25,67,],[39,42,43,45,89,]),'conditions':([25,],[44,]),'nums':([33,],[52,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','py_yacc.py',16),
  ('statements -> statements statement','statements',2,'p_statements','py_yacc.py',22),
  ('statements -> statement','statements',1,'p_statements','py_yacc.py',23),
  ('statement -> assignment','statement',1,'p_statement','py_yacc.py',33),
  ('statement -> operation','statement',1,'p_statement','py_yacc.py',34),
  ('statement -> print','statement',1,'p_statement','py_yacc.py',35),
  ('statement -> if','statement',1,'p_statement','py_yacc.py',36),
  ('statement -> elif','statement',1,'p_statement','py_yacc.py',37),
  ('statement -> while','statement',1,'p_statement','py_yacc.py',38),
  ('statement -> for','statement',1,'p_statement','py_yacc.py',39),
  ('statement -> else','statement',1,'p_statement','py_yacc.py',40),
  ('assignment -> VARIABLE = NUMBER','assignment',3,'p_assignment','py_yacc.py',59),
  ('assignment -> VARIABLE = list','assignment',3,'p_assignment','py_yacc.py',60),
  ('assignment -> VARIABLE = len','assignment',3,'p_assignment','py_yacc.py',61),
  ('assignment -> VARIABLE = VARIABLE','assignment',3,'p_assignment','py_yacc.py',62),
  ('assignment -> VARIABLE = ( expr ) / / NUMBER','assignment',8,'p_assignment','py_yacc.py',63),
  ('list -> [ nums ]','list',3,'p_list','py_yacc.py',85),
  ('nums -> nums , NUMBER','nums',3,'p_nums','py_yacc.py',92),
  ('nums -> NUMBER','nums',1,'p_nums','py_yacc.py',93),
  ('len -> LEN ( VARIABLE )','len',4,'p_LEN','py_yacc.py',105),
  ('operation -> VARIABLE = expr','operation',3,'p_operation','py_yacc.py',110),
  ('expr -> expr + term','expr',3,'p_expr','py_yacc.py',124),
  ('expr -> expr - term','expr',3,'p_expr','py_yacc.py',125),
  ('expr -> term','expr',1,'p_expr','py_yacc.py',126),
  ('term -> term * factor','term',3,'p_term','py_yacc.py',137),
  ('term -> term / factor','term',3,'p_term','py_yacc.py',138),
  ('term -> factor','term',1,'p_term','py_yacc.py',139),
  ('factor -> VARIABLE','factor',1,'p_factor','py_yacc.py',150),
  ('factor -> NUMBER','factor',1,'p_factor','py_yacc.py',151),
  ('print -> PRINT ( values )','print',4,'p_print','py_yacc.py',163),
  ('values -> VARIABLE','values',1,'p_values','py_yacc.py',172),
  ('values -> values , VARIABLE','values',3,'p_values','py_yacc.py',173),
  ('conditions -> conditions ; condition','conditions',3,'p_conditions','py_yacc.py',185),
  ('conditions -> condition','conditions',1,'p_conditions','py_yacc.py',186),
  ('condition -> VARIABLE > VARIABLE','condition',3,'p_condition','py_yacc.py',198),
  ('condition -> VARIABLE < VARIABLE','condition',3,'p_condition','py_yacc.py',199),
  ('condition -> VARIABLE < = VARIABLE','condition',4,'p_condition','py_yacc.py',200),
  ('condition -> VARIABLE > = VARIABLE','condition',4,'p_condition','py_yacc.py',201),
  ('condition -> assignment','condition',1,'p_condition','py_yacc.py',202),
  ('condition -> VARIABLE + +','condition',3,'p_condition','py_yacc.py',203),
  ('if -> IF ( condition ) { statements }','if',7,'p_if','py_yacc.py',214),
  ('elif -> ELIF ( condition ) { statements }','elif',7,'p_elif','py_yacc.py',222),
  ('else -> ELSE { BREAK }','else',4,'p_else','py_yacc.py',229),
  ('while -> WHILE ( condition ) { statements }','while',7,'p_while','py_yacc.py',233),
  ('for -> FOR ( conditions ) { statements }','for',7,'p_for','py_yacc.py',241),
]
