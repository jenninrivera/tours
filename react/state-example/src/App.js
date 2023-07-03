import { useState } from "react";

let countWithoutState = 0; //doesn't work as expected!
function App() {
    //example from https://react.dev/reference/react/useState
    const [count, setCount] = useState(0);
    const [countList, setCountList] = useState([])
    function handleStateClick() {
        setCount(count + 1);
        setCountList([...countList, count + 1])
    }
    function handleNonStateClick() {
        countWithoutState++;
    }

    return (
        <>
            <button onClick={handleStateClick}>
                Count using state button pressed: {count} times
            </button>
            <br></br>
            <button onClick={handleNonStateClick}>
                Count without using state button pressed: {countWithoutState} times
            </button>
            <br></br>
            Past counts:
            <ul>
                {countList.map(num => <li key={num}>{num}</li>)}
            </ul>
        </>
    );
}

export default App;
