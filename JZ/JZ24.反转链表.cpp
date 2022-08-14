/*
 * @Description: 
 * @Author: Zhirong
 * @Date: 2022-02-21 15:18:14
 * @LastEditTime: 2022-02-21 15:29:15
 * @LastEditors: Zhirong
 */
/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :JZ
			val(x), next(NULL) {
	}
};*/
class Solution {
public:
    ListNode* ReverseList(ListNode* pHead) {
        // mehthod-1: 双指针/迭代
        ListNode* prev = NULL;
        ListNode* curr = pHead;
        ListNode* nex = NULL;
        while (curr) {
            nex = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nex;
        }
        return prev;

        // method-2: 递归
        if (pHead == NULL or pHead->next == NULL)
            return pHead;
        ListNode* pReverse = ReverseList(pHead->next);
        pHead->next->next = pHead;
        pHead->next = NULL;
        return pReverse;
    }
};