#include "cl_dispenser.h"
#include "cl_application.h"
#include "cl_panel.h"

cl_dispenser::cl_dispenser(cl_base* p_head_obj, string s_name) : cl_base(p_head_obj, s_name) {};

void cl_dispenser::signal(string message) {
	cout << "Signal from " << this->get_absolute_path() << endl;
	message += " (class: dispencer)";
}

void cl_dispenser::handler(string message) {
	cout << "String to " << this->get_absolute_path() <<  " Text: " << message << endl;
}

void cl_dispenser::signal_dispenser_to_screen(string message) {}

void cl_dispenser::handler_dispenser_from_panel(string message) {
	int productId = stoi(message.substr(message.find(' ') + 1));
	cl_application* appTmp = static_cast<cl_application*>(this->get_head_obj());
	o_product* targetProduct = appTmp->getProduct(productId);
	this->emit_signal(SIGNAL_D(cl_dispenser::signal_dispenser_to_screen), "Take the product " + targetProduct->title);
}

