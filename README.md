# MapReduce Algorithm

This project represents how MapReduce Algorithm works in Hadoop. It is implemented using the ZeroMQ open-source library.

## Hadoop introduction

Apache Hadoop is a free framework written in Java for scalable, distributed software. The main parts of Hadoop are the MapReduce algorithm and the HDFS. The collaboration of components enables intensive computing processes with large amounts of data to be carried out on computer clusters.

HDFS stores a data set at multiple nodes in the cluster which ensures data security and fault tolerance.
Map Reduce is used to process the data stored in HDFS (Hadoop Distributed File System). 
Data processing works as follows: 
1) A query is sent to process a data set in the HDFS. 
2) Mapping: Hadoop identifies where this data is stored. 
3) Reduce: Now the query is broken into multiple parts and the results of all these multiple parts are combined and the overall result is sent back to the user.

## Project structure

The project consists of the following parts: one splitter, two mappers and two reducers. 
The input is a sentence. The sentence is divided into words and the words are stored and processed on the different nodes. Reducer counts the number of occurrences of each word. 

#### Splitter

Splitter processes the input of sentences. It sends the sentences to the mapper.

#### Mapper

Mapper divides sentences into the words, sorts words by the first letter and sends them to the reducers. The words start with letter a-l are sent to the first reducer. The words start with letter m-z are sent to the second reducer. 

#### Reducer 

Reducer receives the words, stores them locally into the dictionary and counts the number of occurrences of each word. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Python, pip, pipenv must be installed to run this project.

### START

Configure python environment

```
pipenv install
pipenv shell
```

Start the splitter in the same terminal.
(Terminal 1)
```
pipenv run python splitter.py 1
```
Start reducers and mappers each in different terminals
(Terminal 2)
```
pipenv run python mapper.py 1
```
(Terminal 3)
```
pipenv run python mapper.py 2
```
(Terminal 4)
```
pipenv run python reducer.py 1
```
(Terminal 5)
```
pipenv run python reducer.py 2
```

**Write some sentences in the terminal, where splitter runs, and look at how map reduce algorithm works :)**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
