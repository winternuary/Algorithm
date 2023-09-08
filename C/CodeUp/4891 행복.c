#include <iostream>
#include <algorithm>

using namespace std;

int arr[1001];

int main() {
	int num;
	cin >> num;

	for (int i = 0; i < num; i++) {
		int x;
		cin >> x;
		arr[i] = x;
	}

	sort(arr, arr + num);

	int result = arr[num - 1] - arr[0];
	cout << result;
}
