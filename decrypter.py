import marshal, struct, sys, time, py_compile, traceback, fupy, os

def unpack_pyc(filename):
    f = open(filename, "rb")
    magic = f.read(4)
    unixtime = struct.unpack("L", f.read(4))[0]
    timestamp = time.asctime(time.localtime(unixtime))
    code = marshal.load(f)
    f.close()
    return filename, magic, unixtime, timestamp, code

def mydecomp(decrypted_name,decompyled_name):
	indent_pattern = ' ' * 4
	pydec = fupy.PythonDecompiler(decrypted_name)
	dump = pydec.decompile(indent = indent_pattern)
	output = open(decompyled_name, "w")  
	output.write(dump)
	output.close()

def mydecrypt(code,decrypted_name,decompyled_name):
	with open(decrypted_name, 'wb') as fc:
		fc.write(py_compile.MAGIC)
		py_compile.wr_long(fc, long(time.time()))
		marshal.dump(code, fc)
		fc.flush()
		fc.seek(0, 0)
		mydecomp(decrypted_name,decompyled_name)
	

def do(name):
	pname = os.path.dirname(os.path.abspath(__file__))+"\\"+name
	crypted_name = pname + ".pyc"
	decrypted_name = pname + "___decrypt.pyc"
	decompyled_name = pname + "___decrypt.py"
	sys.path.append(os.path.dirname(pname))
	try:
		cur_module = __import__(os.path.basename(pname))
		filename, magic, unixtime, timestamp, code = unpack_pyc(crypted_name)
		mydecrypt(code,decrypted_name,decompyled_name)
	except:
		traceback.print_exc(file=sys.stdout)
		exc_traceback = sys.exc_info()[2]
		trkobj = exc_traceback
		while(trkobj.tb_next is not None):
			trkobj = trkobj.tb_next
		code = trkobj.tb_frame.f_code
		mydecrypt(code,decrypted_name,decompyled_name)
		
first = True
for file in sys.argv:
	if first:
		first = False
		continue
	pythonFolder = os.path.dirname(os.path.abspath(__file__))
	modulePath = file.replace(pythonFolder+'\\',"")
	do(os.path.splitext(modulePath)[0])