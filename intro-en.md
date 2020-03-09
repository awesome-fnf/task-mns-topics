## Description
Serverless workflow task step publish messages to MNS topic, and wait for callback. MNS topic use FC http trigger as
 HTTP subscription endpoint, which will report task succeeded to workflow.

## How to use
Parameters:
- TopicName: self-defined mns topic name.

![usage](https://img.alicdn.com/tfs/TB1_T1LxUz1gK0jSZLeXXb9kVXa-1365-641.gif)

## Framework
![framework](https://img.alicdn.com/tfs/TB1.yaNxNz1gK0jSZSgXXavwpXa-1106-584.png)

## Reference
1. [Application code](https://github.com/awesome-fnf/task-mns-topics)