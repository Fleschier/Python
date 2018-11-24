#include<iostream>
#include<string>
#include<vector>
#include<queue>
#include<cmath>

/*����NFAת��ΪDFA*/

using namespace std;

struct NFA_Node;
struct DFA_Node;

bool isElement(string, vector<string>);
// whether a string vector is a subvector of another string 
bool isElement(vector<string>, vector<string>);
bool isElement(vector<string>, vector<vector<string>>);


//find all the elements that isn't in A but in B
vector<string> intersection(vector<string> A, vector<string> B);

class FA_Graph {
public:
	string end_state;
	vector<vector<string>> DFA_end_states;
	static vector<string> Inquire;
	vector<NFA_Node> NFA;
	vector<DFA_Node> DFA;
	void Initialization(string sarr[], int len);		//��ʼ������NFA״̬
	void convert_to_DFA();
	void show_NFA();
	void show_DFA();
	int find_NFA_Node(string);
	bool is_exists(vector<string> DFA_name);
};

//initialize the static element
vector<string> FA_Graph::Inquire = { "A", "B", "C", "D", "E" };

struct NFA_Node {
	string name;
	vector<vector<string>> nextStates;		//index ��ʾת�����룬string��ʾת������״̬��Ĭ��Ϊ��
	NFA_Node() {};
	NFA_Node(string s) {
		this->name = s;
	}
	NFA_Node(string s, vector<vector<string>> vcs) {
		this->name = s;
		this->nextStates = vcs;
	}
	void addTrans(vector<vector<string>> trans){
		this->nextStates = trans;
	}

};

struct DFA_Node {
	vector<string> newStates;				//DFAÿһ���ڵ���NFA״̬�ļ���
	vector<vector<string>> nextState;		//index ��ʾת�����룬string��ʾת������״̬, ��ΪDFAһ��ת��ֻ�ܶ�Ӧһ��״̬������Ҳ�Ƕ�ά���顣
	DFA_Node(){}
	DFA_Node(vector<string> names) {
		this->newStates = names;
	}
	DFA_Node(vector<string> names, vector<vector<string>> vcs) {
		this->newStates = names;
		this->nextState = vcs;
	}
};

int main() {

	FA_Graph test1;
	FA_Graph test2;
	vector<vector<string>> input;	//used for temporary store input data

	//test one data input
	string NodesName1[] = { "A", "B", "C" };
	test1.Initialization(NodesName1, 3);
	//A status convertion
	input.push_back(vector<string>{"A", "B"});		//index = 0
	input.push_back(vector<string>{"A"});				//index = 1
	test1.NFA[0].addTrans(input);
	input.clear();
	//B status convertion
	input.push_back(vector<string>{"C"});
	test1.NFA[1].addTrans(input);
	input.clear();
	test1.end_state = "C";
	cout << "test1 begin: \n";
	test1.show_NFA();
	test1.convert_to_DFA();
	test1.show_DFA();


	//test two data input
	string NodesName2[] = { "A","B","C","D","E" };
	test2.Initialization(NodesName2, 5);
	//A status conversion
	input.push_back(vector<string>{"D"});		//0 conversion
	input.push_back(vector<string>{"B","C"});		//1 conversion
	test2.NFA[0].addTrans(input);
	input.clear();
	//B status conversion	
	input.push_back(vector<string>{"E"});	//0
	test2.NFA[1].addTrans(input);
	input.clear();
	//C status conversion
	input.push_back(vector<string>{"NULL"});		//0
	input.push_back(vector<string>{"D"});			//1
	test2.NFA[2].addTrans(input);
	input.clear();
	//D status conversion
	input.push_back(vector<string>{"D"});
	input.push_back(vector<string>{"E"});
	test2.NFA[3].addTrans(input);
	input.clear();
	test2.end_state = "E";

	cout << "test2 begin:\n";
	test2.show_NFA();
	test2.convert_to_DFA();
	test2.show_DFA();

	////this is a part of test code that learn how to remove redundant elements in a vector
	//string s[] = { "a","c", "d","a","x" };
	//vector<string> vs(s, s + 5);	//��ʼ��vector������ĵ�ַ
	//sort(vs.begin(), vs.end());
	//vs.erase(unique(vs.begin(), vs.end()), vs.end());//unique()�������ظ���Ԫ�طŵ�vector��β�� Ȼ�󷵻�ָ���һ���ظ�Ԫ�صĵ����� ����erase�������������Ԫ�ص����Ԫ�ص����е�Ԫ��
	//for (int i = 0; i < vs.size(); i++) cout << vs[i] << endl;

	return 0;
}

void FA_Graph::Initialization(string sarr[], int len) {
	for (int i = 0; i < len; i++) {
		this->NFA.push_back(NFA_Node(sarr[i]));
	}
}

void FA_Graph::show_NFA() {
	cout << "NFA all convertion: " << endl;
	int len = this->NFA.size();
	for (int i = 0; i < len; i++) {
		for (int j = 0; j < NFA[i].nextStates.size(); j++)
			for (int k = 0; k < NFA[i].nextStates[j].size(); k++) {
				if (NFA[i].nextStates[j][k] != "NULL")
					cout << NFA[i].name << " --- " << j << " ---> " << NFA[i].nextStates[j][k] << endl;
				else
					continue;
			}
	}
	cout << "the NFA end state is: " << this->end_state << endl;
	printf("\n");
}

