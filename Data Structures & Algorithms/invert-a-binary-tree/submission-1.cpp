/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(root == nullptr) {
            return nullptr;
        }
        
        //traverse
        TreeNode* tmp = root->left;
        root->left = root->right;
        root->right = tmp;

        //recursive call
        invertTree(root->left);
        invertTree(root->right);

        return root;

    }

    //check invert status
    

    //if we need to invert we invert





};


//Think cases, if we want to invert a binary tree, root stays the same, 
//every left node isnow the right node and the other way around
