function Word({ text, origin }) {
    console.assert(typeof(text) === "string");
    return (
        <li>
            {text}: word origin: {origin}
        </li>
    );
}
export default Word;
