const { spawn } = require('child_process');

exports.getUserInput = async (req, res) => {
    try {
        const { input } = req.body;
        console.log('input of user', input);

        const childPythonWithModel = spawn('python', ['model.py', input]);
        let result = '';

        childPythonWithModel.stdout.on('data', async (data) => {
            // console.log('Received data:', data.toString());
            result = await data; 
            console.log("result",data.toString())
        });

        childPythonWithModel.on('close', (code) => {
            
            res.json({
                status: true,
                message: result
            });
        });

    } catch (e) {
        console.log('failed to get user input:', e);
        res.status(500).json({ status: false, message: 'Failed to get user input' });
    }
};
