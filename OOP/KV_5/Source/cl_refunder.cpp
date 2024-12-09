#include "cl_refunder.h"
#include "cl_application.h"
#include "cl_reciever.h"
	
cl_refunder::cl_refunder(cl_base* p_head_obj, string s_name) : cl_base(p_head_obj, s_name)
{};

void cl_refunder::signal(string message){
	cout << "Signal from " << this -> get_absolute_path() << endl;
	message += " (class: 5)";
}

void cl_refunder::handler(string message){
	cout << "Signal to " << this -> get_absolute_path() << " Text: " << message << endl;
}

//

void cl_refunder::signal_refunder_to_screen(string message){}

void cl_refunder::handler_refunder_from_reader(string message){
	if (message == "Refund money"){
		// refund
		cl_application* appTmp = static_cast<cl_application*>(this->get_head_obj());
		cl_reciever* recieverTmp = static_cast<cl_reciever*>(appTmp->get_sub_object("reciever"));
		int changeTotal = recieverTmp->getSum();
		int changeCoins10 = min(this->coins10, changeTotal / 10);
		int changeCoins5 = (changeTotal - 10 * changeCoins10) / 5;
		if(changeCoins10 && changeCoins5) {
			this->emit_signal(SIGNAL_D(cl_refunder::signal_refunder_to_screen), "Take the change: 10 * " + to_string(changeCoins10) + " rub., 5 * " + to_string(changeCoins5) + " rub.");
		}
		else if (changeCoins10) {
			this->emit_signal(SIGNAL_D(cl_refunder::signal_refunder_to_screen), "Take the change: 10 * " + to_string(changeCoins10) + " rub.");
			
		}
		else if (changeCoins5) {
			this->emit_signal(SIGNAL_D(cl_refunder::signal_refunder_to_screen), "Take the change: 5 * " + to_string(changeCoins5) + " rub.");
		}
		
		this->removeCoins(10, changeCoins10);
		this->removeCoins(5, changeCoins5);
		
		recieverTmp->reset();
		
		this->emit_signal(SIGNAL_D(cl_refunder::signal_refunder_to_screen), "Ready to work");
	}
}

void cl_refunder::handler_refunder_from_panel(string message) {
	int productId = stoi(message.substr(message.find(' ') + 1));
	cl_application* appTmp = static_cast<cl_application*>(this->get_head_obj());
	cl_reciever* recieverTmp = static_cast<cl_reciever*>(appTmp->get_sub_object("reciever"));
	o_product* targetProduct = appTmp->getProduct(productId);
	int changeTotal = recieverTmp->getSum() - targetProduct->price;
	int changeCoins10 = min(this->coins10, changeTotal / 10);
	int changeCoins5 = (changeTotal - 10 * changeCoins10) / 5;
	if (changeCoins10 && changeCoins5) {
		this->emit_signal(SIGNAL_D(cl_refunder::signal_refunder_to_screen), "Take the change: 10 * " + to_string(changeCoins10) + " rub., 5 * " + to_string(changeCoins5) + " rub.");
		
	}
	else if (changeCoins10) {
		this->emit_signal(SIGNAL_D(cl_refunder::signal_refunder_to_screen), "Take the change: 10 * " + to_string(changeCoins10) + " rub.");
	}
	else if (changeCoins5) {
		this->emit_signal(SIGNAL_D(cl_refunder::signal_refunder_to_screen), "Take the change: 5 * " + to_string(changeCoins5) + " rub.");
	}
	
	this->removeCoins(10, changeCoins10);
	this->removeCoins(5, changeCoins5);
		
	recieverTmp->reset();
		
	this->emit_signal(SIGNAL_D(cl_refunder::signal_refunder_to_screen), "Ready to work");
}

void cl_refunder::setCoinsAmount(int nominal, int amount) {
	if (nominal == 5) 
		this->coins5 = amount;
	else
		this->coins10 = amount;
}

void cl_refunder::removeCoins(int nominal, int amount) {
	if (nominal == 5)
		this->coins5 -= amount;
	else 
		this->coins10 -= amount;
}

int cl_refunder::getSum() {
	return this->coins5 * 5 + this->coins10 * 10;
}
