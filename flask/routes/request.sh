#!/bin/bash

# https://linuxize.com/post/curl-rest-api/
# curl [options] [URL...]

# options:

#     -X, --request - The HTTP method to be used.
#     -i, --include - Include the response headers.
#     -d, --data - The data to be sent.
#     -H, --header - Additional header to be sent.
method=$1

if [ $method == "get" ]
then
    curl -X GET localhost:5555/langs
fi

if [ $method == 'post' ]
then
    curl -X POST -H "Content-Type:application/json" \
    -d '{"name":"ML", "creator":"Milner", "year":1973, "users":0}' \
    localhost:5555/langs
fi

if [ $method == 'delete' ]
then
    curl -X DELETE localhost:5555/langs/7
fi
