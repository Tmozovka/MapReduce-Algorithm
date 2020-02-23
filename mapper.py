import pickle
import constPipe
import time 
import sys
from zmq_helper import *

me = int(sys.argv[1])
if me == 1:
    pull_socket = create_pull_socket_with_connecting(constPipe.MAPPER_SRC1, constPipe.MAPPER_PORT1)
else:
    pull_socket = create_pull_socket_with_connecting(constPipe.MAPPER_SRC2, constPipe.MAPPER_PORT2)
print("{} started".format(me))

push_socket_1 = create_push_socket_with_connecting(constPipe.REDUCER_SRC1, constPipe.REDUCER_PORT1)
push_socket_2 = create_push_socket_with_connecting(constPipe.REDUCER_SRC2, constPipe.REDUCER_PORT2)


while True:
    work = pickle.loads(pull_socket.recv())  # receive work from splitter
    print("{} received workload {} from {}".format(me, work[1], work[0])) 
    words =  work[1].lower().split(' ')
    for word in words:
        if ord(word[0]) < ord('m'):
            print("send {0} to 1".format(word))
            push_socket_1.send(pickle.dumps((1, word)))
        else:
            print("send {0} to 2".format(word))
            push_socket_2.send(pickle.dumps((2, word)))