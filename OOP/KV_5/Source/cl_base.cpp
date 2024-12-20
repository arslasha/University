#include "cl_base.h"
#include "stack"

cl_base::cl_base(cl_base* p_head_obj, string s_name)
{
	/*
	Описание: Параметризированный конструктор
	Параметры: 
		p_head_obj - указатель на головной объекта;
		s_name - имя узла дерева;
	*/
	
	this->s_name = s_name;
	this->p_head_obj = p_head_obj;
	if (p_head_obj) 
		p_head_obj->p_sub_objects.push_back(this);
}

bool cl_base::set_name(string s_new_name){
	
	/*
	Описание: редактировнаия имени объекта;
	Параметры: 
		s_new_name - новое имя узла дерева;
	*/
	
	if(p_head_obj)
		for (int i = 0; i < p_head_obj->p_sub_objects.size(); ++i)
			if(p_head_obj->p_sub_objects[i]->get_name() == s_new_name)
				return false;
	this->s_name = s_new_name;
	return true;
}

string cl_base::get_name(){
	/*
	Описание:метод поулчения имени объекта
	Параметры: нет
	*/
	return this->s_name;
}

cl_base* cl_base::get_head_obj(){
	/*
	Описание:метод поулчения указаетля на головной объект текущего объекта 
	Параметры: нет
	*/
	return this->p_head_obj;
}

cl_base* cl_base::get_sub_object(string s_name){
	
	/*
	Описание: получение указателя на непосредтсвенно подчиненный объект по имени
	Параметры: 
		s_name - имя искомого объекта
	*/
	
	for (int i = 0; i < p_sub_objects.size(); ++i)
		if(p_sub_objects[i]->get_name() == s_name)
			return p_sub_objects[i];
	return nullptr;
}

cl_base* cl_base::find_object_from_current(string s_name)
{
	/*
	Описание: метод поиска объекта на ветке по имени(обход графа в ширину)
	Параметры:
		s_name - имя искомого объекта
	*/
	queue<cl_base*> q;// очередь элементов 
	cl_base* found = nullptr; // объявление нулевого указателя 
	q.push(this); // добавление в очередь всех наших элементов
	while (!q.empty()) // пока очередь не пуста
	{
		cl_base* e = q.front(); // указатель на текущий объект
		if (e -> get_name() == s_name) // cовпадает ли имя с текущим объектом
		{
			if (found != nullptr) // указатель не пустой и объект не уникалдьный 
				return nullptr;
			else{
				found = e; // записывавем указатель на этот объект
			}
		}
		for (int i = 0; i < e->p_sub_objects.size(); ++i) // проходим по подчиненным элементам
		q.push(e->p_sub_objects[i]); //каждый элемент добавляем в очередь
		q.pop(); // удаление элемента из начала очереди чтобы пройти по всем элементам
		
	}
	return found;
}

cl_base* cl_base::find_object_from_root(string s_name) 
{
	/*
	Описание: метод поиска объекта на дереве иерархии по имени
	Параметры:
		s_name - имя искомого объекта
	*/
	if (p_head_obj != nullptr) // есои головнойтобъект существует
		return p_head_obj -> find_object_from_root(s_name);
	else return find_object_from_current(s_name);
}

void cl_base::print_branch(int layer)
{
	/*
	Описание: метод вывода иерархии объектов (дерева или ветки) от текущего объекта
	Параметры:
		layer - уровень на дереве иерархии
	*/
	cout << endl;
	
	for (int i = 0; i < layer; ++i)
		cout << "    ";
	
	cout << this->get_name();
	for (int i = 0; i < p_sub_objects.size(); ++i)
		p_sub_objects[i]->print_branch(layer + 1);
}

void cl_base::print_branch_status(int layer)
{
	/* 
	Описание: метода вывода иерархии объектов (дерева или ветки) и отметок их готовности от текущего объекта
	Параметры:
		layer - уровень на дереве иерархии
	*/ 
	cout << endl;
	
	for(int i = 0; i < layer; ++i)
		cout << "    ";
	
	if (this->status != 0)
		cout << this->get_name() << " is ready";
	else cout << this->get_name() << " is not ready";
	
	for (int i = 0; i < p_sub_objects.size(); ++i)
		p_sub_objects[i]->print_branch_status(layer + 1);
}

void cl_base::set_status(int status)
{
	/*
	Описание: метода установки готовности объекта
	Параметры:
		status - пременная целого типа, содержит номер состояния
	*/
	if (p_head_obj == nullptr || p_head_obj->status != 0)
		this->status = status;
	
	if (status == 0)
	{
		this-> status = status;
		for (int i = 0; i < p_sub_objects.size(); ++ i)
			p_sub_objects[i]->set_status(status);
	}
}

bool cl_base::set_head_object(cl_base* new_p_head_obj) 
{
	/*
	Описание:метод переопределения головного объекта для текущего объекта в дереве иерархии
	Параметры: new_p_head_object - пременная содержит новое имя головного объекта
	*/
	if (this -> get_head_obj() == new_p_head_obj)
		return true;
	if (this->get_head_obj() == nullptr || new_p_head_obj == nullptr)
		return false;
	if (new_p_head_obj->get_sub_object(this->get_name()) != nullptr)
		return false;
	
	stack<cl_base*> st;
	st.push(this);
	while (!st.empty())
	{
		cl_base* current = st.top();
		st.pop();
		if (current == new_p_head_obj)
			return false;
		for (int i = 0; i < current->p_sub_objects.size(); ++i)
			st.push(current->p_sub_objects[i]);
	}
	vector<cl_base*> & v = this->get_head_obj()->p_sub_objects;
	for (int i = 0; i < v.size(); ++i)
		if (v[i]->get_name() == this->get_name())
		{
			v.erase(v.begin() + i);
			new_p_head_obj->p_sub_objects.push_back(this);
			return true;
		}
	return false;
}

