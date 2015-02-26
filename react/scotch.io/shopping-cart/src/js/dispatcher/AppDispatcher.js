var Dispatcher      = require('flux').Dispatcher
var AppDispatcher   = new Dispatcher();

// Convenience method for handling requests
AppDispatcher.handleAction = function(action) {
    this.dispatch({
        source: 'VIEW_ACTION',
        action: action
    });
}

module.exports = AppDispatcher;
