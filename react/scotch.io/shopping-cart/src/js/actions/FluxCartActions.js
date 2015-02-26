var AppDispatcher       = require('../dispatcher/AppDispatcher');
var FluxCartConstants   = require('../constants/FluxCartConstants');

var FluxCartActions = {
    // Receive Initial Product Data
    receiveProduct: function(data) {
        AppDispatcher.handleAction({
            actionType: FluxCartConstants.RECEIVE_DATA,
            data: data
        })
    },

    // Set curretly selected product variation
    selectProduct: function(index) {
        AppDispatcher.handleAction({
            actionType: FluxCartConstants.SELECT_PRODUCT,
            data: index
        })
    },

    // Add item to cart
    addToCart: function(sku, update) {
        AppDispatcher.handleAction({
            actionType: FluxCartConstants.CART_ADD,
            sku: sku,
            update: update
        })
    },

    // Remove item from cart
    removeFromCart: function(sku) {
        AppDispatcher.handleAction({
            actionType: FluxCartConstants.CART_REMOVE,
            sku: sku
        })
    },

    // Update cart visible
    updateCartVisible: function(cartVisible) {
        AppDispatcher.handleAction({
            actionType: FluxCartConstants.CART_VISIBLE,
            cartVisible: cartVisible
        })
    }
};

module.exports = FluxCartActions;
