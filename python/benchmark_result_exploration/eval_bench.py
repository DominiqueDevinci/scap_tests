import openscap_api as oscap
import inspect
from pprint import pprint

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


benchmark = oscap.xccdf.benchmark_import("./scap-results.xml")
if benchmark.instance is None:
	print("Cannot open the benchmark file.");
	exit();
else:
	print("Benchmark id, ", benchmark.get_id());

# Print the results array to show that arrays also work and show the number of items to show that this is a python array
results = benchmark.get_results()
test_result=results.pop();
print(test_result.get_id());

for rs in test_result.get_rule_results():
	print(rs.get_idref(), result2str(rs.get_result()));


