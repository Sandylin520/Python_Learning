"""
Unlike other languages in Python, there's no main function that you call somewhere at the top of
your script that gets run automatically.

Instead, what happens is just implicitly all the code at this indentation level zero gets run when
you call the script file

python has a build in variable  __name__
"""
#one.py
def func():
    print("FUNC() IN ONE.PY")

print("TOP LEVEL IN ONE.PY")

if __name__== '__main__':
    print('ONE.PY is being run directly')
else:
    print('ONE.PY has been imported!')