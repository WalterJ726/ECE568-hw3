#include <iostream>
#include "sha256.h"
#include <vector>
#include "assert.h"

using std::string;
using std::cout;
using std::endl;
bool flag;
string output;
string expected_hashed_value = "9994a0007e4271061b671424371f3f04dce63520b25ef9036fa45f3439e2f062";
// string expected_hashed_value = "3803b47609a2a464054659b14a0cdfba92830fb46ee70c03a336d5554b9acad4";
string ans_password;
std::vector<int> ascii_pass;
int k;

void dfs(string &input, int index, int flag){
	if (flag == true){
		return;
	}
	if (index == input.size()){
		output = sha256(input);
		if (expected_hashed_value == output){
			ans_password = input;
			flag = true;
		}
		return ;
	}

	for (int i = 0; i < ascii_pass.size(); i ++ ){
		int temp = input[index];
		input[index] = ascii_pass[i];
		// cout << "index is " << index << "input char is " << input[index] << endl;
		if (flag == true) break;
		dfs(input, index + 1, flag);
		if (flag == true) break;
		input[index] = temp;
	}
	
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
    string input(6, 48);
	cout << "test input is " << input << endl;
	cout << expected_hashed_value.size() << endl;
	cout << expected_hashed_value << endl;
	// 20, 128
	flag = false;
	dfs(input, 0, flag);
 	cout << "Expected answer is " << ans_password << endl;
    cout << "finished" << endl;
    return 0;
}