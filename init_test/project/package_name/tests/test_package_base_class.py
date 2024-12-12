from ...package_name import DerivedInternalBaseClass, DerivedExternalBaseClass

def test_derived_internal_class():
    print("Hello")
    assert DerivedInternalBaseClass().get_number() == 5
    
def test_derived_external_package_class():
    print("Hello")
    assert DerivedExternalBaseClass().get_number() == 5
    