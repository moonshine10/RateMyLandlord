var path = require('path');
var webpack = require('webpack');

module.exports = {
    context: __dirname,

    entry: {
        // Main React components go here
        Index: './react/Index',
        vendors: ['react']
    },

    output: {
        path: path.resolve('./webapp/webapp/static/bundles/local'),
        filename: 'bundle.js'
    },

    externals: [
        // add all vendor libs
    ],

    plugins: [
        // all common plugins go here
        new webpack.optimize.CommonsChunkPlugin('vendors', 'vendors.js')
    ],

    module: {
        loaders: [] // add all common loaders here
    },

    resolve: {
        modulesDirectories: ['node_modules', 'bower_components'],
        extensions: ['', '.js', '.jsx']
    }
};
