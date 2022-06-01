class Queue {
    var queueArray = [String]()
    
    func enqueue(item:String) {
        self.queueArray.append(item)
    }
    
    func dequeue() -> String?{
        if self.queuekArray.first != nil {
            let firstString = self.queueArray.first
            self.queueArray.removeFirst()
            return firstString!
        } else {
            return nil
        }
    }
    
    func peek() -> String? {
        if self.stackArray.first != nil {
            return self.stackArray.first
        } else {
            return nil
        }
    }
}

var myQueue = Queue()
myQueue.enqueue(item: "Fouad")
myQueue.enqueue(item: "Alaa")
myQueue.enqueue(item: "Ahmad")

print(myQueue.peek()!)