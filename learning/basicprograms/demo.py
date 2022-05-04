#raise keyword for raising any exception if condition is true, 
# else is used to print else block if either one of the block is executed
#finally- this block will execute even if try or catch is executed.
try:
  f = open("example.py","r")
  try:
    print(f.read())
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")