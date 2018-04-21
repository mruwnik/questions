import 'babel-polyfill';
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import Questions from './Questions';
import ItemGrid from './Answers';
import questionsApp from './reducers';
import './index.css';


const store = createStore(
    questionsApp,
    applyMiddleware(thunk)
);


ReactDOM.render(
    <Provider store={store}>
        <div><Questions /><ItemGrid /></div>
    </Provider> ,
  document.getElementById('root')
);
