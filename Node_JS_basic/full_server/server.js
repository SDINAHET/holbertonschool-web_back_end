import express from 'express';
import router from './routes/index.js';

const app = express();
const port = 1245;

// Use the router for all routes
app.use('/', router);

// Start the server
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});

export default app;
