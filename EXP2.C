#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

struct Node
{
int data;
struct Node* next;
};

void insertAtBeginning(struct Node** head_ref, int new_data)
{
struct Node* new_node=(struct Node*)malloc(sizeof(struct Node));
new_node->data = new_data;
new_node->next = (*head_ref);
(*head_ref)=new_node;
}
void deleteNode (struct Node** head_ref,int key)
{
struct Node*temp = *head_ref, *prev;
if(temp !=NULL&&temp->data==key)
{
*head_ref = temp -> next ;
free(temp);
return;
}
while(temp!=NULL && temp -> data != key)
{
prev = temp ;
temp =temp -> next;
}
if ( temp == NULL )return;
prev->next = temp ->next;
free(temp);
}

void displayList( struct Node* node)
{
while (node != NULL)
{
printf ("%d->",node->data);
node = node-> next;
}
printf("NULL\n");
}
     int main(){
     struct Node* head = NULL;
     insertAtBeginning(&head, 1);
     insertAtBeginning(&head, 2);
     insertAtBeginning(&head, 3);
     printf("Linked List:");
     displayList(head);
     deleteNode(&head,2);
     printf("Linked list after deletion :");
     displayList(head);
     getch();
     return 0;
     }







