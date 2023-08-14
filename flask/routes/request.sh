#!/bin/bash

# https://linuxize.com/post/curl-rest-api/
# curl [options] [URL...]

# options:

#     -X, --request - The HTTP method to be used.
#     -i, --include - Include the response headers.
#     -d, --data - The data to be sent.
#     -H, --header - Additional header to be sent.

curl -X GET localhost:5555/langs

# curl -X POST -H "Content-Type:application/json" \
# -d {"name":"test", "creator":"test", "year":9999, "users":0} \
# localhost:5555/langs
