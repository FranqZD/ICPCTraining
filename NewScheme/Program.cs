using System;
using static System.Console;
namespace NewScheme
{
class Program
{
static void Main (string[] args)
{
    string[] numerosS = new string[8];
    int[] numerosI = new int[8];
    int l=0;
    for(int i = 0;i<=7;i++){
    if(i==0){
        numerosS=ReadLine().Split(' ');
        foreach(string s in numerosS){
            numerosI[l]=int.Parse(s);
            l++;
        }
    }
    else{
        if(numerosI[i-1]<=numerosI[i] && numerosI[i]>=100 && numerosI[i]<=675 && numerosI[i]%25==0){

        }else{
            WriteLine("No");
            return;
        }
    }
    }
    WriteLine("Yes");
}
}
}