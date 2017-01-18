# Overview
There are two ways to run this python code:

  - Bash
  - Docker container

### Bash 
```sh
$ python createll.py
```

The output file is:
```sh
./linkedlistpageViews.csv
```


### Docker Container 

##### Docker Environment Setup 
Clone this repository.
Go to the directory where the file "Dockerfile" is located.
Run this to build a docker image called ubuntu-spark which contains ubuntu with the spark engine installed.
```sh
docker build -t tlew/ubuntu-spark:latest .
```

Run this to create a container based on the image ubuntu-spark.
```sh
docker run -it -d --name ubuntu-spark tlew/ubuntu-spark 
```

Alternatively, run this to create the container and also submit the specified python script to the spark engine.
```sh
docker run -it -d --name ubuntu-spark tlew/ubuntu-spark spark-submit  createll.py --workingdir /home/sparkjobs
```

Start the container that was just created from the built image.
```sh
docker start ubuntu-spark 
```


##### Docker Container Run 

There are 2 ways to submit a python program to the spark engine in the ubuntu-spark container:
From outside of the container:
```sh
docker exec -it ubuntu-spark spark-submit /home/sparkjobs/createll.py
```

From inside of the container:
To run a bash shell on the newly created container ubuntu-spark.
```sh
docker exec -it ubuntu-spark bash
```

Go to the project folder "/home/sparkjobs/".
```sh
$ cd /home/sparkjobs/
```

Submit the python script to the spark engine directly.
```sh
$ spark-submit createll.py
```


##### Docker Container Output 

To view the output file "linkedlistpageViews.csv",
shell into the Docker container ubuntu-spark.
```sh
docker exec -it ubuntu-spark bash
```

The output file is:
```sh
/home/sparkjobs/linkedlistpageViews.csv
```


### Spark 
An ubuntu:latest based [Spark](http://spark.apache.org "Spark") container. Use it in a standalone cluster with the accompanying docker-compose.yml, or as a base for more complex recipes.

### License 
MIT



