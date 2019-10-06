import openscap_api as oscap
import inspect
from pprint import pprint

def oval_callback(msg, usr):
	print(oscap.xccdf.XCCDF_RESULT_PASS);
	pprint(type(msg));
	pprint(msg.__repr__());
	pprint(msg.object);
	print(type(msg));
	print(dir(msg));
	print(help(msg));
	#print(help(msg.user2num));
	print(msg.get_all_values());
	return 0

oval_file="../samples/oval_is_quadcore.xml";
oval_def=oscap.oval.definition_model_import(oval_file);
if oval_def==None:
	print("Cannot load oval file.");
else:
	print("OVAL file loaded :)");
	
	
sess = oscap.oval.agent_new_session(oval_def, "id1");
sess.__dict__['filename'] = oval_file;
ret = oscap.oval.agent_eval_system(sess, oval_callback, {'false':0,'true':0,'err':0,'unknown':0,'neval':0,'na':0,'verbose':True});	
