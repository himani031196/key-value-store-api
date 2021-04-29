<h1>This is an implementation of Key-Value HTTP API </h1>

<h3>Requirements:<h3>
1. Python >=3.7</br>
2. Flask >=1.1 </br>
3. Sqlite3 </br>

<h3>API functionality:</h3>
1. <b>/set</b> : sets a key against a value in the database. This need a json object as input specifying the key value pair {"key":"abc-1", "value":"verified"}</br>
2. <b>/get?key=$key </b>: gets the value of the given key</br>
3. <b>/search</b> : returns all the keys with the specified condition. This API supports two conditions</br>
        1. <b>/search?prefix=$keyprefix</b> : the prefix condition will search for all the keys that contain the specified prefix</br>
        2. <b>/search?suffix=$keysuffix</b> : the suffix condition will search for all the keys that contain the specified suffix


<h3>Run the Application:</h3>
<b>python ./src/app.py </b></br>
This command will start the service on your local system on port 5000. you can test the api at http://localhost:5000

<h3>Run the Unit Test cases</h3>
<b>python ./src/keyvalueapi_test.py -t </b>

<h3>Docker Installation :</h3>
The Dockerfile contains the code to host this application within a docker container. 
This hosts the api on port 5000 inside the container and exposes it on port 5001 inside the container. 
Steps:
1. <b>docker build -t key-value-app-image:latest Dockerfile</b></br>
2. <b>docker run -p 5001:5000 key-value-app-image:latest</b>

<h3>For Kubernetes installation </h3>
For hosting the deployment, service and ingress objects inside the kubernetes cluster :
<b>
cd Kubernetes </br>
kubectl apply -f deployment.yaml</br>
kubectl apply -f service.yaml</br>
kubectl apply -f ingress.yaml</b>