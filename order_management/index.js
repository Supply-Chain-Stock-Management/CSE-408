const express = require('express');
const { Pool } = require('pg');
require('dotenv').config();
const app = express();
const PORT = process.env.PORT || 3000;

// PostgreSQL configuration
const pool = new Pool({
    user: process.env.DB_USER,
    host: process.env.DB_HOST,
    database: process.env.DB_NAME,
    password: process.env.DB_PASSWORD,
    port: process.env.DB_PORT,
  });

// Test route for database connection
app.get('/', async (req, res) => {
    try {
        const client = await pool.connect();
        const result = await client.query('SELECT $1::text as message', ['Hello, PostgreSQL!']);
        const message = result.rows[0].message;
        res.send(`Database connection successful. Message: ${message}`);
        console.log(`Database connection successful. Message: ${message}`);
        client.release();
    } catch (error) {
        console.error('Error connecting to the database', error);
        res.status(500).send('Internal Server Error');
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
