

function Search({updateSearchText}){
    console.assert(typeof(updateSearchText) == 'function', 
        'callback function was not passed to Search component')
    return (
        <input type="text" placeholder="Search words..." onChange={updateSearchText}></input>        
    )
}
export default Search