void cl_base::delete_sub_by_name(string sub_name)
{
	/*
	Описание:метод удаления подчиненного объекта по наименованию
	Параметры: 
		sub_name - пременная строкого типа, содержит имя подчиненного объекта
	*/
	vector<cl_base*> & v = this->p_sub_objects;
	for (int i = 0; i < v.size(); ++i)
		if (v[i]->get_name() == sub_name)
		{
			delete v[i];
			v.erase(v.begin() + i);
			return;
		}
}

cl_base* cl_base::get_object_by_path(string path) 
{ 
	/*
	Описание:метод поулчения указателя на любой объект в составе дерева иерархии объектов согласно пути
	Параметры: 
		path - переменная стрового типа, содержит указатель на объект
	*/
	if (path.empty())
		return nullptr;
	if (path == ".")
		return this;
	if (path[0] == '.')
		return find_object_from_current(path.substr(1));
	if (path.substr(0, 2) == "//")
		return this->find_object_from_root(path.substr(2));
	if (path[0] != '/')
	{
		size_t slash = path.find('/');
		cl_base* sub_ptr = this->get_sub_object(path.substr(0, slash));
		if (sub_ptr == nullptr || slash == string::npos)
			return sub_ptr;
		return sub_ptr->get_object_by_path(path.substr(slash + 1));
	}
	
	cl_base* root = this;
	while (root->get_head_obj() != nullptr)
		root = root->get_head_obj();
	if(path == "/")
		return root;
	return root->get_object_by_path(path.substr(1));
}

void cl_base::set_connect(TYPE_SIGNAL signal, cl_base* target, TYPE_HANDLER handler)
{
	/*
	Описание: метод связи между сигналом текущего объекта и обработчиком целевого объекта
	*/
	
	for (int i = 0; i < connects.size(); ++i)
		if (connects[i]->signal == signal && connects[i]->target == target && connects[i]->handler == handler)
			return;
	connect * new_connect = new connect();
	new_connect->signal = signal;
	new_connect->target = target;
	new_connect->handler = handler;
	connects.push_back(new_connect);
}

void cl_base::remove_connect(TYPE_SIGNAL signal, cl_base* target, TYPE_HANDLER handler)                                    
{
	/*
	Описание: метод удаления (разрыва) связи между сигналом текущего объекта и обработчиокм целевого объекта
	*/
	for (int i = 0; i < connects.size(); ++i)
		if (connects[i]->signal == signal && connects[i]->target == target && connects[i]->handler == handler)
		{
			delete connects[i];
			connects.erase(connects.begin() + i);
			return;
		}
}

void cl_base::emit_signal(TYPE_SIGNAL signal, string command)
{
	/*
	ОПисание: метод выдачи сигнала от текущего объекта с перердачей строковой переменной
	*/
	if (!this->status)
		return;
	TYPE_HANDLER handler;
	cl_base* target;
	(this->*signal)(command);
	for (int i = 0; i < connects.size(); ++i) {
		if (connects[i]->signal == signal)
		{
			handler = connects[i]->handler;
			target = connects[i]->target;
			if (target->status != 0)
				(target->*handler)(command);
		}
	}
}

string cl_base::get_absolute_path()
{
	/*
	Описание: метод определения абсолютного пути до текущего объекта
	*/
	
	string result;
	stack <string> st;
	cl_base* root = this;
	while (root->get_head_obj() != nullptr)
	{
		st.push(root->get_name());
		root = root->get_head_obj();
	}
	while (!st.empty())
	{
		result += '/' + st.top();
		st.pop();
	}
	if (result.empty())
		return "/";
	return result;
}

int cl_base::get_class_number()
{
	/*
	Описание: метод получения указателя на класс 
	*/
	return 0;
}

void cl_base::set_status_branch(int new_status)
{
	/*
	Опсиание: метод установки объекту и всем его потомкам значение готовности
	Параметры: 
		new_status - переменная целого типа, содержит значение готовности
	*/
	if (get_head_obj() != nullptr && get_head_obj()->status == 0)
		return;
	
	set_status(new_status);
	for (int i = 0; i < p_sub_objects.size(); ++i)
		p_sub_objects[i]->set_status_branch(new_status);
}

cl_base::~cl_base(){
	/*
	Описание: деструктор
	Параметры: нет
	*/
	cl_base* root = this;
	while (root->get_head_obj() != nullptr)
		root = root->get_head_obj();
	stack<cl_base*> st;
	st.push(root);
	while (!st.empty())
	{
		cl_base* ptr = st.top();
		st.pop();
		int i = 0;
		while (i < ptr->connects.size())
		{
			if (ptr->connects[i]->target == this)
			{
				delete ptr->connects[i];
				ptr->connects.erase(ptr->connects.begin() + i);
			}
			else i++;
		}
		for (int i = 0; i < ptr->p_sub_objects.size(); ++i)
			st.push(ptr->p_sub_objects[i]);
	}
	for (int i = 0; i < connects.size(); ++i)
	{
		delete connects[i];
		connects.erase(connects.begin() + i );
		i--;
	}
	for (int i = 0; i < p_sub_objects.size(); ++i)
	{
		delete p_sub_objects[i];
		p_sub_objects.erase(p_sub_objects.begin() + i);
		i--;
	}
}

// К_26
void cl_base::makeBranchReady() {
	this->status = 1;
	for (auto* sub_object : p_sub_objects) {
		sub_object->makeBranchReady();
	}
}