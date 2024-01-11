# API Doc
## request body
data sent by the client to API
## response body
data API sends to the client.
## HTTP Method
**PUT** replaces that password [PUT only creates one if there is none]
## Response Code
200 (password update is successful)
401 (current password is incorrect)
404 (user not found)
201 Created (if the user is successfully created)
400 Bad Request (if the request is malformed or missing required fields)
409 Conflict (if the username or email is already taken)
204 status code is used when the server successfully processes the request, but there is no content to return to the client.
## Response Code AND Method
help of chatgpt
| HTTP request method 	| Purpose 	| 200 OK 	| 201 Created 	| 204 No Content 	| 400 Bad Request 	| 401 Unauthorized 	| 403 Forbidden 	| 404 Not Found 	|
|---	|---	|---	|---	|---	|---	|---	|---	|---	|
| GET 	| Retrieve data from the server 	| Successful retrieval of the resource 	|  	|  	|  	|  	|  	| The requested resource could not be found 	|
| POST 	| Submit data to be processed to a specified resource 	|  	| Resource successfully create 	|  	| The request is malformed or invalid 	| Authentication is required 	| The client does not have permission 	| The requested resource could not be found 	|
| PUT 	| Update a resource or create a new resource if it doesn't exist 	| Successful update of the resource 	| Resource successfully created 	| The request was successful, but there is no content to return 	| The request is malformed or invalid 	| Authentication is required 	| The client does not have permission 	| The requested resource could not be found 	|
| DELETE 	| Delete a specified resource 	| Successful deletion of the resource 	|  	| The request was successful, but there is no content to return 	| The request is malformed or invalid 	| Authentication is required 	| The client does not have permission 	| The requested resource could not be found 	|
| PATCH 	| Apply partial modifications to a resource 	| Successful application of partial modifications 	|  	| The request was successful, but there is no content to return 	| The request is malformed or invalid 	| Authentication is required 	| The client does not have permission 	| The requested resource could not be found 	|
| OPTIONS 	| Retrieve information about the communication options available for a resource 	| Successful retrieval of options information 	|  	| The request was successful, but there is no content to return 	|  	|  	|  	|  	|