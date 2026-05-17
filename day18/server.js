const express = require('express');
const app = express();
app.use(express.json());

const tasks = [];

app.get('/health', (req, res) => {
    res.json({ status: 'healthy', runtime: 'Node.js' });
});

app.get('/tasks', (req, res) => {
    res.json(tasks);
});

app.post('/tasks', (req, res) => {
    const task = req.body.task;
    tasks.push({ id: tasks.length + 1, task });
    res.json({ message: `Task '${task}' added!` });
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});
