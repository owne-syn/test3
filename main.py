from test_modules import TestModule

from test_modules.trigger_new_entries import NewEntriesTrigger
from test_modules.action_request import Request


if __name__ == "__main__":
    module = TestModule()
    module.register(NewEntriesTrigger, "NewEntriesTrigger")
    module.register(Request, "Request")
    module.run()
