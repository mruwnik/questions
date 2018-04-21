import React from 'react';
import { connect } from 'react-redux'
import {selectItem, showAnswer} from './actions'


function Item({item, onClick}) {
    return (
        <div className={item.class} id={item.id} onClick={ onClick } >
            {item.title}
        </div>
    );
}


function ItemGrid({question, items, loading, onItemClick}) {
    let loadingClass = loading ? "" : "loading";
    return (
        <div className="items-container {loadingClass}">
            {items.map((item) => (
                <Item key={item.id}
                      item={item}
                      onClick={() => onItemClick(question, item.id, item.class)}
                />
            ))}
        </div>
    );
}


const mapStateToProps = state => {
    return {
        question: state.question,
        items: state.items || [],
        loading: state.loading
    };
}


const mapDispatchToProps = dispatch => {
    return {
        onItemClick: (question, id, type) => {
            dispatch(selectItem(question, id, type))
        }
    }
}

ItemGrid = connect(
    mapStateToProps,
    mapDispatchToProps
)(ItemGrid)


export default ItemGrid
