import gc

print(gc.isenabled())  # by default gc is enabled
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())

