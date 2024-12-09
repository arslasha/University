#include "cl_reader.h"

cl_reader::cl_reader(cl_base* p_head_obj, string s_name) : cl_base(p_head_obj, s_name) {};

void cl_reader::signal(string message){
	cout << "Signal from " << this -> get_absolute_path() << endl;
	message += " (class: dispenser)";
}

void cl_reader::handler(string message)
{
	cout << "Signal to " << this -> get_absolute_path() << " Text: " << message << endl;
}

void cl_reader::signal_reader_to_all(string message){}

void cl_reader::handler_reader_from_app(string message){
	string inputLine;
	getline(cin, inputLine);
	this->emit_signal(SIGNAL_D(cl_reader::signal_reader_to_all), inputLine);
}