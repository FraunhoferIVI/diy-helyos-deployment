#!/bin/bash

# Generate RSA private key in PEM format
openssl genrsa -out ./etc_helyos/.ssl_keys/helyos_private.key 1024

# Generate the corresponding public key in PEM format
openssl rsa -in ./etc_helyos/.ssl_keys/helyos_private.key -pubout -out ./etc_helyos/.ssl_keys/helyos_public.key

# Restrict permissions on the private key
chmod 666 ./etc_helyos/.ssl_keys/helyos_private.key


