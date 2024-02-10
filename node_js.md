# Error
## Error: Cannot find module 'express'
express not installed or not in *dependency* of ```package.json```<br>
So can do:
```sh
npm install express --save
```
```--save flag``` is used to ensure that the package is added to the dependencies section
<br><br>
Then ```express``` will be on ```node_modules``` directory
### npm install
<br>
Can make sure by running ```npm install``` after adding dependecy then check ```node_modules```

# modifying package.json
## dotenv in dependency
as i take env variables as arguments<br>
so  ~~"dotenv": "^16.4.1",~~
```sh
"dependencies": {
    "express": "^4.18.2",
    "pg": "^8.11.3"
  }
```
## when docker (not locally)
"start": "node index.js ~~PORT=$PORT MONGODB_URI=$MONGODB_URI CREDENTIALS=$CREDENTIALS~~",
