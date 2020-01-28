import os

# La clase nodo define una 'red'


class Node:
    def __init__(self, ip):
        self.ip = ip  # esto indica la IP de la red.
        # este atributo indica a que otras red se conecta en una vía. En este caso, una lista de redes (nodos).
        self.networks = []


# Esta función consigue el nodo con tan solo la IP.
def get_node(ip):
    for x in network:
        if(x.ip == ip):
            return x


# Esta función determina si hay conexión de una via desde el nodo actual.
def root_has_connection_to(root, ip):
    for x in root.networks:
        if (x == ip):
            return True
        else:
            return False


# Esta función se utiliza cuando se va leer un comando.
# EJEMPLO: TELNET 192.168.1.1
# En este caso, esta función retorna una lista.
# ['TELNET', '192.168.1.1']
def root(node):
    cmd = list(map(str, input('({0}) > '.format(node.ip)).split()))
    return cmd


# Esta función simplemente limpia la consola (por estetica)
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Esta función recibe una IP de destino para conectarse a ella.
# Aun falta agregar lo de verificar si hay conexión entre la red que se hará TELNET.
def telnet(target):
    current_node = get_node(target)
    print('Estas conectado a:', current_node.ip)
    execute(root(current_node), current_node, network)


# Esta función retorna al modo base.
def exit(node):
    if(node.ip != 'BASE'):
        current_node = Node('BASE')
        node = current_node
        print('Usted ha retornado a modo base.')
    else:
        print('Usted ya se encuentra en modo base.')
    execute(root(node), node, network)


def ping(root_node, target):
    if(root_node.ip == 'BASE'):
        print('No puede hacer PING desde el modo base.')
    else:
        if(len(root_node.networks) != 0):
            for x in root_node.networks:
                if(x == target.ip and len(target.networks) != 0):
                    for y in target.networks:
                        if(y == root_node.ip):
                            print('Su ping ha sido exitoso.')
                else:
                    print('Su ping ha fallado.')
        else:
            print('Su ping ha fallado.')
    execute(root(root_node), root_node, network)


# Esta función verifica si está en modo base, o si está conectado a una red.
def is_base(node):
    if(node.ip == 'BASE'):
        print('Actualmente estas en modo BASE')
    else:
        print('Estas conectado a la red:', node.ip)
    execute(root(node), node, network)


# Esta función recibe la red actual, y la red de destino para agregar la conexión de una vía.
# EJEMPLO: Si conecto la 192.168.1.1 con la 192.168.1.2
# Dicha conexión es de una via 192.168.1.1 -> 192.168.1.2
# Lo que quiere decir que para que sea de doble via,
# se debe agregar la 192.168.1.1 desde la 192.168.1.2
def add(node, ip):
    node.networks.append(ip)
    print('Has agregado la red:', ip, ' a', node.ip)
    execute(root(node), node, network)


# Esta es una función que recibe el input como parámetro.
# Comunmente procedente de la función root()
# La red actual, y la lista que contiene las IP de toda la red.
# Se encarga de identificar cual comando se va a ejecutar.
def execute(cmd_input, current_node, network):
    node = current_node  # red actual
    cmd = cmd_input  # input de root()
    # variable de utilidad para verificar si la red existe o no. (0 = no existe, 1 = existe).
    trigger = 0
    if (cmd[0].lower() == "help"):
        help()
    if (cmd[0].lower() == "mode"):
        is_base(node)
    if (cmd[0].lower() == "exit"):
        exit(node)
    if (cmd[0].lower() == "ping"):
        ping(node, get_node(cmd[1]))
    if (cmd[0].lower() == "telnet"):
      # Este for se encarga de verificar si la red que se quiere hacer TELNET existe.
        for x in network:
            if(x.ip == cmd[1]):
                if(node.ip == 'BASE'):
                    telnet(cmd[1])
                else:
                    trigger = 0
                    for y in node.networks:
                        if(y == cmd[1]):
                            telnet(cmd[1])
                            trigger = 1
                    if(trigger == 0):
                        print(
                            'La red actual no tiene conexion a la red', cmd[1])
                        execute(root(node), node, network)

    if (cmd[0].lower() == "add"):
      # Este for se encarga de verificar si la IP la cual se quiere agregar existe.
        for x in range(0, len(network)):
            if(network[x].ip == cmd[1]):
                if(root_has_connection_to(node, cmd[1])):
                    return 0
                add(node, cmd[1])
                trigger = 1
        if (trigger == 0):
            print('Esta red no existe.')
            execute(root(node), node, network)


# Esta función se encarga de mostrar en pantalla un texto de ayuda.
def help():
    print('Los comandos disponibles actualmente son: ')
    print("""
-	TELNET   
Este comando es el único que puede utilizarse desde el modo base del programa. Me permite “conectarme” a una red y ejecutar otros comandos desde la misma. Desde el modo base puedo conectarme a cualquier red, sin embargo, desde una red específica solo puedo conectarme a las redes con las que tengo conexión establecida.
Sintaxis del comando: TELNET red

-	ADD
Este comando me permite agregar conexión de una vía desde la red en la que me encuentro hacia otra red cual sea.
Sintaxis del comando: ADD red

-	PING
Este comando me permite probar si existe comunicación entre la red en la cual estoy conectado, y otra red cual sea.
Sintaxis del comando: PING red

-	TRACERT
Este comando me permite imprimir la ruta por la cual estoy alcanzando una red específica, o las rutas, si hay más de una.
Sintaxis del comando: TRACERT red.

-	MODE
Este comando me permite saber si me encuentro en modo base, o conectado a una red específica. Les dejo a su creatividad el mecanismo de saber el modo. 

-	EXIT
Este comando solo puede utilizarse cuando estamos conectados a una red. Nos devuelve a modo base.
""")
    input('Presione cualquier tecla para volver a la consola. \n')
    cls()
    print("Inserte un comando. Si necesita ayuda escriba 'help' \n")
    # Esto está aqui con el fin de poder volver a la consola luego de haber impreso el mensaje.
    execute(root(current_node), current_node, network)


# Esta lista contiene todas las IP de la red completa.
# Dentro irán elementos tipo 'node' que son cada red con IP, y conexiones.
network = []
# Esta variable indica cual es el nodo en el cual se encuentra actualmente, por default es BASE.
current_node = Node('BASE')

# Este while se encarga de leer las IP al inicio del programa.
# Para de leer cuando se da espacio, y no existe texto (no hay más IP).
while True:
    inp = input('(INTRODUZCA UNA IP) > ')
    if inp == "":
        break
    new_node = Node(inp)
    network.append(new_node)

# Texto de entrada a la consola, lectura de comandos mediantes las funciones antes declaradas.
print('Bienvenido a la consola ({0}).'.format(current_node.ip))
print("Inserte un comando. Si necesita ayuda, escriba 'help'. \n")
execute(root(current_node), current_node, network)
