#include "cl_panel.h"
#include "cl_application.h"
#include "cl_reciever.h"

cl_panel::cl_panel(cl_base* p_head_obj, string s_name) : cl_base(p_head_obj, s_name) {};

void cl_panel::signal(string message) {
	cout << "Signal from " << this->get_absolute_path() << endl;
	message += " (class: 3)";
}

void cl_panel::handler(string message) {
	cout << "Signal to " << this->get_absolute_path() << " Text: " << message << endl;
}


void cl_panel::signal_panel_to_screen(string message) {}
void cl_panel::signal_panel_to_refunder(string message) {}
void cl_panel::signal_panel_to_dispenser(string message) {}

void cl_panel::handler_panel_from_reader(string message) {
	if (count(message.begin(), message.end(), ' ') == 1 && message.substr(0, message.find(' ')) == "Product") {
		int productId = stoi(message.substr(message.find(' ') + 1));
		cl_application* appTmp = static_cast<cl_application*>(this->get_head_obj());
		cl_reciever* recieverTmp = static_cast<cl_reciever*>(appTmp->get_sub_object("reciever"));
		o_product* targetProduct = appTmp->getProduct(productId);
		if (targetProduct == nullptr) {
			this->emit_signal(SIGNAL_D(cl_panel::signal_panel_to_screen), "There is no product with this number");
		}
		else if (targetProduct->quantity == 0) {
			this->emit_signal(SIGNAL_D(cl_panel::signal_panel_to_screen), "There is no product");
		}
		else if (recieverTmp->getSum() < targetProduct->price) {
			this->emit_signal(SIGNAL_D(cl_panel:: signal_panel_to_screen), "There is not enough money");
		}
		else {
			targetProduct->quantity--;
			this->emit_signal(SIGNAL_D(cl_panel::signal_panel_to_dispenser), message);
			this->emit_signal(SIGNAL_D(cl_panel::signal_panel_to_refunder), message);
		}
	}
}



