// Minimal mock API using Node's http (no deps)
import http from 'http';
import fs from 'fs';
import path from 'path';

const mockDir = process.env.MOCK_DIR || 'data/samples';

function readJSON(name){
  return JSON.parse(fs.readFileSync(path.join(mockDir, name + '.json'), 'utf8'));
}

const server = http.createServer((req, res) => {
  const url = new URL(req.url, 'http://localhost');
  const parts = url.pathname.split('/').filter(Boolean);

  res.setHeader('Content-Type','application/json');

  if(parts[0] === 'api' && parts[1] === 'flowscore'){
    res.end(JSON.stringify(readJSON(`flowscore_${parts[2].toUpperCase()}`)));
  } else if(parts[0] === 'api' && parts[1] === 'whales'){
    res.end(JSON.stringify(readJSON(`whales_${parts[2].toUpperCase()}`)));
  } else if(parts[0] === 'api' && parts[1] === 'liquidity'){
    res.end(JSON.stringify(readJSON(`liquidity_${parts[2].toUpperCase()}`)));
  } else if(parts[0] === 'api' && parts[1] === 'social'){
    res.end(JSON.stringify(readJSON(`social_${parts[2].toUpperCase()}`)));
  } else {
    res.statusCode = 404;
    res.end(JSON.stringify({error:'not found'}));
  }
});

const PORT = process.env.PORT || 5812;
server.listen(PORT, () => console.log('Mock API on', PORT));
