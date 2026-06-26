#Lexer for the calculator
from typing import Any

tokens = {
    "+":"add",
    "-":"sub",
    "*":"mul",
    "/":"div",
}

def lexer(_tokens:dict, _input:str):
    found_tokens = []
    for item in _input.split():
        if item in _tokens:
            found_tokens.append(_tokens[item])
        else:
            if item.isdigit():
                found_tokens.append({"int":int(item)})
            else:
                found_tokens.append("Error")

    return found_tokens

def parse(_tokens:list):
    dummy = None
    skip_next = False
    for i in range(len(_tokens)):
        if skip_next:
            skip_next = False
        elif _tokens[i] == "Error":
            raise ValueError
        elif type(_tokens[i])==dict:
            if not dummy: # it's the first number
                dummy = _tokens[i]["int"]
            else:
                print(i)
                raise ValueError
        elif _tokens[i] == "add":
            if dummy:
                dummy += _tokens[i+1]["int"]
                skip_next = True #skip next because now go to next oporator
            else:
                raise ValueError
        elif _tokens[i] == "sub":
            if dummy:
                dummy -= _tokens[i+1]["int"]
                skip_next = True #skip next because now go to next oporator
            else:
                raise ValueError
        elif _tokens[i] == "mul":
            if dummy:
                dummy *= _tokens[i+1]["int"]
                skip_next = True #skip next because now go to next oporator
            else:
                raise ValueError
        elif _tokens[i] == "div":
            if dummy:
                dummy /= _tokens[i+1]["int"]
                skip_next = True #skip next because now go to next oporator
            else:
                raise ValueError

    return dummy

tokenized = lexer(tokens,"1 + 2 + 3 - 145")

print(tokenized)
print(parse(tokenized))