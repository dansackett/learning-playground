var AppDispatcher       = require('../dispatcher/AppDispatcher');
var EventEmitter        = require('events').EventEmitter;
var FluxCartConstants   = require('../constants/FluxCartConstants');
var _                   = require('underscore');

var _products = {},
    _cartVisible = false;

// Method to add product to the cart
function add(sku, update) {
    update.quantity = sku in _products ? _products[sku].quantity + 1 : 1;
    _products[sku] = _.extend({}, _products[sku], update);
}

// Method to set the cart to visible
function setCartVisible(cartVisible) {
    _cartVisible = cartVisible;
}

// Method to remove an item from a cart
function removeItem(sku) {
    delete _products[sku];
}

// Build our store to handle data and emit events
var CartStore = _.extend({}, EventEmitter.prototype, {
    // Return cart items
    getCartItems: function() {
        return _products;
    },

    // Return number of cart items
    getCartCount: function() {
        return Object.keys(_products).length;
    },

    // Return cart totla
    getCartTotal: function() {
        var total = 0;

        for (product in _products) {
            if (_products.hasOwnProperty(product)) {
                total += _products[product].price * _products[product].quantity;
            }
        }

        return total.toFixed(2);
    },

    // Return cart visibility
    getCartVisible: function() {
        return _cartVisible;
    },

    // Emit change event
    emitChange: function() {
        this.emit('change');
    },

    // Add change listener
    addChangeListener: function(callback) {
        this.on('change', callback);
    },

    // Remove change listener
    removeChangeListener: function(callback) {
        this.removeListener('change', callback);
    }
});

// Register store payloads with actions
AppDispatcher.register(function(payload) {
    var action = payload.action;
    var text;

    switch(action.actionType) {
        case FluxCartConstants.CART_ADD:
            add(action.sku, action.update);
            break;

        case FluxCartConstants.CART_REMOVE:
            removeItem(action.sku);
            break;

        case FluxCartConstants.CART_VISIBLE:
            setCartVisible(action.cartVisible);
            break;

        default:
            return true;
    }

    CartStore.emitChange();
    return true;
});

module.exports = CartStore;
