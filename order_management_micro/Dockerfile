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

# Copy the environment variable file to the working directory
# COPY config.env .env

# Expose the port on which your Node.js application will run
EXPOSE 3030

# Start the Node.js application
CMD ["npm", "start"]
