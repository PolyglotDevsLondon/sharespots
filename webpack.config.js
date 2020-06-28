// importing node path module
const path = require("path");

const BrowserSyncPlugin = require("browser-sync-webpack-plugin");
const CopyPlugin = require('copy-webpack-plugin');

module.exports = {
    entry: ["./src/index.js", "./src/styles/styles.scss"],
    output: {
        filename: "main.js",
        path: path.resolve(__dirname, "./dist")
    },
    module: {
        rules: [
            {
                test: /\.tsx?$/,
                use: "ts-loader",
                exclude: /node_modules/
            },
            {
                test: /\.scss$/,
                use: [
                    "style-loader", // creates style nodes from JS strings
                    "css-loader", // translates CSS into CommonJS
                    "sass-loader" // compiles Sass to CSS, using Node Sass by default
                ]
            }
        ]
    },
    plugins: [
        new BrowserSyncPlugin(
            {
                host: "localhost",
                port: 3000,
                proxy: "http://0.0.0.0:8000/"
            },
            {
                reload: true
            }
        ),
        new CopyPlugin({
            patterns: [
                {   
                    from: './src/img/',
                    to: './img',
                },
            ],    
        })
    ],
    resolve: {
        extensions: [".tsx", ".ts", ".js"]
    }
};
