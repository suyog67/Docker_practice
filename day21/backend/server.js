const express = require('express');
const { Pool } = require('pg');
const cors = require('cors');

const app = express();
app.use(express.json());
app.use(cors());

const pool = new Pool({
    host: process.env.DB_HOST,
    database: process.env.DB_NAME,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    port: 5432
});

app.get('/health', (req, res) => {
    res.json({ status: 'healthy', service: 'Node API' });
});

app.get('/api/tasks', async (req, res) => {
    const client = await pool.connect();
    await client.query(`
        CREATE TABLE IF NOT EXISTS tasks 
        (id SERIAL PRIMARY KEY, task TEXT)
    `);
    const result = await client.query('SELECT * FROM tasks');
    client.release();
    res.json(result.rows);
});

app.post('/api/tasks', async (req, res) => {
    const { task } = req.body;
    const client = await pool.connect();
    await client.query(
        'INSERT INTO tasks (task) VALUES ($1)', [task]
    );
    client.release();
    res.json({ message: `Task '${task}' added!` });
});

app.listen(5000, () => console.log('API running on port 5000'));
