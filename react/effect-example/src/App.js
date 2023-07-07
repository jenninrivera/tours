import { useState, useEffect } from "react";
import QueryForm from "./components/QueryForm.js";
import Spell from "./components/Spell.js";
function App() {
    const [spellList, setSpellList] = useState([]);
    const [spellInfo, setSpellInfo] = useState({});
    const [query, setQuery] = useState("");

    useEffect(() => {
        fetch("https://www.dnd5eapi.co/api/spells/")
            .then((res) => res.json())
            .then((data) => setSpellList(data.results));
    }, []);
    function displayQuery(event) {
        event.preventDefault();
        console.log(spellList);
        const spell = spellList.find((spell) => {
            return spell.name.toLowerCase().includes(query.toLowerCase());
        });
        if (spell === undefined) {
            setSpellInfo({ error: `${query}: spell not found` });
        } else {
            fetch(`https://www.dnd5eapi.co${spell.url}`)
                .then((res) => res.json())
                .then((data) => setSpellInfo(data));
        }
        event.target.reset();
    }
    return (
        <>
            <h1>Spell Search</h1>
            <QueryForm
                updateQuery={(event) => setQuery(event.target.value)}
                displayQuery={displayQuery}
            />
            <Spell spellInfo={spellInfo} />
        </>
    );
}

export default App;
