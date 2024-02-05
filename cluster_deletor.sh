#!/bin/bash

cluster_name=$1
if [ -z "$cluster_name" ]; then
    echo "No cluster name provided."
    exit 1
fi


eksctl delete cluster --name $cluster_name --region ap-south-1

echo "view the AWS CloudFormation stack https://console.aws.amazon.com/cloudformation"