import React, { PropTypes } from'react';
import ReactDOM from 'react-dom';
import { Router, Route, hashHistory } from 'react-router';

// components
import App from './app';

const ForkFoundry = props => (
	<Router history={hashHistory}>
		<Route path="/" component={App} />
	</Router>
);

ReactDOM.render(<ForkFoundry />, document.getElementById('app'));
