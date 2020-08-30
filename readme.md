# sshcounter

Count the number of time a person logs into a machine


## Installation Service

Run the create_db.py to create the sqllite DB used in the app

```bash
python create_db.py
```
Run the server by running run_app.cmd or run_app.sh depending on the shell

Prerequisites
1. Root access on the machines on which the client is to be installed
2. python3.6 

Working
We are adding script to the bashrc files that will run whenever a user login to machine
the script send a post request to out server which then updates the counter.
the count can be seen on the landing page 

Local testing
if you want to check by sending a post request run sshcounter_client
docker
Please let me know if docker image is needed for this project

