from octoflow import OctoFlow

client = OctoFlow(mock_dir="../../data/samples")

print("FLOW SCORE (SOL):")
print(client.flow_score("SOL"))

print("\nTOP WHALES:")
for ev in client.whales("SOL")[:5]:
    print(ev.wallet, ev.side, ev.amount, "SOL")
