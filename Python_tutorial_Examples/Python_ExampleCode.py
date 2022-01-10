Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print('Hello, World!")
      
SyntaxError: unterminated string literal (detected at line 1)
print("Hello, World!")
      
Hello, World!
4
      
4
+ 5
      
5
4
      
4
num1 = 4
      
num1
      
4
type(num1)
      
<class 'int'>
num2 = 5
      
num2
      
5
num1
      
4
num1 = 4
      
num1
      
4
num2
      
5
num2
      
5
type(num2)
      
<class 'int'>
num3 = num1 = num2
      
num3
      
5
num3 = num1 + num2
      
num3
      
10
num1 = 4
      
num1
      
4
num3 = num1 + num2
      
num3
      
9
num1 = 1
      
num2 = 2
      



print(num1 + num2)
      
3
num1 = 1.2
      
num2 = 2.1
      
print(num1 + num2)
      
3.3
myString = "hello world"
      
myString
      
'hello world'
len (myString)
      
11
myString[0]
      
'h'
myString[2]
      
'l'
fName = "Shannon"
      
lName ="Hodges"
      
print (fName + lName)
      
ShannonHodges
print (fName + " " + lName)
      
Shannon Hodges
print ("Hello {} {}, welcome to python!".format(fName,lName))
      
Hello Shannon Hodges, welcome to python!
x = 3
      
y = 7
      
myMath = "x + y"
      
myMath
      
'x + y'
print(myMath)
      
x + y















myMath
      
'x + y'


a = "Hello"
      
print(a)
      
Hello
myMath = "7 + 3"
      
print(myMath)
      
7 + 3
#This is a comment.
      
print("Hello, World!"

b = "Hello, World!"
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print"Hello, World!"
      
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
b = "Hello, World!"
      
print(b[2:5])
      
llo
len (myMath)
      
5
len (b)
      
13
txt = "    banana    "
      
x = txt.strip()
      
print("of all fruits", x, "is my favorite")
      
of all fruits banana is my favorite
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
      
print(a)
      
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
txt = "Hello my friends"
      
x = txt.upper()
      
print(x)
      
HELLO MY FRIENDS
txt = "The best things in life are free!"
      
print("free" in txt)
      
True
txt = "The best things in life are free!"
      
if "free" in txt:
      print("Yes, 'free' is present.")

     
Yes, 'free' is present.
txt = "The best things in life are free!"
      
print("expensive" not in txt)
      

print("expensive" not in txt)
      
True
txt = "The best things in life are free!"
      
if "expensive" not in txt:
      print("No, 'expensive' is NOT present.")

      
No, 'expensive' is NOT present.
x = "Python is "
      
y = "awesome"
      
z = x+ y
      
print(z)
      
Python is awesome
txt = "We are the so-called "Vikings" from the north."
      
SyntaxError: invalid syntax
txt = "We are the so-called \"Vikings"\ from the north."
      
SyntaxError: unexpected character after line continuation character
print(txt)
      
The best things in life are free!
txt = "We are the so-called "Vikings" from the north."
      
SyntaxError: invalid syntax
txt = "We are the so-called \"Vikings"\ from the north."
      
SyntaxError: unexpected character after line continuation character
txt = "We are the so-called \"Vikings\" from the north."
print(txt) 



txt = "We are the so-called \"Vikings\" from the north."
      
print(txt)
      
We are the so-called "Vikings" from the north.
num1 = 1
      
num2 = 2
      
print(num1 + num2)
      
3
num1 = 1.2
      
num2 = 2.1
      
print(num1 + num2)
      
3.3
num1 = "one"
      
print(num1 + num2)
      
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    print(num1 + num2)
TypeError: can only concatenate str (not "float") to str
num1 = "1"
      
print(num1 + num2)
      
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    print(num1 + num2)
TypeError: can only concatenate str (not "float") to str
print(int(num1) + num2)
      
3.1
x = 5
      
y = 3
      
print(x=y)
      
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    print(x=y)
TypeError: 'x' is an invalid keyword argument for print()
print(x+y)
      
8
x = 5
      
x%=3
      
print(x)
      
2
x=5
      
y = 3
      
print(x >= y)
      
True
print(10 + 5)
      
15
x = ["apple", "banana"]
      
y = ["apple", "banana"]
      
z = x
      
print(x is z)
      
True
print(x is y)
      
False
print(x == y)
      
True
x = ["apple", "banana"]
      
print("banana" in x)
      
True
x = ["apple", "banana"]
      
x = ["apple", "banana"]
      
x = ["apple", "banana"]
      
x = ["apple", "banana"]
      


animal = ( 'zebra', 'alligator', 'giraffe', 'goat', 'ox' )
      
listofAnimals = list(animal)
      
print(listofAnimals)
      
['zebra', 'alligator', 'giraffe', 'goat', 'ox']
listofAnimals = list(animal)
      
listofAnimals.append ("honey badger")
      
print(listofAnimals)
      
['zebra', 'alligator', 'giraffe', 'goat', 'ox', 'honey badger']
myString = myString = "Hello! I am pleased to meet you"
      
myString = "Hello! I am pleased to meet you"
      
newString = list(myString)
      
print(newString)
      
['H', 'e', 'l', 'l', 'o', '!', ' ', 'I', ' ', 'a', 'm', ' ', 'p', 'l', 'e', 'a', 's', 'e', 'd', ' ', 't', 'o', ' ', 'm', 'e', 'e', 't', ' ', 'y', 'o', 'u']
newString = myString.split(' ')
      
print(newString)
      
['Hello!', 'I', 'am', 'pleased', 'to', 'meet', 'you']
myList = [2,3,4]
      
len(myList)
      
3
for i in myList:
      print(i)

      
2
3
4
myList [2]
      
4
mylist[0]
      
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    mylist[0]
NameError: name 'mylist' is not defined. Did you mean: 'myList'?
myList[0]
      
2
myList.append(5)
      
for i in myList:
      print(i)

      
2
3
4
5
len(myList)
      
4
print(myList)
      
[2, 3, 4, 5]

Mylist = [a,b,c,d,e]
      
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    Mylist = [a,b,c,d,e]
NameError: name 'c' is not defined
letterList = [a,b,c,d,e]
      
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    letterList = [a,b,c,d,e]
NameError: name 'c' is not defined
letterList = [a,b,c,d,e]
      
Traceback (most recent call last):
  File "<pyshell#176>", line 1, in <module>
    letterList = [a,b,c,d,e]
NameError: name 'c' is not defined
shannonList = [a,b,c,d,e]
      
Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    shannonList = [a,b,c,d,e]
NameError: name 'c' is not defined
letterList =['a', 'b', 'c', 'd']
      
for x in letterList:
      print(x)

      
a
b
c
d
letterList.append('b')
      
letterList.append('e')
      
print(letterList)
      
['a', 'b', 'c', 'd', 'b', 'e']
print(letterList)
      
['a', 'b', 'c', 'd', 'b', 'e']
fruits = ['apple', 'banana', 'cherry', 'orange']
      
x = fruits.copy()
      

print(x)
      
['apple', 'banana', 'cherry', 'orange']
list1 = ["a", "b" , "c"]
      
list2 = [1, 2, 3]
      
list3 = list1 + list2
      
print(list3)
      
['a', 'b', 'c', 1, 2, 3]
fruits = ['apple', 'banana', 'cherry']
      
fruits.reverse()
      
print(fruits)
      
['cherry', 'banana', 'apple']
mytuple = ("apple", "banana", "cherry")
      
print(thistuple)
      
Traceback (most recent call last):
  File "<pyshell#198>", line 1, in <module>
    print(thistuple)
NameError: name 'thistuple' is not defined
print(mytuple)
      
('apple', 'banana', 'cherry')
for x in thistuple:
      print(x)

      
Traceback (most recent call last):
  File "<pyshell#202>", line 1, in <module>
    for x in thistuple:
NameError: name 'thistuple' is not defined
for x inmytuple:
      
SyntaxError: invalid syntax
for x in mytuple:
      print(x)

      
apple
banana
cherry
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
      
x = thistuple.count(5)
      
print(x)
      
2
mySet = ["baseball", "basketball", "football"]
      
mySet.remove("basketball")
      
thisset = {"apple", "banana", "cherry"}
      
thisset.remove("banana")
      
print(thisset)
      
{'cherry', 'apple'}
x = {"apple", "banana", "cherry"}
      
y = {"google", "microsoft", "apple"}
      
z = x.difference(y)
      
print(z)
      
{'cherry', 'banana'}
x = {"apple", "banana", "cherry"}
      
y = {"google", "microsoft", "apple"}
      
z = y.difference(x)
      
print(z)
      
{'google', 'microsoft'}
myDictionary = {'index1': 1, 'index2': 2, 'index3': 355}
      
myDictionary['index2']
      
2
dict_users = {'em_1234': {'fname': 'Bob', 'lname': 'Smith', 'phone': '123-456-7890'}, 'em_1235': {'fname': 'Mary', 'lname': 'Jones', 'phone': '152-364-5764'} }
      
print(dict_users['em_1235'])
      
{'fname': 'Mary', 'lname': 'Jones', 'phone': '152-364-5764'}
print(dict_users['em_1235']['phone'])
      
152-364-5764
print('User: {} {}\nPhone: {}'.format(dict_users['em_1235']['fname'],dict_users['em_1235']['lname'],dict_users['em_1235']['phone']))
      
User: Mary Jones
Phone: 152-364-5764
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
      
x = thisdict.get("model")
      
print(x)
      
Mustang
thisdict["year"] = 2018
      
print(thisdict)
      
{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}
thisdict["color"] ="red"
      
print(thisdcit)
      
Traceback (most recent call last):
  File "<pyshell#235>", line 1, in <module>
    print(thisdcit)
NameError: name 'thisdcit' is not defined. Did you mean: 'thisdict'?
print(thisdict)
      
{'brand': 'Ford', 'model': 'Mustang', 'year': 2018, 'color': 'red'}
myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
        },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
        },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
        }
    }
      
