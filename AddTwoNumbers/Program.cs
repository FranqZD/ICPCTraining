using System;
using static System.Console;
namespace TwoNumbers
{
class Program
{
      public class ListNode {
      public int val;
      public ListNode next;
      public ListNode(int val=0, ListNode next=null) {
          this.val = val;
          this.next = next;
      }
  }
  public static ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        string numero1="";
        string numero2="";
        string volteadin1="";
        string volteadin2="";
        
        //Iteramos la lista enlazada y lo metemos a un string
        while(l1!=null){
        numero1 = numero1+l1.val;
        l1=l1.next;
        }
        do
        {
        numero2 = numero2+l2.val;
        l2 = l2.next;
        }while(l2!=null);

        //Volteamos el string
        for(int i = numero1.Length-1; i!=-1; i--){
            volteadin1=volteadin1+numero1[i];
        }
        for(int i = numero2.Length-1; i!=-1; i--){
            volteadin2=volteadin2+numero2[i];
        }
        //Convertimos volteadin  a un entero
        int num1 = int.Parse(volteadin1);
        int num2 = int.Parse(volteadin2);
        

        num1=num1+num2;
        numero1 = ""+num1;
        WriteLine("TOTAL:" + numero1);
            ListNode Resultado = new ListNode(int.Parse(numero1[numero1.Length - 1].ToString()));
             ListNode Head = new ListNode(0,Resultado);


         for(int i =numero1.Length-1;numero1[i]!=numero1[0];i--){
            Resultado.next=new ListNode(int.Parse(numero1[i].ToString()));
            Resultado=Resultado.next;
         }
         return Head;
    }
static void Main (string[] args)
{
    ListNode l1 = new ListNode(2);
    l1.next=new ListNode(4);
    l1.next.next=new ListNode(3);

    ListNode l2 = new ListNode(5);
    l2.next = new ListNode(6);
    l2.next.next = new ListNode(4);
            l1 = AddTwoNumbers(l1, l2);
            WriteLine(l1.val);
    while(l1.next!=null){
        WriteLine("linkedlist: "+l1.val);
        l1=l1.next;
    }
}  
}
}