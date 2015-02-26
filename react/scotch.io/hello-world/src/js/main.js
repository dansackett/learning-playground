var HelloWorld  = require('./components/app');
var React       = require('react');

React.render(
    <HelloWorld name="dan" />,
    document.getElementById('main'));
