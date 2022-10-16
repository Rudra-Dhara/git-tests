#include<iostream>
using namespace std;


int factorial(int n){
    if (n>=1) {
        return n*factorial(n-1);
    } 
    else if (n==0){
         return 1;
        

    }
           
    else{
        cout<<"wrong entry"<<endl;
        return 0;
    }

}
long int fibo(int n){
    if (n>2){
        return fibo(n-1) + fibo(n-2);
    }
    else if (n>0){
        return 1;
    }
    else{
        cout<<"wrong input";
        return 0;
    }
}


int main(){
    int a; int i=0;
    cout<<"enter a number:";
    cin>>a;
    while (i<=a){
        cout<<fibo(i)<<"\t";
        cout<<sizeof(fibo(i))<<endl;
        i++;
    }
    return 0;
}