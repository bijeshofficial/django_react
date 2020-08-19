module.exports = {
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /nodu_modules/,
                use: {
                    loader : "babel-loader",
                }
            }
        ]
    }
}