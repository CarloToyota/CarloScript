from toolbox import *

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

def math_oop(_input): # first solve the multiplication/ division then the rest its just a filter for the normal math
    need_oop = False
    where_mul_div = []
    mdoffset = 0
    for i in range(len(_input["math"])):
        unpacked = [*_input["math"][i]]
        if "id" in unpacked:
            if _input["math"][i]["id"] == "mul" or _input["math"][i]["id"] == "div":
                #print("Mul/Div found need OOP")
                need_oop = True
                where_mul_div.append(i)

    if not need_oop: #not nessisary
        return math(_input)
    else:
        for md in where_mul_div: # need to take the things left and right and combine them to the answer.
            #print(md)
            md += mdoffset
            if _input["math"][md]["id"] == "mul":
                #print("mul")
                try:
                    before = _input["math"][md - 1]["int"]
                except KeyError:
                    before = _input["math"][md - 1]["float"]
                try:
                    after = _input["math"][md + 1]["int"]
                except KeyError:
                    after = _input["math"][md + 1]["float"]

                if before is None or after is None:
                    raise Exception("no good")

                cur_solution = before * after

                #remove the pre-calculated items :
                del _input["math"][md]
                del _input["math"][md]
                del _input["math"][md-1]



                #put the new answer in
                if check_int_float(cur_solution) == "int":
                    _input["math"].insert(md-1, {"int":cur_solution})
                else:
                    _input["math"].insert(md-1, {"float":cur_solution})

                #print(_input)
                mdoffset -= 2  # now that we remove 3 and add 1 we gotta adjust the offset by 2 because there are 2 less
            else: #division
                #print("div")
                try:
                    before = _input["math"][md - 1]["int"]
                except KeyError:
                    before = _input["math"][md - 1]["float"]
                try:
                    after = _input["math"][md + 1]["int"]
                except KeyError:
                    after = _input["math"][md + 1]["float"]

                if not before or not after:
                    raise Exception("no good")

                cur_solution = before / after

                # remove the pre-calculated items :
                del _input["math"][md]
                del _input["math"][md]
                del _input["math"][md - 1]

                # put the new answer in
                if check_int_float(cur_solution) == "int":
                    _input["math"].insert(md - 1, {"int": cur_solution})
                else:
                    _input["math"].insert(md - 1, {"float": cur_solution})

                #print(_input)
                mdoffset -= 2  # now that we remove 3 and add 1 we gotta adjust the offset by 2 because there are 2 less
            print(_input)

    #now it is necisary to re check all of the terms to make sure they are still the correct type or not (int or float)
    for i,token in enumerate(_input["math"]):
        key = [*token]
        if "id" not in key:
            current_key = key[0]
            current_value = _input["math"][i][current_key]

            new_key = check_int_float(str(current_value))
            print(new_key)
            if new_key != current_key:
                _input["math"][i][new_key] = _input["math"][i].pop(current_key)

    return math(_input)
