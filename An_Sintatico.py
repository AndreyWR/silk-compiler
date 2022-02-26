global line
table_list = list()
stack = list()
grammar_list = list()
error_list = list()

def open_LR_table():

    arq = open('TableLR.txt', 'r')
    texto = arq.readlines()
    line_list = list()
    for line in texto:

        i = 0
        token = ''
        while i < len(line):
            while line[i] != ' ' and line[i] != '\t' and line[i] != '\n':
                token += line[i]
                i += 1
            if token != '':
                line_list.append(token)
            token = ''
            i += 1
        table_list.append(line_list[:])
        line_list.clear()

    #for i in range(0, len(table_list)):
    #    print(table_list[i])


def open_grammar():

    grammar_line = list()
    arq = open('GRAMATICA.txt', 'r')
    texto = arq.readlines()

    for line in texto:
        token = ''
        grammar_line.append(line[0] + line[1])
        i = 2
        while i < len(line):
            if line[i] != '\n':
                token += line[i]
            i += 1
        grammar_line.append(token)
        grammar_list.append(grammar_line[:])
        grammar_line.clear()

    #for i in range(0, len(grammar_list)):
    #    print(grammar_list[i])


def open_error_list():

    error_line = list()
    arq = open('error_list.txt', 'r')
    texto = arq.readlines()

    for line in texto:
        token = ''
        error_line.append(line[0] + line[1])
        i = 3
        while i < len(line):
            if line[i] != '\n':
                token += line[i]
            i += 1
        error_line.append(token)
        error_list.append(error_line[:])
        error_line.clear()

    # for i in range(0, len(error_list)):
    #    print(error_list[i])


def set_line(token_list_with_lines, index_token_list):
    global line
    i = 0
    while i < len(token_list_with_lines):

        if type(token_list_with_lines[i]) is tuple:
            line = token_list_with_lines[i]
            del token_list_with_lines[i]
        if i == index_token_list:
            del token_list_with_lines[i]
            break

        i += 1


