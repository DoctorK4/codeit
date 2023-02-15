import './App.css';



function Header(props){
  
  return <header>
    <h1><a href="/" onClick={function(event){
      event.preventDefault();
      props.onChangeMode();
    }}>{ props.title }</a></h1>
  </header>
}
function Nav(props){
  const lis = [];

  for (let i =0; i<props.topics.length;i++){
    let t = props.topics[i];
    lis.push(<li key={t.id}>
      <a id={t.id} href={'/read/'+t.id} onClick={event=>{
        event.preventDefault();
        props.onChangeMode(event.target.id);
      }}>{t.title}</a>
      </li>)
  }

  return <nav>
    <ol>
      {lis}
    </ol>
  </nav>
}

function App() {
  const topics = [
    {id : 1, title : 'html', body : 'html is...'},
    {id : 2, title : 'CSS', body : 'CSS is...'},
    {id : 3, title : 'Javascript', body : 'Javascript is...'}
  ]
  return (
    <div>
     <Header title="REACT" onChangeMode={function(){
      alert('Header');
     }}></Header>
     <Nav topics={topics} onChangeMode={(id)=>{
      alert(id);
     }}></Nav>
    </div>
  );
}

export default App;
