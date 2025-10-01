import fs from 'fs';
import path from 'path';

export class OctoFlow {
  constructor({ apiKey='DEMO', mockDir='../../data/samples' } = {}) {
    this.apiKey = apiKey;
    this.mockDir = mockDir;
  }
  _load(name) {
    const p = path.resolve(new URL(import.meta.url).pathname, this.mockDir, `${name}.json`);
    return JSON.parse(fs.readFileSync(p, 'utf8'));
  }
  flowScore(symbol) { return this._load(`flowscore_${symbol.toUpperCase()}`); }
  whales(symbol) { return this._load(`whales_${symbol.toUpperCase()}`); }
  liquidity(symbol) { return this._load(`liquidity_${symbol.toUpperCase()}`); }
  social(symbol) { return this._load(`social_${symbol.toUpperCase()}`); }
}
