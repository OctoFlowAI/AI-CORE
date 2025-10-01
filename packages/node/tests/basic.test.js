import { OctoFlow } from '../src/index.js';
const client = new OctoFlow({ mockDir: '../../data/samples' });
const fs = client.flowScore('SOL');
if(!(fs.score >=0 && fs.score <= 100)) throw new Error('FlowScore out of range');
console.log('OK');
