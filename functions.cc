#include<iostream>
using namespace std;

float Squre(float a){
    return (a*a);
}
int main(){
    int var1 =5;
    char var2[10];

    cout<< "adress of var1";
    cout<< &var1<< endl;
    cout<< &var2<< endl;
    int *y;
    y=&var1;
    cout<<*y;
    return 0;
}