import openscap_api as oscap
import inspect
from pprint import pprint
import re

'''
RESULT OBTAINED (with the official non modified API)
We can see that the object returned by the callback is wrong (object of type xccdf_rule_result but containing a swig object of type oval_result_definition )

python3 test_official_api.py
OVAL file loaded :)
Msg returned by callback: <Oscap Object of type 'xccdf_rule_result' with instance '<Swig Object of type 'struct oval_result_definition *' at 0x7fd3aedbb870>'>
Current structure is : oval_result_definition
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
	#result: <Oscap Object of type 'xccdf_rule_result' with instance '<Swig Object of type 'struct oval_result_definition *' at 0x7f1165668840>'>
	
	obj=msg.instance;
	#extract the name "oval_result_definition" from something like <Swig Object of type 'struct oval_result_definition *' at 0x7f1165668840>
	structure = re.findall(r"type '(struct )?(\b\S*\b)", obj.__repr__())[0][1] 
	print("Current structure is : "+structure);
	
	#convert the swig object in a oscap object handling builtins functions
	nobj=oscap.OSCAP_Object(structure, obj);
	print(result2str(nobj.get_result()));
	return 0

oval_file="../../samples/oval_is_quadcore.xml";
oval_def=oscap.oval.definition_model_import_source(oscap.common.source_new_from_file(oval_file));

if oval_def.instance==None:
	print("Cannot load oval file.");
else:
	print("OVAL file loaded :)");
	
	
sess = oscap.oval.agent_new_session(oval_def, "oval_is_quadcore");
ret = oscap.oval.agent_eval_system(sess, oval_callback, {'false':0,'true':0,'err':0,'unknown':0,'neval':0,'na':0,'verbose':True});	
