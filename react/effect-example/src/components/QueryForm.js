

function QueryForm({updateQuery, displayQuery}){

    return(
        <form onSubmit={displayQuery}>
            <input type="text" id="query" onChange={updateQuery} placeholder="Enter a spell name..."></input>
            <input type="submit" value="Submit" ></input>
        </form>
    )
}

export default QueryForm