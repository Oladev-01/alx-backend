# 0x03 - Queuing System in JavaScript

## Overview
This project implements a queuing system in JavaScript. It provides a straightforward way to manage and process tasks using a queue data structure, showcasing the fundamental concepts of queues and their applications.

## Features
- **FIFO Structure**: Implements a First-In-First-Out (FIFO) queuing mechanism.
- **Task Management**: Ability to enqueue and dequeue tasks efficiently.
- **Flexible API**: Simple methods to interact with the queue (e.g., add, remove, view status).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/0x03-queuing_system_in_js.git
   ```
2. Navigate to the project directory:
   ```bash
   cd 0x03-queuing_system_in_js
   ```

## Usage
You can use the queuing system by importing it into your JavaScript files. Below is a simple example:

```javascript
const Queue = require('./queue');

const myQueue = new Queue();

myQueue.enqueue('Task 1');
myQueue.enqueue('Task 2');

console.log(myQueue.dequeue()); // Output: Task 1
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

