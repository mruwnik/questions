import React from 'react';
import { connect } from 'react-redux'
import {QUESTION_ENDPOINT, selectQuestion, fetchQuestions} from './actions'


function Question({question, selected, onClick}) {
    let className = "question " + (selected ? 'selected' : '');

    return (
        <li id={question.id}
            className={className}
            onClick={ onClick } >
            {question.content}
        </li>
    );
}


const mapStateToProps = state => {
    return {
        questions: state.entities.questions,
        chosen: state.question
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
        return (
           <div className="sidebar">
                <ul className="questions-list">
                    {this.props.questions.map((question) => (
                        <Question key={question.id}
                                  question={question}
                                  selected={question.id == this.props.chosen}
                                  onClick={() => this.props.onQuestionClick(question.id)}
                        />
                    ))}
                </ul>
           </div>
        );
    }
}


Questions = connect(
    mapStateToProps,
    mapDispatchToProps
)(Questions)

export default Questions
