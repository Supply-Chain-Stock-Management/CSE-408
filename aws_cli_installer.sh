#!/bin/bash


# from https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

echo "after ./aws/install"
echo "So, AWS CLI installed successfully"
echo "Now checking version of AWS CLI"
/usr/local/bin/aws --version
