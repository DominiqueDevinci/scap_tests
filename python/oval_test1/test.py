import openscap_api as oscap
import inspect
from pprint import pprint
import re

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
	pprint(msg.__repr__());
	pprint(msg.object);
	pprint(msg.instance);
	pprint(dir(msg.instance));
	retobj=msg.instance;
	structure = re.findall(r"type '(struct )?(\b\S*\b)", retobj.__repr__())[0][1]
	print(structure);
	nobj=oscap.OSCAP_Object(structure, retobj);
	pprint(nobj.introspect_current());
	print(nobj.get_result());
	return 0

oval_file="../../samples/oval_is_quadcore.xml";
oval_def=oscap.oval.definition_model_import_source(oscap.oval.oscap_source_new_from_file(oval_file));

if oval_def.instance==None:
	print("Cannot load oval file.");
else:
	print("OVAL file loaded :)");
	
	
sess = oscap.oval.agent_new_session(oval_def, "oval_is_quadcore");
ret = oscap.oval.agent_eval_system(sess, oval_callback, {'false':0,'true':0,'err':0,'unknown':0,'neval':0,'na':0,'verbose':True});	
