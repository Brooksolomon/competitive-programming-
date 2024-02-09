#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int n,k ;
    cin >>n>>k;
    while(k){
        if(n%10)
            n-=1;  
        else
            n/=10;
            
        k-=1;
    } 
    cout<<n;
}
