#!/bin/bash
# curl -X POST -d "username=user2&email=sarifulsourov321@gmail.com"  http://localhost:8000/authentication/register/
# curl -X POST -H "Content-Type: application/json" -d '{"username": "your_username", "password": "your_password"}' http://localhost:8000/authentication/login/
# curl -X POST http://localhost:8000/authentication/logout/
# curl -X POST -H "Content-Type: application/json" -d '{"email": "user@example.com"}' http://localhost:8000/authentication/password_reset/

curl -X POST \
  -d "subject=Test_Email2" \
  -d "message=This_is_a_test_email_message2" \
  -d "recipient_email=sarifulsourov321@gmail.com" \
  http://localhost:8000/email/send/
