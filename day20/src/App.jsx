function App() {
  return (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      height: '100vh',
      fontFamily: 'Arial, sans-serif',
      background: '#f0f2f5'
    }}>
      <h1 style={{color: '#2c3e50'}}>
        🐳 Hello from React in Docker!
      </h1>
      <p style={{color: '#7f8c8d'}}>
        Built with multi-stage Docker build
      </p>
    </div>
  );
}

export default App;
