import SearchBar from "./SearchBar";
import Button from '@mui/material/Button';

function Transfer() {
    return(
      <div className="transfer">
        <SearchBar />
        <h1>Welcome to OPEN Playlist Migrator</h1>
        <Button variant="contained">Start Transfer</Button>
      </div>
    )

}

export default Transfer;
