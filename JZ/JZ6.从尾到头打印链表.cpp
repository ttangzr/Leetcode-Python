/*
 * @Description: 
 * @Author: Zhirong
 * @Date: 2022-02-21 15:10:47
 * @LastEditTime: 2022-02-21 15:48:23
 * @LastEditors: Zhirong
 */

/**
*  struct ListNode {
*        int val;
*        struct ListNode *next;
*        ListNode(int x) :
*              val(x), next(NULL) {
*        }
*  };
*/
class Solution {
public:
    vector<int> ans;
    vector<int> printListFromTailToHead(ListNode* head) {
        // method-1:暴力
        vector<int> ans;
        while (head) {
            ans.push_back(head->val);
            head = head->next;
        }
        std::reverse(ans.begin(), ans.end());
        return ans;

        // method-2:递归/DFS
        if (head) {
            printListFromTailToHead(head->next);
            ans.push_back(head->val);
        }
        return ans;

        // method-3:
        vector<int> ans;
        stack<int> stk;
        if (head == nullptr) {
            return ans;
        }
        while (head) {
            stk.push(head->val);
            head = head->next;
        }
        while (!stk.empty()) {
            int tmp = stk.top();
            stk.pop();
            ans.push_back(tmp);
        }
        return ans;
    }
};