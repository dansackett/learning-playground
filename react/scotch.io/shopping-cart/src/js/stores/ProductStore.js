var AppDispatcher       = require('../dispatcher/AppDispatcher');
var EventEmitter        = require('events').EventEmitter;
var FluxCartConstants   = require('../constants/FluxCartConstants');
var _                   = require('underscore');

var _product = {},
    _selected = null;

// Method to load product data from API
function loadProductData(data) {
    _product = data[0];
    _selected = data[0].variants[0];
}

// Set selected variant
function setSelected(index) {
    _selected = _product.variants[index];
}

// Build our store to handle data and emit events
var ProductStore = _.extend({}, EventEmitter.prototype, {
    // Return product data
    getProduct: function() {
        return _product;
    },

    // Return selected product
    getSelected: function() {
        return _selected;
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
        case FluxCartConstants.RECEIVE_DATA:
            loadProductData(action.data);
            break;

        case FluxCartConstants.SELECT_PRODUCT:
            setSelected(action.data);
            break;

        default:
            return true;
    }

    ProductStore.emitChange();
    return true;
});

module.exports = ProductStore;
