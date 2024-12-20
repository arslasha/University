#include "cl_reciever.h"
#include "cl_refunder.h"

cl_reciever::cl_reciever(cl_base* p_head_obj, string s_name) : cl_base(p_head_obj, s_name) {};

void cl_reciever::signal(string message) {
	cout << "Signal from " << this->get_absolute_path() << endl;
	message += " (class: 4)";
}

void cl_reciever::handler(string message) {
	cout << "Signal from " << this-> get_absolute_path() << " Text: " << message << endl;
}

void cl_reciever::signal_reciever_to_screen(string mesasge) {} 

void cl_reciever::handler_reciever_from_reader(string message) {
	if (message.find(' ') == string::npos && !(message == "SHOWTREE")) {
		// deposising money
		if (message == "5" || message == "10") {
			// a coin
			int coin = stoi(message);
			this->recieveMoney(coin);
			this->emit_signal(SIGNAL_D(cl_reciever::signal_reciever_to_screen), "The amount: " + to_string(this->getSum()));
			
			// move coin to refunder
			cl_refunder* cl_refunderTmp = static_cast<cl_refunder*>(this->get_head_obj()->get_sub_object("refunder"));
			cl_refunderTmp->removeCoins(coin, -1);
		}
		else {
			// a banknote getCoinsInfo
			int banknote = stoi(message);
			cl_refunder* refunderTmp = static_cast<cl_refunder*>(this->get_head_obj()->get_sub_object("refunder"));
			if (refunderTmp->getSum() >= this->getSum() + banknote) {
				this->recieveMoney(banknote);
				this->emit_signal(SIGNAL_D(cl_reciever::signal_reciever_to_screen), "The amount: " + to_string(this->getSum()));
			}
			else {
				this->emit_signal(SIGNAL_D(cl_reciever::signal_reciever_to_screen), "Take the money back, no change");
			}
		}
	}
}

void cl_reciever::recieveMoney(int nominal) {
	if (nominal == 5) this->coins5++;
	else if (nominal == 10) this->coins10++;
	else if (nominal == 50) this->banknotes50++;
	else if (nominal == 100) this->banknotes100++;
}

void cl_reciever::reset() {
	this->coins5 = 0;
	this->coins10 = 0;
	this->banknotes50 = 0;
	this->banknotes100 = 0;
}

int cl_reciever::getSum() {
	return this->coins5 * 5 + this->coins10 * 10 + this->banknotes50 * 50 + this->banknotes100 * 100;
}
	
			
