#ifndef __CL_DISPENSER__H
#define __CL_DISPENSER__H
#include "cl_base.h"

class cl_dispenser : public cl_base {
public:
	cl_dispenser(cl_base* p_head_obj, string s_name);
	//kb-4
	void signal(string message);
	void handler(string message);
	//
	void signal_dispenser_to_screen(string message);
	void handler_dispenser_from_panel(string message);
};

#endif
