import Letter from './components/Letter.js'
function App() {

  const letter = {
    symbol:{
      upperCase:'A',
      lowerCase:'a'
    },
    isVowel:true,
    alphabets: ['latin', 'cyrillic','greek'],
    usage: {
      latin: 'Athens',
      cyrillic:'Афины',
      greek:'Αθήνα'
    }
  }

  return (
    <div>
      <Letter letter={letter} />
    </div>
  );
}

export default App;
