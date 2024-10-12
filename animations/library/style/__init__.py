"""
    Common style elements suggested to be consistent throughout all animatations.
"""

# We want to be able to access submodules after only importing the package, i.e:
#   import style
#   style.color.Whatever
# One way of doing this would be, for each module, to go through and write in this
# file:
#   import color
# Which would have the affect of adding the module `color` to `__all__`.
# OR, instead of doing that manually, we can do it automatically:
# (kudos to https://stackoverflow.com/a/3365846/10717280)
# import pkgutil

# __all__ = []
# for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
#     __all__.append(module_name)
#     _module = loader.find_module(module_name).load_module(module_name)
#     globals()[module_name] = _module