print(myfamily)
      
{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
x = ('key1', 'key2', 'key3')
      
y = 0
      
thisdict = dict.fromkeys(x, y)
      
print(thisdict)
      
{'key1': 0, 'key2': 0, 'key3': 0}
color = 'Red'
      
color = ['Red', 'Blue', 'Green', 'Orange', 'Pink', 'Yellow', 'Black', 'White']
      
"Hello World!"
      
'Hello World!'
hello world
      
SyntaxError: invalid syntax
"Hello World!"
      
'Hello World!'
name = "Bob"
      
print(name)
      
Bob
name = 'Python'
      
print(name)
      
Python
print(type(name))
      
<class 'str'>
x = 5
print(type(x))
      
SyntaxError: multiple statements found while compiling a single statement
x = 5
      
print(type(x))
      
<class 'int'>
a = 6
      
b = 7
      
a!=b
      
True
a = 3
      
b = 6
      
b > a
      
True
a = 2
      
b = 2
      
a >= b
      
True
a = 1
      
b = 3
      
a < b
      
True
a > b
      
False
a = 12
      
b = 40
      
a<= b
      
True
num1 = 5
      
num2 = 5
      
num3 =6
      
num4 = 6
      
num1 == num2 AND num3 == num4
      
SyntaxError: invalid syntax
num3 = 6
      
num1 == num2 AND num3 == num4
      
SyntaxError: invalid syntax
num1 == num2 and num3 == num4
      
True
num1 != num3 and num2 < num4
      
True
num1 = 1
      
num2 = 5
      
num1 < num2 or num1 == num2
      
True
not num1 == num2
      
True
answer = True
      
type(answer)
      
<class 'bool'>
type(answer) = False
      
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
answer = False
      
type(answer)
      
<class 'bool'>
print(10 < 9)
      
False
print(10 == 9)
      
False
print(10 > 9)
      
True
a = 200
      
b = 33
      
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

  
b is not greater than a
if b > a:
    print("True")
    else:
        
SyntaxError: invalid syntax
if b > a:
    print("True")

    
else:
    
SyntaxError: invalid syntax
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
SyntaxError: multiple statements found while compiling a single statement
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
SyntaxError: multiple statements found while compiling a single statement
a 33
SyntaxError: invalid syntax
a = 33
b = 33
if b > a:
    print("b is greater than a")
    elif a == b:
        
SyntaxError: invalid syntax
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
SyntaxError: multiple statements found while compiling a single statement



integer PayRate = 35.00
SyntaxError: invalid syntax
integer payRate = 35.00
SyntaxError: invalid syntax
integer PayRate = 35.00

integer HoursWorked = 10

integer Paycheck
SyntaxError: invalid syntax
PayRate = 35.00
HoursWorked = 10
Paycheck = HoursWorked x PayRate
SyntaxError: invalid syntax
Paycheck = HoursWorked * PayRate

Paycheck
350.0
help()

Welcome to Python 3.10's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the internet at https://docs.python.org/3.10/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> help> modules
No Python documentation found for 'help> modules'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> modules

Please wait a moment while I gather a list of all available modules...

__future__          argparse            help                sched
__main__            array               help_about          scrolledlist
_abc                ast                 history             search
_aix_support        asynchat            hmac                searchbase
_ast                asyncio             html                searchengine
_asyncio            asyncore            http                secrets
_bisect             atexit              hyperparser         select
_blake2             audioop             idle                selectors
_bootsubprocess     autocomplete        idle_test           setuptools
_bz2                autocomplete_w      idlelib             shelve
_codecs             autoexpand          imaplib             shlex
_codecs_cn          base64              imghdr              shutil
_codecs_hk          bdb                 imp                 sidebar
_codecs_iso2022     binascii            importlib           signal
_codecs_jp          binhex              inspect             site
_codecs_kr          bisect              io                  smtpd
_codecs_tw          browser             iomenu              smtplib
_collections        builtins            ipaddress           sndhdr
_collections_abc    bz2                 itertools           socket
_compat_pickle      cProfile            json                socketserver
_compression        calendar            keyword             sqlite3
_contextvars        calltip             lib2to3             squeezer
_csv                calltip_w           linecache           sre_compile
_ctypes             cgi                 locale              sre_constants
_ctypes_test        cgitb               logging             sre_parse
_datetime           chunk               lzma                ssl
_decimal            cmath               macosx              stackviewer
_distutils_hack     cmd                 mailbox             stat
_elementtree        code                mailcap             statistics
_functools          codecontext         mainmenu            statusbar
_hashlib            codecs              marshal             string
_heapq              codeop              math                stringprep
_imp                collections         mimetypes           struct
_io                 colorizer           mmap                subprocess
_json               colorsys            modulefinder        sunau
_locale             compileall          msilib              symtable
_lsprof             concurrent          msvcrt              sys
_lzma               config              multicall           sysconfig
_markupbase         config_key          multiprocessing     tabnanny
_md5                configdialog        netrc               tarfile
_msi                configparser        nntplib             telnetlib
_multibytecodec     contextlib          nt                  tempfile
_multiprocessing    contextvars         ntpath              test
_opcode             copy                nturl2path          textview
_operator           copyreg             numbers             textwrap
_osx_support        crypt               opcode              this
_overlapped         csv                 operator            threading
_pickle             ctypes              optparse            time
_py_abc             curses              os                  timeit
_pydecimal          dataclasses         outwin              tkinter
_pyio               datetime            parenmatch          token
_queue              dbm                 pathbrowser         tokenize
_random             debugger            pathlib             tooltip
_sha1               debugger_r          pdb                 trace
_sha256             debugobj            percolator          traceback
_sha3               debugobj_r          pickle              tracemalloc
_sha512             decimal             pickletools         tree
_signal             delegator           pip                 tty
_sitebuiltins       difflib             pipes               turtle
_socket             dis                 pkg_resources       turtledemo
_sqlite3            distutils           pkgutil             types
_sre                doctest             platform            typing
_ssl                dynoption           plistlib            undo
_stat               editor              poplib              unicodedata
_statistics         email               posixpath           unittest
_string             encodings           pprint              urllib
_strptime           ensurepip           profile             uu
_struct             enum                pstats              uuid
_symtable           errno               pty                 venv
_testbuffer         faulthandler        py_compile          warnings
_testcapi           filecmp             pyclbr              wave
_testconsole        fileinput           pydoc               weakref
_testimportmultiple filelist            pydoc_data          webbrowser
_testinternalcapi   fnmatch             pyexpat             window
_testmultiphase     format              pyparse             winreg
_thread             fractions           pyshell             winsound
_threading_local    ftplib              query               wsgiref
_tkinter            functools           queue               xdrlib
_tracemalloc        gc                  quopri              xml
_uuid               genericpath         random              xmlrpc
_warnings           getopt              re                  xxsubtype
_weakref            getpass             redirector          zipapp
_weakrefset         gettext             replace             zipfile
_winapi             glob                reprlib             zipimport
_xxsubinterpreters  graphlib            rlcompleter         zlib
_zoneinfo           grep                rpc                 zoneinfo
abc                 gzip                run                 zoomheight
aifc                hashlib             runpy               zzdummy
antigravity         heapq               runscript           

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.





import math

math.floor(3.5)
3



if __name__ == "__main__":









def getNumbers(num1, num2):
    results = num1 * num2
    return results





































if __name__ == "__main__":
    
SyntaxError: expected an indented block after 'if' statement on line 1
pass

= RESTART: C:/Users/shodg/OneDrive/Documents/GitHub/Python_Projects/mymodule.py =
Traceback (most recent call last):
  File "C:/Users/shodg/OneDrive/Documents/GitHub/Python_Projects/mymodule.py", line 1, in <module>
    import mymodule
  File "C:\Users/shodg/OneDrive/Documents/GitHub/Python_Projects\mymodule.py", line 2, in <module>
    mymodule.greeting("Jonathan")
AttributeError: partially initialized module 'mymodule' has no attribute 'greeting' (most likely due to a circular import)









import sys
help()

Welcome to Python 3.10's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the internet at https://docs.python.org/3.10/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> modules

Please wait a moment while I gather a list of all available modules...

Tutorial_Shell      argparse            help_about          sched
__future__          array               history             scrolledlist
__main__            ast                 hmac                search
_abc                asynchat            html                searchbase
_aix_support        asyncio             http                searchengine
_ast                asyncore            hyperparser         secrets
_asyncio            atexit              idle                select
_bisect             audioop             idle_test           selectors
_blake2             autocomplete        idlelib             setuptools
_bootsubprocess     autocomplete_w      imaplib             shelve
_bz2                autoexpand          imghdr              shlex
_codecs             base64              imp                 shutil
_codecs_cn          bdb                 importlib           sidebar
_codecs_hk          binascii            inspect             signal
_codecs_iso2022     binhex              io                  site
_codecs_jp          bisect              iomenu              smtpd
_codecs_kr          browser             ipaddress           smtplib
_codecs_tw          builtins            itertools           sndhdr
_collections        bz2                 json                socket
_collections_abc    cProfile            keyword             socketserver
_compat_pickle      calendar            lib2to3             sqlite3
_compression        calltip             linecache           squeezer
_contextvars        calltip_w           locale              sre_compile
_csv                cgi                 logging             sre_constants
_ctypes             cgitb               lzma                sre_parse
_ctypes_test        chunk               macosx              ssl
_datetime           cmath               mailbox             stackviewer
_decimal            cmd                 mailcap             stat
_distutils_hack     code                mainmenu            statistics
_elementtree        codecontext         marshal             statusbar
_functools          codecs              math                string
_hashlib            codeop              mimetypes           stringprep
_heapq              collections         mmap                struct
_imp                colorizer           modulefinder        subprocess
_io                 colorsys            msilib              sunau
_json               compileall          msvcrt              symtable
_locale             concurrent          multicall           sys
_lsprof             config              multiprocessing     sysconfig
_lzma               config_key          mymodule            tabnanny
_markupbase         configdialog        netrc               tarfile
_md5                configparser        nntplib             telnetlib
_msi                contextlib          nt                  tempfile
_multibytecodec     contextvars         ntpath              test
_multiprocessing    copy                nturl2path          textview
_opcode             copyreg             numbers             textwrap
_operator           crypt               opcode              this
_osx_support        csv                 operator            threading
_overlapped         ctypes              optparse            time
_pickle             curses              os                  timeit
_py_abc             dataclasses         outwin              tkinter
_pydecimal          datetime            parenmatch          token
_pyio               dbm                 pathbrowser         tokenize
_queue              debugger            pathlib             tooltip
_random             debugger_r          pdb                 trace
_sha1               debugobj            percolator          traceback
_sha256             debugobj_r          pickle              tracemalloc
_sha3               decimal             pickletools         tree
_sha512             delegator           pip                 tty
_signal             difflib             pipes               turtle
_sitebuiltins       dis                 pkg_resources       turtledemo
_socket             distutils           pkgutil             types
_sqlite3            doctest             platform            typing
_sre                dynoption           plistlib            undo
_ssl                editor              poplib              unicodedata
_stat               email               posixpath           unittest
_statistics         encodings           pprint              urllib
_string             ensurepip           printNum            uu
_strptime           enum                profile             uuid
_struct             errno               pstats              venv
_symtable           faulthandler        pty                 warnings
_testbuffer         filecmp             py_compile          wave
_testcapi           fileinput           pyclbr              weakref
_testconsole        filelist            pydoc               webbrowser
_testimportmultiple fnmatch             pydoc_data          window
_testinternalcapi   format              pyexpat             winreg
_testmultiphase     fractions           pyparse             winsound
_thread             ftplib              pyshell             wsgiref
_threading_local    functools           query               xdrlib
_tkinter            gc                  queue               xml
_tracemalloc        genericpath         quopri              xmlrpc
_uuid               getopt              random              xxsubtype
_warnings           getpass             re                  zipapp
_weakref            gettext             redirector          zipfile
_weakrefset         glob                replace             zipimport
_winapi             graphlib            reprlib             zlib
_xxsubinterpreters  grep                rlcompleter         zoneinfo
_zoneinfo           gzip                rpc                 zoomheight
abc                 hashlib             run                 zzdummy
aifc                heapq               runpy               
antigravity         help                runscript           

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

help> 
============================================================================================================ RESTART: Shell ============================================================================================================
[DEBUG ON]
[DEBUG OFF]
[DEBUG ON]
[DEBUG OFF]
print("Hello, World!") #This is a comment
Hello, World!
import mymodule
Traceback (most recent call last):
  File "<pyshell#380>", line 1, in <module>
    import mymodule
ModuleNotFoundError: No module named 'mymodule'
import mymodule.py
Traceback (most recent call last):
  File "<pyshell#381>", line 1, in <module>
    import mymodule.py
ModuleNotFoundError: No module named 'mymodule'
