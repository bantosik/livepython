# livepython

Very simple implementation of single file live coding.
livemod.py main part contains exemplar implementation.

Let's say that you want some process executed in a loop to exhibit behaviour you can modify while the process is running.
Let's call it host loop.
To enable it initialize LiveModule with the filename of the script, and in loop body call checkAndReload and assign 
result to variable which is a handle to an actual module and delegate to a function of your choice on that module the actual loop 
processing.

Limitations:
If python script under governance of LiveModule imports any other script and this other script changes it won't be reflected 
in the host loop execution, it can be fixed in future by watching entire directory instead of a file.
If error is encountered during loading we should fallback to script before the modification.


Watching implemented with the help of
http://stackoverflow.com/a/182259/1362786
