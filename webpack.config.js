// importing node path module
const path = require('path');

module.exports = {
    entry: './frontend/src/scripts/index.js',
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, './frontend/dist')
    }
};