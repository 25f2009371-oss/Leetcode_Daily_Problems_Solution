class BrowserHistory {
    std::stack<string>past;
    std::stack<string>future;
public:
    BrowserHistory(string homepage) {
        past.push(homepage);
    }
    
    void visit(string url) {
        past.push(url);
        std::stack<string>().swap(future);
    }
    
    string back(int steps) {
        while((past.size()>1) && steps--){
            future.push(past.top());
            past.pop();
        }
        return past.top();
    }
    
    string forward(int steps) {
        while(!future.empty() && steps--){
            past.push(future.top());
            future.pop();
        }
        return past.top();
    }
};

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory* obj = new BrowserHistory(homepage);
 * obj->visit(url);
 * string param_2 = obj->back(steps);
 * string param_3 = obj->forward(steps);
 */