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
reads the dependencies and devDependencies sections of the ```package.json``` file and installs the specified packages, along with their dependencies, into a ```node_modules``` directory in the project.
<br>
Can make sure by running ```npm install``` after adding dependecy then check ```node_modules```