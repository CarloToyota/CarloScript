def math(_input):
    dummy = None
    rule = None

    for i in range(len(_input["math"])):
        unpacked = [*_input["math"][i]]
        #print(unpacked)
        if not rule:
            if unpacked[0] == "int":
                #print("int at position ", i)
                if dummy is None:
                    dummy = int(_input["math"][i]["int"])
                else:
                    raise SyntaxError("Double numbers")
            elif unpacked[0] == "float":
                #print("float at position ", i)
                if dummy is None:
                    dummy = float(_input["math"][i]["float"])
                else:
                    raise SyntaxError("Double numbers")
            elif unpacked[0] == "id":
                #print("id at position ", i)
                rule = _input["math"][i]["id"] # next iteration, use the said rule to operate on it
        else:
            if unpacked[0] == "int":
                #print("int at position ", i)
                if rule == "add":
                    dummy += int(_input["math"][i]["int"])
                elif rule == "sub":
                    dummy -= int(_input["math"][i]["int"])
                elif rule == "mul":
                    dummy *= int(_input["math"][i]["int"])
                elif rule == "div":
                    dummy /= int(_input["math"][i]["int"])
                else:
                    print("Unknown rule")
            elif unpacked[0] == "float":
                #print("float at position ", i)
                if rule == "add":
                    dummy += float(_input["math"][i]["float"])
                elif rule == "sub":
                    dummy -= float(_input["math"][i]["float"])
                elif rule == "mul":
                    dummy *= float(_input["math"][i]["float"])
                elif rule == "div":
                    dummy /= float(_input["math"][i]["float"])
                else:
                    print("Unknown rule")
            rule = None

    return dummy