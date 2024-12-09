#ifndef __CL_REFUNDER__H
#define __CL_REFUNDER__H
#include "cl_base.h"
	
class cl_refunder : public cl_base {
	int coins5, coins10;
public:
	cl_refunder(cl_base* p_head_obj, string s_name);
	// KB-4
	void signal(string message);
	void handler(string message);
	//
	void signal_refunder_to_screen(string message);
	void handler_refunder_from_reader(string mesasge);
	void handler_refunder_from_panel(string message);
	void setCoinsAmount(int nominal, int amount);
	void removeCoins(int nominal, int amount);
	int getSum();
};


#endif
