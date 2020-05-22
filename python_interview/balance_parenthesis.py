#!/usr/bin/python3

def is_balance_paren(item):
  is_balance = True
  i = 0
  lst = []
  while i <len(item) and is_balance:
    param = item[i]
    if param in "{[(":
      lst.append(param)
    else:
      if len(lst) == 0:
        is_balance = False
      else:
        top = lst.pop()
        if is_match(param, top):
          is_balance = True
    i +=1
  print(lst)
  if len(lst) == 0  and is_balance:
    return True
  else:
   return False


def is_match(top, param):
  if top == '{' and param=='}':
    return True
  if top == '[' and param == ']':
    return True
  if top == '(' and param == ')':
    return True
  return False

print(is_balance_paren("{[()]}"))
