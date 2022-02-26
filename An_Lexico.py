import Verifica


def an_lexico(texto):

    Count_linha = 1
    lista_var = []
    Lista_Tokens = []
    Lista_Tokens_without_lines = []
    for linha in texto:  # Percorre Texto

        N_linha = 'linha: ', Count_linha
        Lista_Tokens.append(N_linha)
        count = 0
        ver = False
        while count < len(linha):  # Percorre Linha
            if linha[count] == ' ' or linha[count] == '\t' or linha[count] == '\n':
                count += 1
                continue
            elif count == len(linha)-1 and len(linha) > 2:
                count += 1
                continue
            elif linha[count].isnumeric():
                int = True
                Erro = False
                while linha[count].isnumeric() or linha[count] == '.' or linha[count] == ',':
                    count += 1
                    if (linha[count] == '.' and (not linha[count+1].isnumeric())) or linha[count] == ',':
                        Erro = True
                    if linha[count] == '.':
                        int = False
                if Erro == True:

                    Lista_Tokens.append("<ID_INVALIDO>")
                else:
                    if int == True:
                        Lista_Tokens.append("<NUM_INTEGER>")
                    else:
                        Lista_Tokens.append("<NUM_FLOAT>")
                continue
            elif linha[count] == '{':
                Lista_Tokens.append('<ABRE_CHAVE>')

            elif linha[count] == '}':
                Lista_Tokens.append('<FECHA_CHAVE>')
                ver = True
            elif linha[count] == '(':
                Lista_Tokens.append('<ABRE_PARENT>')

            elif linha[count] == ')':
                Lista_Tokens.append('<FECHA_PARENT>')

            elif linha[count] == '&' and linha[count+1] == '&':
                Lista_Tokens.append('<OP_LOGICO_E>')
                count += 1
            elif linha[count] == '!':
                if linha[count+1] == "=":
                    Lista_Tokens.append('<OP_REL_DIF_IG>')
                    count += 1
                else:
                    Lista_Tokens.append('<OP_LOGICO_NAO_LOGICO>')
            elif linha[count] == '+':
                Lista_Tokens.append('<OP_ARIT_MAIS>')
            elif linha[count] == '-':
                Lista_Tokens.append('<OP_ARIT_MENOS>')
            elif linha[count] == '*':
                Lista_Tokens.append('<OP_ARIT_MULTI>')
            elif linha[count] == '/':
                Lista_Tokens.append('<OP_ARIT_DIV>')
            elif linha[count] == '<':
                if linha[count+1] == "=":
                    Lista_Tokens.append('<OP_REL_MENOR_IG>')
                    count += 1
                else:
                    Lista_Tokens.append('<OP_REL_MENOR>')
            elif linha[count] == '>':
                if linha[count+1] == "=":
                    Lista_Tokens.append('<OP_REL_MAIOR_IG>')
                    count += 1
                else:
                    Lista_Tokens.append('<OP_REL_MAIOR>')
            elif linha[count] == '=':
                if linha[count+1] == "=":
                    Lista_Tokens.append('<OP_REL_IG_IG>')
                    count += 1
                else:
                    Lista_Tokens.append('<ATRIBUICAO>')
            elif linha[count] == ';':
                Lista_Tokens.append('<PONTO_VIRGULA>')
            elif linha[count] == '$' and linha[count+1] == '$':
                #Lista_Tokens.append('<COMENTARIO>') #opcional
                while linha[count] != '\n':
                    count += 1
            elif linha[count] == '|' and linha[count+1] == '|':
                Lista_Tokens.append('<OP_LOGICO_OU>')
                count += 1
            elif linha[count] == 'w' and linha[count+1] == 'h' and linha[count+2] == 'i' and linha[count+3] == 'l' and linha[count+4] == 'e' and  (not linha[count+5].isalpha()):
                Lista_Tokens.append('<WHILE>')
                count += 5
                continue
            elif linha[count] == 'B' and linha[count+1] == 'i' and linha[count+2] == 'g' and linha[count+3] == 'B' and linha[count+4] == 'a' and linha[count+5] == 'n' and linha[count+6] == 'g' and  (not linha[count+7].isalpha()):
                Lista_Tokens.append('<BIGBANG>')
                count += 7
                continue
            elif linha[count] == 'p' and linha[count + 1] == 'r' and linha[count + 2] == 'i' and linha[count + 3] == 'n' and linha[count + 4] == 't' and  (not linha[count+5].isalpha()):
                while linha[count] != '\n':
                    count += 1
                #Lista_Tokens.append('<PRINT>')
                #count += 5
                continue
            elif linha[count] == 'i' and linha[count + 1] == 'n' and linha[count + 2] == 'p' and linha[count + 3] == 'u' and linha[count + 4] == 't' and  (not linha[count+5].isalpha()):
                Lista_Tokens.append('<INPUT>')
                count += 5
                continue
            elif linha[count] == 'E' and linha[count + 1] == 'n' and linha[count + 2] == 't' and linha[count + 3] == 'r' and linha[count + 4] == 'o' and linha[count + 5] == 'p' and linha[count + 6] == 'i' and linha[count + 7] == 'a' and  (not linha[count+8].isalpha()):
                Lista_Tokens.append('<ENTROPIA>')
                count += 8
                continue
            elif linha[count] == 'i' and linha[count + 1] == 'f' and  (not linha[count+2].isalpha()):
                Lista_Tokens.append('<IF>')
                count += 2
                continue
            elif linha[count] == 'f' and linha[count + 1] == 'o' and linha[count + 2] == 'r' and  (not linha[count+3].isalpha()):
                Lista_Tokens.append('<FOR>')
                count += 3
                continue
            elif linha[count] == 'e' and linha[count + 1] == 'l' and linha[count + 2] == 's' and linha[count + 3] == 'e' and  (not linha[count+4].isalpha()):
                Lista_Tokens.append('<ELSE>')
                count += 4
                continue
            elif linha[count] == 's' and linha[count + 1] == 'n' and linha[count + 2] == 'g' and linha[count + 3] == 'I' and  (not linha[count+4].isalpha()):
                Lista_Tokens.append('<TIPO_NUM_INTEGER>')
                count += 4
                continue
            elif linha[count] == 's' and linha[count + 1] == 'n' and linha[count + 2] == 'g' and linha[count + 3] == 'F' and  (not linha[count+4].isalpha()):
                Lista_Tokens.append('<TIPO_NUM_FLOAT>')
                count += 4
                continue
            elif linha[count] == 's' and linha[count + 1] == 'n' and linha[count + 2] == 'g' and linha[count + 3] == 'B' and  (not linha[count+4].isalpha()):
                Lista_Tokens.append('<TIPO_NUM_BOOL>')
                count += 4
                continue
            elif linha[count] == 't' and linha[count + 1] == 'r' and linha[count + 2] == 'u' and linha[count + 3] == 'e' and  (not linha[count+4].isalpha()):
                Lista_Tokens.append('<NUM_BOOL_TRUE>')
                count += 4
                continue
            elif linha[count] == 'f' and linha[count + 1] == 'a' and linha[count + 2] == 'l' and linha[count + 3] == 's' and linha[count + 4] == 'e' and  (not linha[count+5].isalpha()):
                Lista_Tokens.append('<NUM_BOOL_FALSE>')
                count += 5
                continue
            else:
                name_id = ''
                aux = count
                while not(Verifica.verifica(count + 1, linha)):
                    name_id += str(linha[count])
                    count += 1
                else:
                    name_id += str(linha[count])
                if '<Entropia>' not in Lista_Tokens:
                    lista_var.append([Lista_Tokens[-1], name_id])
                print(name_id)
                name_id = ''
                if ver == False:
                    if (ord(linha[count]) >= 65 and ord(linha[count]) <= 90) == True or (ord(linha[count]) >= 97 and ord(linha[count]) <= 122) == True:
                        Lista_Tokens.append('<ID>')
                        #print('linha[count]', linha[count])
                    else:
                        Lista_Tokens.append('<ID_INVALIDO>')
                else:
                    ver = False

            count += 1 #countprincipal

        Count_linha += 1

    for i in range(0, len(Lista_Tokens)):
        if not type(Lista_Tokens[i]) is tuple:
            Lista_Tokens_without_lines.append(Lista_Tokens[i])

    print(lista_var)
    print(Lista_Tokens)
    Lista_Tokens_without_lines.append('$')
    return Lista_Tokens, Lista_Tokens_without_lines
