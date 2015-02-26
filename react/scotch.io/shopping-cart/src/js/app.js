window.React        = require('react');
var ProductData     = require('./ProductData');
var CartAPI         = require('./utils/CartApi');
var FluxCartApp     = require('./components/FluxCartApp.react');

// Load product data into localstorage
ProductData.init();

// Load Mock API Call
CartAPI.getProductData();

// Render FluxCartApp controller view
React.render(
    <FluxCartApp />,
    document.getElementById('main')
);
