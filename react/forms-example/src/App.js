import NewWordForm from "./components/NewWordForm.js";
import Search from "./components/Search.js";
import WordList from "./components/WordList.js";
import { useState } from "react";
function App() {
    const wordData = [
        {
            text: "brotherhood",
            origin: "germanic",
        },
        {
            text: "fraternity",
            origin: "latin",
        },
        {
            text: "husband",
            origin: "norse",
        },
        {
            text: "chocolate",
            origin: "aztec",
        },
    ];
    const [words, setWords] = useState(wordData);
    const [searchText, setSearchText] = useState("");
    const [formData, setFormData] = useState({
        text: "",
        origin: "",
    });
    function updateSearchText(event) {
        setSearchText(event.target.value);
    }
    function updateFormData(event) {
        setFormData({...formData, 
            [event.target.id]:event.target.value})
    }
    function addNewWord() {
        setWords([...words, formData]);
    }
    const filteredWords = words.filter(word =>{
        if(searchText === ''){
            return true
        }else{
            return word.text.toLowerCase()
                .includes(searchText.toLowerCase())
        }
    })
    return (
        <>
            <h1>More Cool Words</h1>
            <Search updateSearchText={updateSearchText} />
            <WordList words={filteredWords} />
            <NewWordForm
                addNewWord={addNewWord}
                updateFormData={updateFormData}
            />
        </>
    );
}

export default App;
