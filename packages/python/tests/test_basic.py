from octoflow import OctoFlow

def test_flowscore_range():
    client = OctoFlow(mock_dir='../../data/samples')
    fs = client.flow_score('SOL')
    assert 0 <= fs.score <= 100
