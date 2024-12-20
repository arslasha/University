#ifndef __CL_PANEL__H
#define __CL_PANEL__H
#include "cl_base.h"
	
class cl_panel : public cl_base {
public:
	cl_panel(cl_base* p_head_obj, string s_name);
	//kb-4
	void signal(string message);
	void handler(string message);
	//
	void handler_panel_from_reader(string message);
	void signal_panel_to_screen(string message);
	void signal_panel_to_refunder(string message);
	void signal_panel_to_dispenser(string message);
};

#endif
