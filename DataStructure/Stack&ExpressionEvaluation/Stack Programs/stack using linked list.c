/*Program of stack using linked list*/

#include<stdio.h>
#include<stdlib.h>

struct node
{
	int data;
	struct node *link;
}*top=NULL;

int isEmpty()
{
	return (!top)?1: 0;
}/*isEmpty()*/

int peek()
{
	if( isEmpty() )
	{
		printf("Stack Underflow\n");
		exit(1);
	}
	return top->data;
}/*End of peek() */


	
void push(int item)
{
	struct node *temp =(struct node *)malloc(sizeof(struct node));
	if(!temp)
	{
		printf("Stack Overflow\n");
		return;
	}
	temp->data=item;
	temp->link=top;
	top=temp;
}/*End of push()*/

int pop()
{
	struct node *temp;
	int item;
	if( isEmpty() )
	{
		printf("Stack Underflow\n");
		exit(1);
	}
	temp=top;
	item=temp->data;
	top=top->link;
	free(temp);
	return item;
}/*End of pop()*/

void display()
{       
	struct node *p;
	p=top;
	if(isEmpty())
	{	
		printf("Stack is empty\n");
		return;
	}
	printf("Stack elements :\n\n");
	while(p)
	{
		printf(" %d\n",p->data);
		p=p->link;
	}
	printf("\n");
}/*End of display()*/
main()
{
	int choice,item;
	while(1)
	{      	
		printf("1.Push\n");
		printf("2.Pop\n");
		printf("3.Display item at the top\n");
		printf("4.Display all items of the stack\n");
		printf("5.Quit\n");
		printf("Enter your choice : ") ;
		scanf("%d", &choice);

		switch(choice)
		{
		case 1:
			printf("Enter the item to be pushed : ");
			scanf("%d",&item);
			push(item);
			break;
		case 2:
			item=pop();
			printf("Popped item is : %d\n",item);
			break;
		case 3:
			printf("Item at the top is %d\n",peek());
			break;
		case 4:
			display();
			break;
		case 5:
			exit(1);
		default :
			printf("Wrong choice\n");
		}/*End of switch */
	}/*End of while */
}/*End of main() */

