#include<iostream>
using namespace std;

void print(int *arr, int n){

    cout << "Size of the array : " << n << endl;

    for(int i = 0; i < n; i++){
        cout << arr[i] << " ";
    }
    cout << endl;
}

bool LinearSearch(int arr[], int size, int k){

    print(arr, size);

    if(size == 0){
        return false;
    }
    if(arr[0] == k){
        return k;
    }
    else{
        bool remainingpart = LinearSearch(arr + 1, size - 1, k);
        return remainingpart;
    }
}

int main()
{
    int arr[5] = {3, 5, 1, 2, 6};
    int size = 5;
    int key = 2;

    bool ans = LinearSearch(arr, size, key);

    if(ans){
        cout << "Key is present" << endl;
    }
    else{
        cout << "Key is absent" << endl;
    }
    return 0;
}
