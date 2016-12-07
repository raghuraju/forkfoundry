var path = require('path');
var webpack = require('webpack');
var validate = require('webpack-validator');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = validate({
	context: __dirname,

	entry: './web/src/js/app',

	output: {
		path: path.resolve('./web/dist/bundles'),
		filename: '[name]-[hash].js',
	},

	plugins: [
		new BundleTracker({filename: './webpack-stats.json'}),
		new webpack.ProvidePlugin({
			$: 'jquery',
			jQuery: 'jquery',
			'window.jQuery': 'jquery',
		}),
	],

	module: {
		loaders: [
			{
				test: /\.jsx?$/,
				exclude: [/node_modules/],
				loader: 'babel-loader',
				query: {
					presets: [
						'latest',
						'react',
					],
				}
			},
		],
	},

	resolve: {
		extensions: ['', '.js', '.jsx'],
	},
})