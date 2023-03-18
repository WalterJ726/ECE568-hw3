#include <iostream>
#include "sha256.h"
#include <vector>
#include "assert.h"

using std::string;
using std::cout;
using std::endl;
bool flag;
string output;
string expected_hashed_value = "3803b47609a2a464054659b14a0cdfba92830fb46ee70c03a336d5554b9acad4";
string ans_password;
string input;
int k;
std::vector<int> ascii_pass;

void dfs(int index, int flag){
	if (flag == true){
		return;
	}

	if (input.size() + (ascii_pass.size() - index + 1) < k){
		return ;
	}

	if (input.size() == k){
		cout << "now input is " << input << endl;
		output = sha256(input);
		if (expected_hashed_value == output){
			ans_password = output;
			flag = true;
			return;
		}
	}

	if (index == ascii_pass.size() + 1){
		return;
	}

	// select
	input.push_back(ascii_pass[index - 1]);
	dfs(index + 1, flag);
	input.pop_back();
	// don't select
	dfs(index + 1, flag);
	
}
int main(int argc, char *argv[])
{
	for (int i = 48; i <= 57; i ++ ){
		ascii_pass.push_back(i);
	}
	for (int i = 65; i <= 90; i ++ ){
		ascii_pass.push_back(i);
	}
	for (int i = 97; i <= 122; i ++ ){
		ascii_pass.push_back(i);
	}

	cout << "ascii_pass size is " << ascii_pass.size() << endl;
	assert(ascii_pass.size() == 62);
	// 32～126
    // string input(4, 48);
	// cout << "test input is " << input << endl;
	cout << expected_hashed_value.size() << endl;
	cout << expected_hashed_value << endl;
	// 20, 128
	flag = false;
	k = 4;
	dfs(1, flag);
 	if (flag == true) cout << "Expected answer is " << ans_password << endl;
    cout << "finished" << endl;
    return 0;
}