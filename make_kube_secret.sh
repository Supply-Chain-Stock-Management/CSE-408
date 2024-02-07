#!/bin/bash

# another modification
# Usage function
usage() {
    echo "Usage: $0 <secret_name1> <pem_file1> [<secret_name2> <pem_file2>] ..."
    echo "Example: $0 tls-cert-secret certificate1.pem"
    exit 1
}

# Check if arguments are provided
if [ $# -eq 0 ]; then
    echo "No arguments provided."
    usage
    exit 1
elif [ $(($# % 2)) -ne 0 ]; then
    echo "Invalid number of arguments. Must provide pairs of secret names and PEM files."
    usage
    exit 1
fi

# Loop through each pair of arguments and create kubectl secret
args=("$@")  # Store all arguments in an array
for ((i=0; i<${#args[@]}; i+=2)); do
    secret_name="${args[i]}"
    pem_file="${args[i+1]}"
    kubectl create secret generic "$secret_name" --from-file="$pem_file"
    if [ $? -ne 0 ]; then
        echo "Failed to create secret: $secret_name from file $pem_file"
    else
        echo "Secret created: $secret_name from file $pem_file"
    fi
done

# now all the secretssssss
echo "All secrets:"
kubectl get secrets
