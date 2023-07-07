function Spell({ spellInfo }) {
    if (spellInfo.error !== undefined) {
        return (
            <>
                <ul>
                    <li>Error: {spellInfo.error}</li>
                </ul>
            </>
        );
    } else {
        return (
            <>
                <ul>
                    <li>
                        <strong>Name: </strong>
                        {spellInfo.name}
                    </li>
                    <li>
                        <strong>Range: </strong>
                        {spellInfo.range}
                    </li>
                    <li>
                        <strong>Description: </strong>
                        {spellInfo.desc}
                    </li>
                </ul>
            </>
        );
    }
}
export default Spell;
