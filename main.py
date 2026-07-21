import functions
import re
from toolbox import *
import sys

tokens = {
    "+":"add",
    "-":"sub",
    "*":"mul",
    "/":"div",
}

def lexer(_tokens:dict, _input:str):
    found_tokens = []

    pattern = r"(?:\d+\.\d*|\.\d+|\d+)(?:[eE][+-]?\d+)?|[+\-*/]" #matches them including scientific notation

    for item in re.findall(pattern, _input):
        if item in _tokens:
            found_tokens.append({"id":_tokens[item]})
        else:
            item_type = check_int_float(item)
            if not item_type:
                found_tokens.append("Error")
            elif item_type == "int":
                found_tokens.append({"int":int(item)})
            elif item_type == "float":
                found_tokens.append({"float":float(item)})

    return found_tokens

def parse(_tokens:list):
    if "Error" in _tokens: raise ValueError
    output = []
    #current_action = {}
    current_action = {"math":[]} #just for now
    for i in range(len(_tokens)):
        unpacked = [*_tokens[i]]
        #print(unpacked)
        if unpacked[0] == "int" or unpacked[0] == "float":
            #print("number at position ", i)
            current_action["math"].append(_tokens[i])
        elif unpacked[0] == "id":
            #print("id at position ", i)
            current_action["math"].append(_tokens[i])
    if [*current_action["math"][-1]][0] == "id":
        raise ValueError("Operator cant be the last thing in a math")
    output.append(current_action)
    return output

try:
    with open(sys.argv[1], "r") as file:
        content = file.read()
        tokenized = lexer(tokens, content)
        print(tokenized)
except OSError:
    tokenized = lexer(tokens, sys.argv[1])

def run(parsed:list):
    for action in parsed:
        if [*action][0] == "math":
            print(functions.math_oop(action))

#print(parse(tokenized))
run(parse(tokenized))
