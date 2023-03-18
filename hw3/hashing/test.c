vector<int> temp;
void dfs(int cur, int n) {
    // 剪枝：temp 长度加上区间 [cur, n] 的长度小于 k，不可能构造出长度为 k 的 temp
    if (temp.size() + (n - cur + 1) < k) {
        return;
    }
    // 记录合法的答案
    if (temp.size() == k) {
        ans.push_back(temp);
        return;
    }
    // cur == n + 1 的时候结束递归
    if (cur == n + 1) {
        return;
    }
    // 考虑选择当前位置
    temp.push_back(cur);
    dfs(cur + 1, n, k);
    temp.pop_back();
    // 考虑不选择当前位置
    dfs(cur + 1, n, k);
}