def test_imports():
    from src import config, train
    assert hasattr(config, "DATA_DIR")
    assert callable(train.train)
