
function NewWordForm({addNewWord, updateFormData}){
    function handleSubmit(event){
        event.preventDefault()
        addNewWord()
        event.target.reset()
    }
    return (
        <form onSubmit={handleSubmit}>
            <input onChange={updateFormData} type="text" id="text" placeholder="Word text"/><br></br>
            <input onChange={updateFormData} type="text" id="origin" placeholder="Word root" /><br></br>
            <input onChange={updateFormData} type="submit" value="Submit"></input>
        </form>
    )

}
export default NewWordForm