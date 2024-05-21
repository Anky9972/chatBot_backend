const express = require('express');
const app = express();
const cors = require('cors');
const bodyParser = require('body-parser');

app.use(express.json());
app.use(cors({
  origin: '*', 
  methods: '*', 
  allowedHeaders: ['Content-Type', 'Authorization'], 
  credentials: true, 
}));
app.use(bodyParser.json());

const PORT = process.env.PORT || 4000;

const botroute = require('./bot');
app.use('/api/v1', botroute);

// Home route
app.get('/', (req, res) => {
    res.set('Access-Control-Allow-Origin', '*');
  res.send('This is HOME page');
});

// Start server
app.listen(PORT, () => {
  console.log(`App started successfully at ${PORT}`);
});
