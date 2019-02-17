// importing node path module
const path = require('path');

module.exports = {
    entry: [
        './src/index.js',
        './src/styles/styles.scss',
    ],
    output: {
        filename: 'main.js',
        path: path.resolve(__dirname, './dist')
    },
    module: {
        rules: [{
            test: /\.tsx?$/,
            use: 'ts-loader',
            exclude: /node_modules/
          },
          {
            test: /\.scss$/,
            use: [
                "style-loader", // creates style nodes from JS strings
                "css-loader", // translates CSS into CommonJS
                "sass-loader" // compiles Sass to CSS, using Node Sass by default
            ]
        }]
    },
    resolve: {
        extensions: [ '.tsx', '.ts', '.js' ]
    }
};