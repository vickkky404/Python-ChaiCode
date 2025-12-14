"""Adapter Pattern - Convert the interface of a class into another interface clients expect."""

from abc import ABC, abstractmethod


class Target(ABC):
    """Target interface that client expects."""
    
    @abstractmethod
    def get_data(self) -> str:
        pass


class LegacySystem:
    """Legacy system with incompatible interface."""
    
    def fetch_information(self) -> str:
        return "Data from legacy system"


class LegacyAdapter(Target):
    """Adapter that makes legacy system compatible."""
    
    def __init__(self, legacy_system: LegacySystem):
        self.legacy_system = legacy_system
    
    def get_data(self) -> str:
        return self.legacy_system.fetch_information()


class NewSystem:
    """New system with expected interface."""
    
    def __init__(self, target: Target):
        self.target = target
    
    def request(self) -> str:
        return f"Processed: {self.target.get_data()}"


class ThirdPartyLibrary:
    """Third party library with different interface."""
    
    def retrieve_content(self) -> str:
        return "Content from third party"


class LibraryAdapter(Target):
    """Adapter for third party library."""
    
    def __init__(self, library: ThirdPartyLibrary):
        self.library = library
    
    def get_data(self) -> str:
        return self.library.retrieve_content()


# Demonstration
if __name__ == "__main__":
    # Using legacy system through adapter
    legacy = LegacySystem()
    legacy_adapter = LegacyAdapter(legacy)
    new_system = NewSystem(legacy_adapter)
    print("Legacy System: ", new_system.request())
    
    # Using third party library through adapter
    library = ThirdPartyLibrary()
    lib_adapter = LibraryAdapter(library)
    new_system = NewSystem(lib_adapter)
    print("Third Party: ", new_system.request())
