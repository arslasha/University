#ifndef __CL_RECIEVER__H
#define __CL_RECIEVER__H
#include "cl_base.h"

class cl_reciever : public cl_base {
	int coins5 = 0, coins10 = 0;
	int banknotes50 = 0, banknotes100 = 0;
public:
	cl_reciever(cl_base* p_head_obj, string s_name);
	// KB-4
	void signal(string message);
	void handler(string message);
	//
	void signal_reciever_to_screen(string message);
	void handler_reciever_from_reader(string message);
	void recieveMoney(int nominal);
	void reset();
	int getSum();
};

#endif