def error(table_list=[], index_line=0, index_column=0, stack=[], token_list_with_lines=[], token_list=[], token_list_with_lines_inline=[]):
    abreParent = 0
    abrechave = 0
    countIF = 0
    estruturas = 0
    line = 0

    for i in range(len(token_list_with_lines_inline[0])):
        '''print('i: {}'.format(i))
        print('tamanho: {}'.format(len(token_list_with_lines_inline[0])))
        print('token_list_with_lines: {} \n'.format(token_list_with_lines_inline[0][i]))'''

        if(token_list_with_lines_inline[0][i] == '<BIGBANG>' or token_list_with_lines_inline[0][i] == '<ELSE>' or token_list_with_lines_inline[0][i] == '<ENTROPIA>'):
            if i < 26:
                if (token_list_with_lines_inline[0][i+1] != '<ABRE_CHAVE>'):
                    print('faltou {} ao fim da linha {}'.format('{', line))
                    exit()

            if i == len(token_list_with_lines_inline[0])-1:
                if(token_list_with_lines_inline[0][i] != '<FECHA_CHAVE>'):
                    print('faltou {} ao fim da linha {}'.format('}', line))
                    exit()

        if(token_list_with_lines_inline[0][i] == '<IF>'):
            countIF += 1

        if(token_list_with_lines_inline[0][i] == '<ELSE>'):
            countIF -= 1
            if(countIF < 0):
                print('Faltou IF para o else na linha {}.'.format(line))
                exit()

        if type(token_list_with_lines_inline[0][i]) is tuple:

            if type(token_list_with_lines_inline[0][i+1]) is tuple:
                line = token_list_with_lines_inline[0][i][1]
                continue
            #  print('Qual sera essa linha: {}'.format(token_list_with_lines_inline[0][i][1]))
            #  print(token_list_with_lines_inline[0][i-1])

            if(i > 0):
                if (token_list_with_lines_inline[0][i-1] != '<PONTO_VIRGULA>') and (token_list_with_lines_inline[0][i][1] > 1) and (type(token_list_with_lines_inline[0][i-1]) is not tuple):
                    if (token_list_with_lines_inline[0][i][1]-1 > 1) and (token_list_with_lines_inline[0][i-1] != '<ABRE_CHAVE>') and (token_list_with_lines_inline[0][i-1] != '<FECHA_CHAVE>') and (token_list_with_lines_inline[0][i-1] != '<ABRE_PARENT>') and (token_list_with_lines_inline[0][i-1] != '<FECHA_PARENT>'):
                        print('faltou ; ao fim da linha {}.'.format(line))
                        exit()

                #else:
            line = token_list_with_lines_inline[0][i][1]

        elif (token_list_with_lines_inline[0][i] == '<BIGBANG>' or
              token_list_with_lines_inline[0][i] == '<ELSE>' or
              token_list_with_lines_inline[0][i] == '<FOR>' or
              token_list_with_lines_inline[0][i] == '<WHILE>' or
              token_list_with_lines_inline[0][i] == '<IF>' or
              token_list_with_lines_inline[0][i] == '<ENTROPIA>'):
            estruturas += 1

        elif(token_list_with_lines_inline[0][i] == '<WHILE>' or
             token_list_with_lines_inline[0][i] == '<FOR>' or
             token_list_with_lines_inline[0][i] == '<WHILE>' or
             token_list_with_lines_inline[0][i] == '<IF>') and (token_list_with_lines_inline[0][i+1] != '<ABRE_PARENT>'):
            print('faltou ( ao fim da linha {}'.format(token_list_with_lines_inline[0][i]))

        elif(token_list_with_lines_inline[0][i] == '<ABRE_PARENT>'):
            abreParent += 1

        elif(token_list_with_lines_inline[0][i] == '<ABRE_CHAVE>'):
            if(abreParent > 0):
                print('faltou ) na linha {}'.format(line))
            else:
                abrechave += 1

        elif(token_list_with_lines_inline[0][i] == '<FECHA_PARENT>'):
            abreParent -= 1
            if(token_list_with_lines_inline[0][i+1] != '<ABRE_CHAVE>'):
                print('faltou {} na linha {}'.format('{', line))
                exit()

        elif(token_list_with_lines_inline[0][i] == '<FECHA_CHAVE>'):
            abrechave -= 1
            estruturas -= 1
            if i == len(token_list_with_lines_inline[0])-1 and abrechave > 0:
                print('faltou {} na linha {}'.format('}', line))
                exit()

        elif(token_list_with_lines_inline[0][i] == '<OP_REL_IG_IG>' or token_list_with_lines_inline[0][i] == '<OP_REL_MENOR>' or token_list_with_lines_inline[0][i] == '<OP_REL_MAIOR>' or token_list_with_lines_inline[0][i] == '<OP_REL_MENOR_IG>' or token_list_with_lines_inline[0][i] == '<OP_REL_MAIOR_IG>' or token_list_with_lines_inline[0][i] == '<OP_REL_DIF_IG>'):

            if ((token_list_with_lines_inline[0][i-1] != '<ID>') or
                (token_list_with_lines_inline[0][i+1] != '<ID>' and
                token_list_with_lines_inline[0][i+1] != '<NUM_BOOL_TRUE>' and
                token_list_with_lines_inline[0][i+1] != '<NUM_BOOL_FALSE>' and
                token_list_with_lines_inline[0][i+1] != '<NUM_INTEGER>' and
                    token_list_with_lines_inline[0][i+1] != '<NUM_FLOAT>')):
                print('faltou operando na linha {}.'.format(line))
                exit()

        elif(token_list_with_lines_inline[0][i] == '<OP_ARIT_MAIS>' or token_list_with_lines_inline[0][i] == '<OP_ARIT_MULTI>' or token_list_with_lines_inline[0][i] == '<OP_ARIT_MENOS>' or token_list_with_lines_inline[0][i] == '<OP_ARIT_DIV>' or token_list_with_lines_inline[0][i] == '<OP_LOGICO_E>' or token_list_with_lines_inline[0][i] == '<OP_LOGICO_OU>'):

            if ((token_list_with_lines_inline[0][i-1] != '<ID>' and
                token_list_with_lines_inline[0][i-1] != '<NUM_BOOL_TRUE>' and
                token_list_with_lines_inline[0][i-1] != '<NUM_BOOL_FALSE>' and
                token_list_with_lines_inline[0][i-1] != '<NUM_INTEGER>' and
                token_list_with_lines_inline[0][i-1] != '<NUM_FLOAT>' and
                token_list_with_lines_inline[0][i-1] != '<FECHA_PARENT>') or
                (token_list_with_lines_inline[0][i+1] != '<ID>' and
                token_list_with_lines_inline[0][i+1] != '<NUM_BOOL_TRUE>' and
                token_list_with_lines_inline[0][i+1] != '<NUM_BOOL_FALSE>' and
                token_list_with_lines_inline[0][i+1] != '<ABRE_PARENT>' and
                token_list_with_lines_inline[0][i+1] != '<NUM_INTEGER>' and
                    token_list_with_lines_inline[0][i+1] != '<NUM_FLOAT>')):
                print('faltou operando na linha {}.'.format(line))
                exit()

        elif ((token_list_with_lines_inline[0][i] == '<ID>' or
              token_list_with_lines_inline[0][i] == '<NUM_BOOL_TRUE>' or
              token_list_with_lines_inline[0][i] == '<NUM_BOOL_FALSE>' or
              token_list_with_lines_inline[0][i] == '<NUM_INTEGER>' or
              token_list_with_lines_inline[0][i] == '<NUM_FLOAT>' or
              token_list_with_lines_inline[0][i] == '<FECHA_PARENT>') or
              (token_list_with_lines_inline[0][i] == '<ID>' or
              token_list_with_lines_inline[0][i] == '<NUM_BOOL_TRUE>' or
              token_list_with_lines_inline[0][i] == '<NUM_BOOL_FALSE>' or
              token_list_with_lines_inline[0][i] == '<ABRE_PARENT>' or
              token_list_with_lines_inline[0][i] == '<NUM_INTEGER>' or
                token_list_with_lines_inline[0][i] == '<NUM_FLOAT>')):
            if ((token_list_with_lines_inline[0][i+1] == '<ID>' or
                token_list_with_lines_inline[0][i+1] == '<NUM_BOOL_TRUE>' or
                token_list_with_lines_inline[0][i+1] == '<NUM_BOOL_FALSE>' or
                token_list_with_lines_inline[0][i+1] == '<ABRE_PARENT>' or
                token_list_with_lines_inline[0][i+1] == '<NUM_INTEGER>' or
                    token_list_with_lines_inline[0][i+1] == '<NUM_FLOAT>')):
                print('faltou operador na linha {}'.format(line))
                exit()

        #  print('line: {}'.format(line))


