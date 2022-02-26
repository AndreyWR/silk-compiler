import An_Lexico
import An_Sintatico
import An_Semantico

token_list = list()

arq = open('Codigos/Codigo3.txt', 'r')
texto = arq.readlines()

token_list, Lista_Tokens_without_lines = An_Lexico.an_lexico(texto)

An_Sintatico.begin(token_list, Lista_Tokens_without_lines)

An_Semantico.main_semantico(token_list, Lista_Tokens_without_lines)
