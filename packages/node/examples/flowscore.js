import { OctoFlow } from '../src/index.js';
const client = new OctoFlow({ mockDir: '../../data/samples' });
console.log('FlowScore SOL:', client.flowScore('SOL'));
console.log('Top whales:', client.whales('SOL').events.slice(0,3));
