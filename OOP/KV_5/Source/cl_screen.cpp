#include "cl_screen.h"

cl_screen::cl_screen(cl_base* p_head_obj, string s_name) : cl_base(p_head_obj, s_name) {};

void cl_screen::signal(string message) {
	cout << "Signal from " << this->get_absolute_path() << endl;
	message += " (class: 6)";
}

void cl_screen::handler(string message) {
	cout << "Signal to " << this->get_absolute_path() <<  " Text: " << message << endl;
}

void cl_screen::handler_screen_from_all(string message) {
	cout << message;
	if (!(message == "Turned off"))
		cout << endl;
}