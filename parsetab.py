
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'EQUALS LPAREN NAME NUMBER PLUS RPARENstatement : NAME EQUALS expressionexpression : termexpression : expression PLUS expressionexpression : LPAREN expression RPARENterm : NAMEterm : NUMBER'
    
_lr_action_items = {'RPAREN':([4,5,6,9,11,12,],[-2,-5,-6,11,-4,-3,]),'NAME':([0,3,7,10,],[1,5,5,5,]),'NUMBER':([3,7,10,],[6,6,6,]),'EQUALS':([1,],[3,]),'PLUS':([4,5,6,8,9,11,12,],[-2,-5,-6,10,10,-4,10,]),'LPAREN':([3,7,10,],[7,7,7,]),'$end':([2,4,5,6,8,11,12,],[0,-2,-5,-6,-1,-4,-3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'term':([3,7,10,],[4,4,4,]),'expression':([3,7,10,],[8,9,12,]),'statement':([0,],[2,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> NAME EQUALS expression','statement',3,'p_statement_assign','parser.py',70),
  ('expression -> term','expression',1,'p_expression_term','parser.py',74),
  ('expression -> expression PLUS expression','expression',3,'p_expression_plus','parser.py',78),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','parser.py',82),
  ('term -> NAME','term',1,'p_expression_name','parser.py',86),
  ('term -> NUMBER','term',1,'p_term_num','parser.py',90),
]
