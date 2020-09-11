#!/bin/sh
port='3000'
url='http://localhost'
curl --request POST $url':'$port'/updatecounter/'$HOSTNAME