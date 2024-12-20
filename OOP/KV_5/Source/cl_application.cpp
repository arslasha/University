#include "cl_application.h"
#include "cl_base.h"
#include "cl_dispenser.h"
#include "cl_panel.h"
#include "cl_reader.h"
#include "cl_reciever.h"
#include "cl_refunder.h"
#include "cl_screen.h"
#include <stack>

cl_application::cl_application(cl_base* p_head_obj):cl_base(p_head_obj) {}

void cl_application::signal(string message) { 
	cout << "Signal from " << this->get_absolute_path() << endl;
	message += " (class: 1)";
}

void cl_application::handler(string message) {
	cout << "Signal to " << this->get_absolute_path() << " Text: " << message << endl;
}

cl_application::o_product* cl_application::getProduct(int productId) {
	o_product* result = nullptr;
	for (auto* product : this->products) {
		if (product->id == productId) {
			result = product;
			break;
		}
	}
	return result;
}

void cl_application::signal_app_to_reader(string message) {}

void cl_application::signal_app_to_screen(string message) {}

void cl_application::handler_app_from_reader(string message) {
	
	if (message == "Turn off the system") {
		this->quitCommand = true;
		this->emit_signal(SIGNAL_D(cl_application::signal_app_to_screen), "Terned off");
	}
	
	else if (count(message.begin(), message.end(), ' ') >= 3) {
		int productId = stoi(message.substr(0, message.find(' ')));
		message = message.substr(message.find(' ') + 1);
		int productQuantity = stoi(message.substr(0, message.find(' ')));
		message = message.substr(message.find(' ') + 1);
		int productPrice = stoi(message.substr(0, message.find(' ')));
		message = message.substr(message.find(' ') + 1);
		string productTitle= message;
		
		o_product* p_product = new o_product();
		p_product->id = productId;
		p_product->quantity = productQuantity;
		p_product->price = productPrice;
		p_product->title = productTitle;
		
		this->products.push_back(p_product);
	}
	
	else if (message == "SHOWTREE") {
		this->print_branch_status();
		this->quitCommand = true;
		this->emit_signal(SIGNAL_D(cl_application::signal_app_to_screen), "Turned off");
	}
}

void cl_application::build_tree_objects(){
	/*
	Описание: метод постраеняи дерева иерархии объектов
	*/
	
	this->set_name("application");
	cl_reader* ob_reader = new cl_reader(this, "reader");
	cl_panel* ob_panel = new cl_panel(this, "panel");
	cl_reciever* ob_reciever = new cl_reciever(this, "reciever");
	cl_refunder* ob_refunder = new cl_refunder(this, "refunder");
	cl_dispenser* ob_dispenser = new cl_dispenser(this, "dispenser");
	cl_screen* ob_screen = new cl_screen(this, "panel");
	this->makeBranchReady();
	
	ob_reader->set_connect(SIGNAL_D(cl_reader::signal_reader_to_all), this, HANDLER_D(cl_application::handler_app_from_reader));
	ob_reader->set_connect(SIGNAL_D(cl_reader::signal_reader_to_all), this, HANDLER_D(cl_panel::handler_panel_from_reader));
	ob_reader->set_connect(SIGNAL_D(cl_reader::signal_reader_to_all), this, HANDLER_D(cl_reciever::handler_reciever_from_reader));
	ob_reader->set_connect(SIGNAL_D(cl_reader::signal_reader_to_all), this, HANDLER_D(cl_refunder::handler_refunder_from_reader));
	
	ob_reciever->set_connect(SIGNAL_D(cl_reciever::signal_reciever_to_screen), ob_screen, HANDLER_D(cl_screen::handler_screen_from_all));
	ob_panel->set_connect(SIGNAL_D(cl_panel::signal_panel_to_screen), ob_screen, HANDLER_D(cl_screen::handler_screen_from_all));
	ob_refunder->set_connect(SIGNAL_D(cl_refunder::signal_refunder_to_screen), ob_screen, HANDLER_D(cl_screen::handler_screen_from_all));
	ob_dispenser->set_connect(SIGNAL_D(cl_dispenser::signal_dispenser_to_screen), ob_screen, HANDLER_D(cl_screen::handler_screen_from_all));
	this->set_connect(SIGNAL_D(cl_application::signal_app_to_screen), ob_screen, HANDLER_D(cl_screen::handler_screen_from_all));
	
	ob_panel->set_connect(SIGNAL_D(cl_panel::signal_panel_to_refunder), ob_refunder, HANDLER_D(cl_refunder::handler_refunder_from_panel));
	ob_panel->set_connect(SIGNAL_D(cl_panel::signal_panel_to_dispenser), ob_dispenser, HANDLER_D(cl_dispenser::handler_dispenser_from_panel));
	
	this->set_connect(SIGNAL_D(cl_application::signal_app_to_reader), ob_reader, HANDLER_D(cl_reader::handler_reader_from_app));
	
	int productTypes;
	cin >> productTypes;
	int c1, c2;
	cin >> c1 >> c2;
	cin.ignore();
	ob_refunder->setCoinsAmount(5, c1);
	ob_refunder->setCoinsAmount(10, c2);
	for (int i = 0; i < productTypes; ++i) {
		this->emit_signal(SIGNAL_D(cl_application::signal_app_to_reader), "");
	}
	
	this->emit_signal(SIGNAL_D(cl_application::signal_app_to_screen), "Ready to work");
}


int cl_application::exec_app() {
	while (!this->quitCommand) {
		this->emit_signal(SIGNAL_D(cl_application::signal_app_to_reader), "");
	}
	return 0;
}
