def verifica (count, linha):
    #print('count: {}, linha {}, len(linha): {}'.format(count, linha, len(linha)))
    if count == len(linha):
        return True
    if linha[count] == ' ' or linha[count] == '\\n' or len(linha)-1 == count:
        return True
    elif linha[count] == '{':
        return True
    elif linha[count] == '}':
        return True
    elif linha[count] == '(':
        return True
    elif linha[count] == ')':
        return True
    elif linha[count] == '!':
        if linha[count+1] == "=":
            return True
        else:
            return True
    elif linha[count] == '+':
        return True
    elif linha[count] == '-':
        return True
    elif linha[count] == '*':
        return True
    elif linha[count] == '/':
        return True
    elif linha[count] == '<':
        if linha[count+1] == "=":
            return True
        else:
            return True
    elif linha[count] == '>':
        if linha[count+1] == "=":
            return True
        else:
            return True
    elif linha[count] == '=':
        return True
    elif linha[count] == '=' and linha[count+1] == '=':
        return True
    elif linha[count] == ',':
        return True
    elif linha[count] == ';':
        return True
    elif linha[count] == '$' and linha[count+1] == '$':
        return True
    elif linha[count] == '|' and linha[count+1] == '|':
        return True
    else:
        return False
