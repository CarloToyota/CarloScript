import functions
tokens = {
    "+":"add",
    "-":"sub",
    "*":"mul",
    "/":"div",
}

def check_int_float(s):
    try:
        int(s)
        return "int"
    except ValueError:
        try:
            float(s)
            return "float"
        except ValueError:
            return None

def lexer(_tokens:dict, _input:str):
    found_tokens = []
    item_type = None
    for item in _input.split():
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
    output.append(current_action)
    return output

tokenized = lexer(tokens,"1 + 2.5 + 3 - 145")

def run(parsed:list):
    for action in parsed:
        if [*action][0] == "math":
            print(functions.math(action))

print(parse(tokenized))
run(parse(tokenized))