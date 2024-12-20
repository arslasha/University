#ifndef __CL_BASE__H
#define __CL_BASE__H

#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>

#define SIGNAL_D( signal_f ) ( TYPE_SIGNAL ) ( & signal_f )
#define HANDLER_D( handler_f ) ( TYPE_HANDLER ) ( & handler_f )

using namespace std;
class cl_base;

typedef void (cl_base::*TYPE_SIGNAL)(string );
typedef void (cl_base::*TYPE_HANDLER)(string);

class cl_base 
{
	struct connect 
	{
		TYPE_SIGNAL signal; //Указатель на метод сигнала
		cl_base* target; //Указатель на целевой объект
		TYPE_HANDLER handler; //Указатель на метод обработчика
	};
	
	
	int status = 0; //индикатор состояниея объекта
	string s_name; 	// наиминование обекта строкового типа
	cl_base* p_head_obj; // указатель на головной объект
	vector <cl_base*> p_sub_objects; //вектор подчиненных объектов
	vector <connect*> connects;
protected:
	struct o_product {
		int id, quantity, price;
		string title;
	};
	
public:

	cl_base (cl_base* p_head_obj, string s_name = "Base object"); //параметризированный конструктор класса
	bool set_name(string s_new_name); // метод установки имени
	string get_name(); // метод получения имени
	cl_base* get_head_obj(); //метод получания указателя на родительский объект
	cl_base* get_sub_object(string s_name); //метод получания указателя на дочерний объект
	cl_base* find_object_from_current(string s_name); // метод поиска объекта на ветке дерева иерархии от текущего по имени
	cl_base* find_object_from_root(string s_name); // метод поиска объекта на дереве иерархии по имени
	void print_branch(int layer = 0); // метод вывода иерархии объектов (дерева или ветки) от текущего объекта
	void print_branch_status(int layer = 0); // метод вывода иерархии объектов (дерева или ветки) и отметок их готовности от текущего объекта
	void set_status(int status); // метод установки готовности объекта, в качестве параметра передается переменная целого типа, содержащая номер состояния
	bool set_head_object(cl_base* p_head_obj); // метод переопределенния головного объекта для текущего в дереве иерархии
	void delete_sub_by_name(string sub_name); // метод удаления подчиненного объекта по наименованию
	cl_base* get_object_by_path(string path); // метод получения указателя на любой объект в составе дерева иерархии объектов согласно пути
	void set_connect(TYPE_SIGNAL signal, cl_base* target, TYPE_HANDLER handler); // метод установки свяхзи между сигналом текущего объекта и обработчиком уелевого объекта
	void remove_connect(TYPE_SIGNAL signal, cl_base* target, TYPE_HANDLER handler); // метод удаления (разрыва) связи между сигналом текущего объекта и обработчиком целевого объекта
	void emit_signal(TYPE_SIGNAL signal, string command); // метод выдачи сигнала от текущего объекта с передачей строковой переменной
	string get_absolute_path(); // установления связи между сигналом текущего объекта и обработчиком целевого объекта
	virtual int get_class_number();// метод возврата номера класса
	void set_status_branch(int new_status); //метод установки объекту и всем потомккам значение готовности
	~cl_base(); // деструктор класса
	void makeBranchReady();
};

#endif
