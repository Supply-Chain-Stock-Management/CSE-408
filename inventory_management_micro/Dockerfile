# Use an official Node.js runtime as the base image
FROM node:21

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port on which your Node.js application will run
EXPOSE 3000
# does not actually publish the specified ports. It serves as a documentation feature to indicate which ports are intended to be published


# Start the Node.js application
CMD ["npm", "start"]
