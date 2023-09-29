using System;
using static System.Console;
namespace FullMoon
{
class Program
{
static void Main (string[] args)
{
    string[] datos = ReadLine().Split(" ");
    if(int.Parse(datos[1])>int.Parse(datos[0])){
        WriteLine("0");
    }else{
    int totaldias = (int.Parse(datos[0])-int.Parse(datos[1]))/int.Parse(datos[2]);
    WriteLine(totaldias+1);
    }
}
}
}