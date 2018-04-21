import React from 'react';
import { connect } from 'react-redux'
import {QUESTION_ENDPOINT, selectQuestion, fetchQuestions} from './actions'


function Question({question, onClick}) {
    return (
        <li id={question.id}
            className="question"
            onClick={ onClick } >
            {question.content}
        </li>
    );
}


const mapStateToProps = state => {
    return {
        questions: state.entities.questions
    }
}


const mapDispatchToProps = dispatch => {
    return {
        onQuestionClick: id => {
            dispatch(selectQuestion(id))
        },
        getQuestions: () => { dispatch(fetchQuestions()) }
    }
}


class Questions extends React.Component  {
    componentDidMount() {
        this.props.getQuestions();
    }

    render() {
        console.log(this.props);
        return (
            <ul className="questions-list">
                {this.props.questions.map((question) => (
                    <Question key={question.id} question={question} onClick={() => this.props.onQuestionClick(question.id)} />
                ))}
            </ul>
        );
    }
}


Questions = connect(
    mapStateToProps,
    mapDispatchToProps
)(Questions)

export default Questions
