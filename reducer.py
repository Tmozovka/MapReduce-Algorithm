import pickle
import constPipe
import time 
import sys
from zmq_helper import *


def add_word_to_dict(word, di):
    if word in di.keys():
            di[word]+=1
    else:
            di[word]=1
    return di

me = int(sys.argv[1])
if me == 1:
    pull_socket = create_pull_socket_with_binding(constPipe.REDUCER_SRC1, constPipe.REDUCER_PORT1)
else:
    pull_socket = create_pull_socket_with_binding(constPipe.REDUCER_SRC2, constPipe.REDUCER_PORT2)
print("{} started".format(me))

result = {}
while True:
    work = pickle.loads(pull_socket.recv())  # receive work from mapper
    print("{} received workload {} from {}".format(me, work[1], work[0]))  # pretend to work
    result = add_word_to_dict(work[1], result)
    print(result)


