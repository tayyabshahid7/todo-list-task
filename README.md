# Todo List Task

This Python program retrieves a list of TODO items from a mock online API and outputs the first 20 TODO items with even IDs, including their titles and completion status.

## Assumption

I'm using ``id`` field indicates the numbering of TODOs. 
I'm filtering all ``id's`` which are even.


## Features


All the functions are defined in ``functions.py``.

1. Fetch TODO items from an online source via an API call.
2. Filter out the first 20 TODO items that have an even ``ID``.
3. Print the filtered TODO items with their titles and completion status.


## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.x.
- You have a basic understanding of Python programming.

## Dependencies

- `requests`: This package is required to make HTTP requests to the online API for fetching TODO items.

## Installation

To install the necessary package(s), run the following command:

```shell
pip install -r requirments.txt
```
Or you can direclty install the package using this command.

```shell
pip install requests
```

## How to run this app

To run this app run the following command:


```shell
 python main.py      
 ```

After running this command you will see the first 20 even number todos printed in command line.


## Docker installation

1. Build the Docker image:

```shell 
docker build -t python-project .
```  

2. Run the Docker container from the image:

```shell 
 docker run --name some-python-app -d  python-project 
```  


## Test Cases

To run test cases run this command:
```shell
python test.py 
```

