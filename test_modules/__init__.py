from sekoia_automation.module import Module
from test_modules.models import TestModuleConfiguration


class TestModule(Module):
    configuration: TestModuleConfiguration
