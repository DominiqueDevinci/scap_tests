import openscap_api as oscap
import inspect
from pprint import pprint
import re

'''
RESULT OBTAINED (with the modified API):

python3 test_corrected_api.py
OVAL file loaded :)
Msg returned by callback: <Oscap Object of type 'oval_result_definition' with instance '<Swig Object of type 'struct oval_result_definition *' at 0x7fe98cff5870>'>
PASS

'''


def result2str(result):
	if result == oscap.xccdf.XCCDF_RESULT_PASS:
		return "PASS";
	elif result == oscap.xccdf.XCCDF_RESULT_FAIL:
		return "FAIL";
	elif result == oscap.xccdf.XCCDF_RESULT_ERROR:
		return "ERROR";
	elif result == oscap.xccdf.XCCDF_RESULT_UNKNOWN:
		return "UNKNOWN";
	elif result == oscap.xccdf.XCCDF_RESULT_NOT_APPLICABLE:
		return "NOT_APPLICABLE";
	elif result == oscap.xccdf.XCCDF_RESULT_NOT_CHECKED:
		return "NOT_CHECKED";
	elif result == oscap.xccdf.XCCDF_RESULT_NOT_SELECTED:
		return "NOT_SELECTED";
	elif result == oscap.xccdf.XCCDF_RESULT_INFORMATIONAL:
		return "INFORMATIONAL";
	elif result == oscap.xccdf.XCCDF_RESULT_FIXED:
		return "FIXED";

def oval_callback(msg, usr):
	print("Msg returned by callback: "+msg.__repr__());
	#result: <Oscap Object of type 'oval_result_definition' with instance '<Swig Object of type 'struct oval_result_definition *' at 0x7f54f8f92870>'>
	print(result2str(msg.get_result()));
	return 0

oval_file="../../samples/oval_is_quadcore.xml";
oval_def=oscap.oval.definition_model_import_source(oscap.common.source_new_from_file(oval_file));

if oval_def.instance==None:
	print("Cannot load oval file.");
else:
	print("OVAL file loaded :)");
	
sess = oscap.oval.agent_new_session(oval_def, "oval_is_quadcore");
ret = oscap.oval.agent_eval_system(sess, oval_callback, {'false':0,'true':0,'err':0,'unknown':0,'neval':0,'na':0,'verbose':True});	


''' Here is the result obtained if we run this py script with the unmodified official API :
The object returned by the callback is wrong (object of type xccdf_rule_result but containing a swig object of type oval_result_definition),
and so when we try to use "get_result", the api call xccdf_rule_result_get_result but passing an oval_result_def. argument ... which return this kind of traceback.


dom@XUDOM:~/scap_tests/python/oval_test1$ python3 test_corrected_api.py
OVAL file loaded :)
Msg returned by callback: <Oscap Object of type 'xccdf_rule_result' with instance '<Swig Object of type 'struct oval_result_definition *' at 0x7efe0812a870>'>
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/dist-packages/openscap_api.py", line 178, in __getter_wrapper
    retobj = func()
TypeError: xccdf_rule_result_get_result() takes exactly 1 argument (0 given)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.6/dist-packages/openscap_api.py", line 181, in __getter_wrapper
    retobj = func(*newargs)
TypeError: xccdf_rule_result_get_result() takes exactly 1 argument (0 given)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.6/dist-packages/openscap_api.py", line 185, in __getter_wrapper
    retobj = func(self.instance)
TypeError: in method 'xccdf_rule_result_get_result', argument 1 of type 'struct xccdf_rule_result const *'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.6/dist-packages/openscap_api.py", line 188, in __getter_wrapper
    retobj = func(self.instance, *newargs)
TypeError: in method 'xccdf_rule_result_get_result', argument 1 of type 'struct xccdf_rule_result const *'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.6/dist-packages/openscap_api.py", line 339, in __output_callback
    return obj[0](OSCAP_Object("xccdf_rule_result", rule_result), obj[1])
  File "test_corrected_api.py", line 40, in oval_callback
    print(result2str(msg.get_result()));
  File "/usr/local/lib/python3.6/dist-packages/openscap_api.py", line 190, in __getter_wrapper
    raise TypeError("Wrong number of arguments in function %s" % (func.__name__,))
TypeError: Wrong number of arguments in function xccdf_rule_result_get_result
''' 