void show_vector(vector<string> s ) {

	cout << "{ ";
	for (int i = 0; i < s.size(); i++) {
		if(s[i] != "NULL")
			cout << s[i] << " ";
	}
	cout << "}";
}

void FA_Graph::show_DFA() {
	cout << "DFA all convertion: " << endl;
	int len = this->DFA.size();
	for (int i = 0; i < len; i++) {
		for (int j = 0; j < DFA[i].nextState.size(); j++) {
					show_vector(DFA[i].newStates);
					cout << " --- " << j << " ---> ";
					show_vector(DFA[i].nextState[j]);
					cout << endl;
			}
	}
	cout << "the DFA end state(s) :";
	for (int i = 0; i < this->DFA_end_states.size();i++) {
		show_vector(this->DFA_end_states[i]);
	}
	cout << endl;
	printf("\n");
}

//find the corresponding index of string s
int find_IDX(string s) {
	int tmp = -1;
	for (int i = 0; i < FA_Graph::Inquire.size(); i++) {
		if (FA_Graph::Inquire[i] == s)
			tmp = i;
	}
	return tmp;
}

vector<string> remove_redundant(vector<string> vs) {
	sort(vs.begin(), vs.end());
	vs.erase(unique(vs.begin(), vs.end()), vs.end() );
	return vs;
}

//find the next state of a DFA state under the conversion i
vector<string> next_State_Of_DFA_Node(FA_Graph graph, vector<string> vcs, int conver_index) {
	vector<string> res;		//return a new DFA state
	for (int i = 0; i < vcs.size(); i++) {
		//find the corresponding NFA node
		int index = find_IDX(vcs[i]);
		//didn't find the corresponding NFA node
		if (index == -1) {
			cout << "error";
			exit(-1);
		}
		if (conver_index < graph.NFA[index].nextStates.size()) {	//if there exits a conversion on conver_index in this NFA node
			//may exists redundant states
			res.insert(res.end(), graph.NFA[index].nextStates[conver_index].begin(), graph.NFA[index].nextStates[conver_index].end());		//��������vector��insert
		}
		//remove redundant
		res = remove_redundant(res);
	}
	//res.shrink_to_fit();
	return res;
}

//key function
void FA_Graph::convert_to_DFA() {
	vector<NFA_Node> tmp = NFA;
	vector<string> tmpStates;
	queue<DFA_Node> qdn;		//store all the new generated DFA states

	DFA_Node first;		//�����еĵ�һ��״̬����������
	first.newStates.push_back(NFA[0].name);
	qdn.push(first);

	vector<string> tmp_DFA_Node_name;
	while (! qdn.empty()) {
		DFA_Node tmp = qdn.front();
		qdn.pop();

		//if the state include the element of end_state in NFA, then it is the end state of DFA
		if (isElement(this->end_state, tmp.newStates)) {
			if(!isElement(tmp.newStates, DFA_end_states))		//if the end state is already exists
				this->DFA_end_states.push_back(tmp.newStates);
			continue;
		}

		for (int j = 0; j < 2; j++) {		//only 0 and 1 conversion in the test input
			tmp_DFA_Node_name = next_State_Of_DFA_Node(*this, tmp.newStates, j);	//��j�µ�ת���õ�����״̬������
			tmp.nextState.push_back(tmp_DFA_Node_name);		//add the new DFA name to the nextstate of the current DFA Node
			if (!this->is_exists(tmp_DFA_Node_name))	//if it is really a new state
				qdn.push(DFA_Node(tmp_DFA_Node_name));
		}

		if (!this->is_exists(tmp.newStates))	//if it is really a new state
			DFA.push_back(tmp);

	}
}

bool isElement(string s , vector<string> vs) {
	int len = vs.size();
	for (int i = 0; i < len; i++) {
		if (s == vs[i])
			return true;
	}
	return false;
}

//if A is sub-vector of B
bool isElement(vector<string> A, vector<string> B) {
	for (int i = 0; i < A.size(); i++) {
		for (int j = 0; j < B.size(); j++) {
			if (A[i] == B[j]) 
				return false;
		}
	}
	return true;
}

bool isElement(vector<string> A, vector<vector<string>> vvs) {
	if (vvs.empty()) return false;
	for (int i = 0; i < vvs.size(); i++) {
		if (A == vvs[i])
			return true;
	}
	return false;
}

//vector<string> intersection(vector<string> A, vector<string> B) {
//	int lenA = A.size();
//	int lenB = B.size();
//	vector<string> res;
//	for (int i = 0; i < lenB; i++) {
//		if (isElement(B[i], A))
//			res.push_back(B[i]);
//	}
//	return res;
//}

//find the index of NFA Node corresponding to the string s
int FA_Graph::find_NFA_Node(string s) {
	for (int i = 0; i < NFA.size(); i++) {
		if (NFA[i].name == s)
			return i;
	}
	return -1;		//fail to find the Node
}

bool FA_Graph::is_exists(vector<string> DFA_name) {
	if (DFA.empty()) return false;
	for (int i = 0; i < DFA.size(); i++) {
		if (DFA_name == DFA[i].newStates)
			return true;
	}
	return false;
}