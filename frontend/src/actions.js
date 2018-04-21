import fetch from 'cross-fetch';

export const SELECT_QUESTION = 'select question';
export const SELECT_CATEGORY = 'select category';
export const SHOW_ANSWER = 'select answer';
export const HIDE_ANSWER = 'hide answer';

export const REQUEST_ITEMS = 'REQUEST_POSTS';
export const RECIEVE_ITEMS = 'RECIEVE_POSTS';
export const RECIEVE_QUESTIONS = 'RECIEVE_QUESTIONS';

export const QUESTION_ENDPOINT = `http://localhost:8000/question/`;
const CATEGORY_ENDING = 'category/';


function items_url(question, parent) {
    let url = QUESTION_ENDPOINT + question + '/';
    if (parent) {
        url = url + CATEGORY_ENDING + parent;
    }
    return url;
}


export function selectQuestion(question) {
    return fetchQuestion(question);
}


export function showAnswer(answer) {
    return { type: SHOW_ANSWER, answer};
}


export function hideAnswer(answer) {
    return { type: HIDE_ANSWER, answer};
}


export function selectCategory(question, catId) {
    return fetchItems(question, catId);
}


export function selectItem(question, item, type) {
    if (type === 'category') {
        return selectCategory(question, item);
    } else {
        return showAnswer(item);
    }
}


function requestItems(question, parent) {
    return {
        type: REQUEST_ITEMS,
        question, parent
    };
}


function receiveItems(question, parent, json) {
    return {
        type: RECIEVE_ITEMS,
        categories: json.categories,
        answers: json.answers,
        question, parent
    };
}


function recieveQuestions(json) {
    return {
        type: RECIEVE_QUESTIONS,
        questions: json.questions
    };
}


function fetchItems(question, parent) {
    return (dispatch, getState) => {
        dispatch(requestItems(question, parent));
        return fetch(items_url(question, parent))
            .then(response => response.json())
            .then(json => dispatch(receiveItems(question, parent, json)));
    };
}


function fetchQuestion(question) {
    return (dispatch, getState) => {
        dispatch({type: SELECT_QUESTION, question: question});
        return fetch(items_url(question))
            .then(response => response.json())
            .then(json => dispatch(receiveItems(question, null, json)));
    };
}


export function fetchQuestions() {
    return (dispatch, getState) => {
        return fetch(QUESTION_ENDPOINT + 'all')
            .then(response => response.json())
            .then(json => dispatch(recieveQuestions(json)));
    };
}
