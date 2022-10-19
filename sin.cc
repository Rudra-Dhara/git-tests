#include<iostream>
#include<cmath>
using namespace std;

int main(){
    double x = 0.5, result;
    
    result=sin(x);
    cout<<result<<endl;

    double xDegree = 45;

    x= 45*M_PI/180;
    result=sin(x);

    cout<<result<<endl;

    return 0;
}
