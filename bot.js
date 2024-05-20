const express = require('express')
const router = express.Router()

const {getUserInput} = require('./controller/Bot')

router.post('/getresult',getUserInput)
module.exports = router;