import './App.css';

function Header(props){
  
  return <header>
    <h1><a href="/">{ props.title }</a></h1>
  </header>
}

function Nav(props){
  const lis = [
    <li><a href="/read/1">html</a></li>,
    <li><a href="/read/2">css</a></li>,
    <li><a href="/read/3">Javascript</a></li>
  ]

  for (let i =0; i<props.topics.length;i++){
    let t = props.topics[i];
    lis.push(<li key={t.id}><a href={'/read/'+t.id}>{t.title}</a></li>)
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
     <Header title="REACT"></Header>
     <Nav topics={topics}></Nav>
    </div>
  );
}

export default App;
