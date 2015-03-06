# ReactJS

React is a UI Library developed at Facebook to allow you to build interactive,
stateful, reusable UI components. It allows both client-side rendering and
server-side rendering making it an attractive and flexible solution.

## Virtual DOM

ReactJS introduces the concept of Virtual DOM which refers to a smarter way to
update DOM nodes based on state. The core idea is that React selectively
rerenders subtress of nodes based on state changes. This means that React
tries to do as few DOM manipulations as possible to render components giving
applications speed and efficiency.

To do this, React runs a "diffing" algorithm which first finds out what has
changed. Based on this diff, it updates the DOM for only the changed node. As
an example, updating text in an input element would only affect that element.
This is thanks in part to React's "fake DOM".

Due to this "fake DOM", we can render it on the server-side and pass it back
to the client to load.

## JSX

React introduces a language called JSX which allows you to write and render
HTML elements directly in the JavaScript files. The idea is that these HTML
elements are actually XML tags that can be transformed into JS functions by
the JSX Transformer. For this reason, common attributes such as `class` and
`for` are replaced with `className` and `htmlFor` respectively.

A basic JSX component can be seen here:


```
React.render(
    <h1 className="component1">I'm a componenet!</h1>,
    document.getElementById('myDiv')
);
```

Of course, we can also write the transformed JSX directly:

```
React.render(
    React.DOM.h1({className: "component1"}, 'Hello, world!'),
    document.getElementById('myDiv')
);
```

In the end, we create the DOM with these JS functions that React supplies and
get our result.

## Components

While it's cool to render already-defined HTML elements as components, it's
also awesome to create your own components. Doing this is much like
AngularJS's directives. We can create custom components by:

```
var MyComponent = React.createClass({
    render: function(){
        return (
            <h1 className="component1">I'm a component!</h1>
        );
    }
});
```

Now when we render the component we can do so like this:

```
React.render(
    <MyComponent/>,
    document.getElementById('myDiv')
);
```

Nice and easy and allows us to build smart modules which is something that
React preaches.

## Props

React components can take in `props` which are attributes available in the
component's render method. In the last example, we can pass props to
`MyComponent` like so:

```
React.render(
    <MyComponent thing="ball"/>,
    document.getElementById('myDiv')
);
```

We can use the `name` property in our render method like so:

```
var MyComponent = React.createClass({
    render: function(){
        return (
            <h1 className="component1">I'm a {this.props.thing}!</h1>
        );
    }
});
```

## Component Methods and State

While `render` is the required method in our component, there are quite a few
others that can give us added functionality.

- `componentWillMount`: Invoked on client and server before rendering.
- `componentDidMount`: Invoked on client only after rendering.
- `shouldComponentUpdate`: Boolean return if it should update.
- `componentWillUnmount`: Invoked prior to unmounting.
- `getInitialState`: Returns the initial value for `state`.
- `getDefaultProps`: Set fallback props if not set.
- `mixins`: Array of objects used to extend the components functionality.

Each of these gives us a level of control at each stage of the component
lifecyle.

Another large concept in React, and probably the most important, is the `state`.
Every component has a state object which sits alongside the props object. We
can set the state implicitly by calling `setState()`. This trigger UI updates
and is what drives React's dynamic interface.

## Events

We can define events much like we do in any HTML and JS application from the
past. They are simply properties on components and trigger methods. For
instance, we can set a property like `onClick={this.handleEvent}` and clicking
the component will now call the `handleEvent()` method on the component.

## Standard Flow

In ReactJS, the data flow is unidirectional. With a framework like AngularJS
we have two-way binding where applications update on both sides. In React we
don't have this. Instead, it travels one way making it best to create a common
parent component when working with multiple components. This will manage the
state and distribute it through the use of passed props.

We call the `setState()` method to refresh the components and then our
children components will receive the updates from that parent.

With that in mind, building React apps requires some thought about how the
data will be hanlded before jumping in like Angular.

# Flux

Flux itself is another piece of the puzzle for working with React
applications. I actually isn't a framework or a library but rather an
architecthure that complements unidirectional flow.

The basic parts of Flux are a `Dispatcher` and NodeJS's `EventEmitter`. A list
of the components with Flux are:

- Actions: Helpers that pass data to dispatcher.
- Dispatcher: Pub/Sub manager broadcasting payloads to callbacks.
- Stores: Containers for state / logic with callbacks on a Dispatcher.
- Controller Views: React Components that grab state from stores and pass it
  down via props to child components.

The flow can be described as:

```
API <---
|      |
--> ACTION -> DISPATCHER -> STORE -> VIEW -->
       ^                                    |
       |                                    |
       --------------------------------------
```

We start from the API. An action occurs and then we are passed to the
dispatcher. The dispatcher sends us into the to manipulate the data and the
store triggers the view. The view then sets the actions again and we wait for
the API to begin again.

## Dispatcher

The Dispatcher is the central hub that keeps things together. It get actions
and sends those actions and relevant data to any registered callbacks. It acts
as a type of pub/sub system in the sense that it broadcasts events to all
callbacks. With it you have the ability to set the order of callbacks, wait
for updates, or proceed as planned.

In an application there is one single Dispatcher and it does the talking. A
sample basic dispatcher can be seen below:

```
var Dispatcher = require('flux').Dispatcher;
var AppDispatcher = new Dispatcher();

AppDispatcher.handleViewAction = function(action) {
    this.dispatch({
        source: 'VIEW_ACTION',
        action: action
    });
}

module.exports = AppDispatcher;
```

Our sample here is called `AppDispatcher` and has a `handleViewAction` method
attached to it. Actions enter this dispatcher and any store registered to it
will have their callbacks sent the action and the action payload. This passing
then is acted on in a store which will subsequently update the state.

Dispatchers give us the ability to set order in our callbacks. It's done by:

```
MyStore.dispatcherIndex = AppDispatcher.register(function(payload) {

});

...

case 'MY_CASE':
    AppDispatcher.waitFor([
        MyStore.dispatcherIndex
    ], function() {
    ...
    });
    break;
```

This flow will allow us to wait for a callback to fire before firing this one
in our store. Pretty neat.

## Stores

Stores are the brain and they handle the state of the application. This means
handling:

- Data
- Data retrieval methods
- Dispatcher callbacks

In most cases we use NodeJS's `EventEmitter` to both listen and broadcast
events across the app. This is what allows us to update things on changes and
rerender our components.

## Actions

Actions are called inside views (or anywhere) to send actions to the
dispatcher. Actions are themselves the payloads that are distributed.

## Controller Views

Controller views are essentially just the React Components themselves. They
listen for events and retrieve state. They pass this data to child components
through props making the whole ecosystem works.
