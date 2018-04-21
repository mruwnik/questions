import { combineReducers } from 'redux';
import {
    SELECT_CATEGORY, SELECT_QUESTION, SHOW_ANSWER,
    HIDE_ANSWER, RECIEVE_ITEMS, REQUEST_ITEMS, RECIEVE_QUESTIONS
} from './actions';


function answer(state, action) {
    switch (action.type) {
    case SHOW_ANSWER:
        return action.answer;
    default:
        return null;
    }
}


function items(state = null, action) {
    switch (action.type) {
    case SELECT_CATEGORY:
        return action.items;
    case RECIEVE_ITEMS:
        let categories = action.categories.map((cat) => ({id: cat.id, title: cat.title, class: 'category'}));
        let answers = action.answers.map((answer) => ({id: answer.id, title: answer.title, class: 'answer'}));
        return [...categories, ...answers];
    default:
        return state;
    }
}


function question(state = null, action) {
    switch (action.type) {
    case SELECT_QUESTION:
        return action.question;
    default:
        return state;
    }
}


function path(state = [], action) {
    switch (action.type) {
    case SELECT_QUESTION:
        return [];
    case SELECT_CATEGORY:
        return state.concat([action.item]);
    default:
        return state;
    }
}


function loading(state = false, action) {
    switch (action.type) {
    case REQUEST_ITEMS:
        return true;
    case RECIEVE_ITEMS:
        return false;
    default:
        return state;
    }
}


function entities(state = {questions: [], categories: {}, answers: {}}, action) {
    let questions = state.questions;
    let categories = state.categories;
    let answers = state.answers;
    switch (action.type) {
    case RECIEVE_QUESTIONS:
        questions = action.questions;
    }
    return {
        questions: questions,
        categories: categories,
        answers: answers
    };
}


const questionsApp = combineReducers({
    entities,
    loading,
    question,
    items,
    answer,
    path
});

export default questionsApp;
