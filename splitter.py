import constPipe
import pickle
from zmq_helper import create_push_socket_with_binding

push_socket_mapper_1 = create_push_socket_with_binding(constPipe.MAPPER_SRC1, constPipe.MAPPER_PORT1)
push_socket_mapper_2 = create_push_socket_with_binding(constPipe.MAPPER_SRC2, constPipe.MAPPER_PORT2)

print("Write your sentence hier. ")
sentence = input()
count = 0
while sentence != "END":
    print("I send %s", sentence)
    if count % 2 == 0:
        push_socket_mapper_1.send(pickle.dumps((1, sentence)))  # send sentence to mapper
    else:
        push_socket_mapper_2.send(pickle.dumps((2, sentence)))
    count += 1
    print(""" Write one more sentence hier or "END" to stop the splitter. """)
    sentence = input()
