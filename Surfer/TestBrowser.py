class TestBrowser:
    def __getattr__(self, *args, **kwargs):
        print(f"property called with args=|{args}| and kwargs=|{kwargs}|")
        return self
    
    def __setattr__(self, *args, **kwargs):
        print(f"property set with args=|{args}| and kwargs=|{kwargs}|")
        return self
    
    def __call__(self, *args, **kwargs):
        print(f"'{args[0]}' method used with args=|{args}| and kwargs=|{kwargs}|")
