import { useEffect, useState } from "react";

function App() {
  const [accounts, setAccounts] = useState([]);

  useEffect(() => {
    fetch("https://mastodon.social/api/v2/search?q=eshanlucifer%40gmail.com&type=accounts")
      .then((res) => res.json())
      .then((data) => {
        setAccounts(data.accounts);
      })
      .catch((err) => console.error(err));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h2>Mastodon Accounts</h2>

      {accounts.length === 0 ? (
        <p>Loading...</p>
      ) : (
        accounts.map((acc) => (
          <div key={acc.id} style={{ border: "1px solid #ccc", margin: "10px", padding: "10px" }}>
            <img src={acc.avatar} alt="" width="50" />
            <h3>{acc.display_name}</h3>
            <p>@{acc.username}</p>
          </div>
        ))
      )}
    </div>
  );
}

export default App;