import React, { PropTypes } from'react';
import ReactDOM from 'react-dom';

const Hello = props => (
	<div>
		App says: {props.message}
	</div>
);

Hello.PropTypes = {
	message: PropTypes.string.isRequired,
};

ReactDOM.render(<Hello message="hello, world!"/>, document.getElementById('app'));
