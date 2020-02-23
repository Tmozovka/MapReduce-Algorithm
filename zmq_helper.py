import zmq

context = zmq.Context()

def create_push_socket_with_binding(src, port):
    push_socket = context.socket(zmq.PUSH)  # create a push socket
    push_socket.bind(_create_adr(src, port))  # bind socket to address
    return push_socket

def create_push_socket_with_connecting(src, port):
    push_socket = context.socket(zmq.PUSH)  # create a push socket
    push_socket.connect(_create_adr(src, port))  # connect socket to address
    return push_socket

def create_pull_socket_with_connecting(src, port):
    pull_socket = context.socket(zmq.PULL)  
    pull_socket.connect(_create_adr(src, port))  
    return pull_socket

def create_pull_socket_with_binding(src, port):
    pull_socket = context.socket(zmq.PULL)  
    pull_socket.bind(_create_adr(src, port))  
    return pull_socket

def _create_adr(src, port):
    return "tcp://" + src + ":" + port