

function Spell({spellInfo}){
    return(
        <>
        <ul>
            <li><strong>Name: </strong>{spellInfo.name}</li>
            <li><strong>Range: </strong>{spellInfo.range}</li>
            <li><strong>Description: </strong>{spellInfo.desc}</li>
            {spellInfo?.error ? <li>Error: {spellInfo.error}</li> : <></>}
        </ul>
        </>
    )
}
export default Spell