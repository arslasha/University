#ifndef __CL_APPLICATION__H
#define __CL_APPLICATION__H
#include "cl_base.h"

class cl_application : public cl_base // наследование от класса cl_base
{
	vector<o_product*> products;
	bool quitCommand = false;
public: 
	cl_application(cl_base* p_head_obj); // параметризированный конструктор
	void build_tree_objects(); // метод построение дерева иерархии объектов
	int exec_app(); // запуск основного алгоритма программы
	void signal(string message);
	void handler(string message);
	o_product* getProduct(int productId);
	void signal_app_to_reader(string message);
	void signal_app_to_screen(string message);
	void handler_app_from_reader(string message);
};

#endif
