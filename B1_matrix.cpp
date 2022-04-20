#include <iostream>
using namespace std;
const int MAX = 100;
void binarySearch(int a[][MAX], int n, int m, int k, int x);
void findRow(int a[][MAX], int n, int m, int k);
int main() {
    int m,n,k;
    cin>>m>>n>>k;
    int mat[m][MAX];
    for(int i = 0 ;i<m;i++)
    {
        for(int j = 0 ;j<n;j++)
        {
            cin>>mat[i][j];
        }
        
    }
     findRow(mat, m, n, k);
    

    return 0;
}

void binarySearch(int a[][MAX], int m, int n, int k, int x)//f is the first number in row, l is the last number in row, mid is the middle number in row
{
   
    int f = 0, l = n - 1, mid;
    while (f <= l)
    {
        mid = (f + l) / 2;
 
        if (a[x][mid] == k)
        {
            cout << "True" <<endl<< x << " " << mid << endl;
            return;
        }
 
        if (a[x][mid] > k)
            l = mid - 1;
        if (a[x][mid] < k)
            f = mid + 1;
    }
    cout << "false" << endl;
}
 
void findRow(int a[][MAX], int m, int n, int k)//searching for row in which number is present
{
 
    int f = 0, l = m - 1, mid; //f is the first row, l is the last row, mid is the middle row
 
    while (f <= l)
    {
        mid = (f + l) / 2;
 
        if (k == a[mid][0])
        {
            cout << "True" <<endl<< mid <<" "<< 0<< endl;
            return;
        }
 
        if (k == a[mid][n - 1]) 
        {
            int t = n - 1;
            cout << "True" <<endl<< mid << " " << t <<endl;
            return;
        }
 
        if (k > a[mid][0] && k < a[mid][n - 1])

        {
            binarySearch(a, m, n, k, mid);
            return;
        }
 
        if (k < a[mid][0])
            l = mid - 1;
        if (k > a[mid][n - 1])
            f = mid + 1;
    }
}
    
    
    
    
