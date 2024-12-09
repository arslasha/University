#ifndef __CL_READER__H
#define __CL_READER__H
#include "cl_base.h"

class cl_reader : public cl_base {
public:
	cl_reader(cl_base* p_head_obj, string name);
	// KB-4
	void signal(string message);
	void handler(string message);
	//K_26
	void handler_reader_from_app(string message);
	void signal_reader_to_all(string message);
};

#endif
