class FakeMongoClient:
    def __init__(self, *args, **kwargs) -> None:
        self.closed = False

    def __getitem__(self, name: any) -> dict:
        return {"test_collection": "fake_collection"}
    
    def close(self) -> None:
        self.closed = True