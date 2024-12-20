#ifndef __CL_SCREEN__H
#define __CL_SCREEN__H
#include "cl_base.h"
	
class cl_screen : public cl_base {
public:
	cl_screen(cl_base* p_head_obj, string s_name);
	//kb-4
	void signal(string message);
	void handler(string message);
	//
	void handler_screen_from_all(string message);
};

#endif
