#Maquina de esta basada en diccionario, para dos unidades de memoria, que nos permite 4 estados, 
#la razón del codificador es una entrada y 2 de salidas. 
#Se ingresa cada bit , del byte del mensaje  y se pasa por la 
#maquina de estado para codificar  cada uno de ellos.

#Mensaje del tamaño de un byte
codigo = ['0', '1', '1', '1', '0', '1', '1', '0']
#Salida de cada estado  segun el valor de entrada
transition_code = {
                '00' : {'0': '00','1': '11'},
                '01' : {'0': '11','1': '00'},
                '10' : {'0': '10','1': '01'},
                '11' : {'0': '01','1': '10'}
                }
#Transicion entre estados
transition_state = {
                '00' : {'0': '00','1': '10'},
                '01' : {'0': '00','1': '10'},
                '10' : {'0': '01','1': '11'},
                '11' : {'0': '01','1': '11'}
                }
def code_generation (code):
    state = '00'# Estado inicial
    s = []
    for t in range(0,len(code)):
        s.append(transition_code[state][code[t]]) # Codigo de salida 
        state = transition_state[state][code[t]] # Cambio de estado
    return (s)
print(code_generation(codigo))

            