def begin(token_list_with_lines, token_list):
    open_LR_table()
    open_grammar()
    open_error_list()

    index_column = 0
    index_line = 1
    stack.append('0')
    index_token_list = 0
    left_production = []
    right_production = []
    token_list_with_lines_inline = list()
    token_list_with_lines_inline.append(token_list_with_lines[:])

    index_token_list_lines = 0
    k = 0

    #  print(table_list)

    set_line(token_list_with_lines, index_token_list)

    error(table_list, index_line, index_column, stack, token_list_with_lines, token_list, token_list_with_lines_inline)
    while True:
        for i in range(0, len(table_list[0])):
            if token_list[index_token_list] == table_list[0][i]:
                index_column = i
                break

        if table_list[index_line][index_column][:1] == 's':

            stack.append(str(token_list[index_token_list]))
            stack.append(str(int(table_list[index_line][index_column][1:])))

            index_token_list += 1

            index_line = int(table_list[index_line][index_column][1:]) + 1
            set_line(token_list_with_lines, index_token_list)
            continue

        elif table_list[index_line][index_column][:1] == 'r':
            production = ''

            for i in range(0, len(grammar_list)):

                if int(table_list[index_line][index_column][1:]) == int(grammar_list[i][0]):
                    production = grammar_list[i][1]
                    break

            left_production = production[1:3]
            right_production = production[6:]

            tam = right_production.count(' ') + 1
            left_production = left_production.strip()

            if right_production == "''":
                tam = 0

            for i in range(tam*2):
                stack.pop()

            col = 0
            line = int(stack[-1]) + 1
            stack.append(left_production)

            for i in range(len(table_list[0])):
                if left_production == table_list[0][i]:
                    col = i
                    break

            stack.append(table_list[line][col])
            index_line = int(stack[-1]) + 1
            continue

        elif token_list[index_token_list] == '$':
            if stack[-1] == '46':
                print('Aceita')
                break
            else:
                print('nao aceita')
                #  print(token_list_with_lines_inline)
            break

        elif len(token_list) == 0:
            print('Codigo vazio.')
            break
