#!/usr/bin/env python3
import argparse, json, os
from octoflow import OctoFlow

def main():
  p = argparse.ArgumentParser(description='OctoFlow CLI')
  p.add_argument('cmd', choices=['flowscore','whales','liquidity','social'])
  p.add_argument('symbol', help='Token symbol, e.g., SOL')
  p.add_argument('--mock', default='data/samples')
  args = p.parse_args()

  client = OctoFlow(mock_dir=args.mock)
  fn = getattr(client, args.cmd)
  out = fn(args.symbol)
  if hasattr(out, '__dict__'): out = out.__dict__
  print(json.dumps(out, indent=2, default=lambda o: o.__dict__))

if __name__ == '__main__':
  main()
