# LuaVersion Directory - CubeAI

Welcome to the **LuaVersion** directory of the **CubeAI** project. This folder contains the necessary files and modules to implement a Rubik's Cube solver within the **Roblox** platform, utilizing the Lua scripting language. The project explores efficient algorithms to solve a Rubik's Cube while providing a visual and interactive experience.

## 📁 Directory Structure
```
LuaVersion/
├── CubeModule.lua       <-- Core module for cube representation
├── SolverModule.lua     <-- Algorithm module for solving the cube
├── MainScript.server.lua <-- Main entry point script for Roblox
└── UI/
    └── CubeUI.lua       <-- UI elements for cube visualization
```

## 📄 File Descriptions
### 1. **CubeModule.lua**
This module represents the Rubik's Cube's state and provides methods to manipulate it. It tracks the cube's configuration and includes functions to rotate layers and check for solved states.

### 2. **SolverModule.lua**
This module implements the solving algorithms for the Rubik's Cube. It includes different search algorithms like **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** to find the most efficient path to solving the cube.

### 3. **MainScript.server.lua**
The main entry point for the Lua version of CubeAI. This script handles the interaction between the cube's state and the solving algorithms, running the solver and displaying results in the Roblox environment.

### 4. **UI/CubeUI.lua**
This optional module contains UI components to provide a visual representation of the Rubik's Cube within Roblox. It helps players interact with and visualize the cube's state and solving process.

## 🚀 How to Run in Roblox Studio
1. Open **Roblox Studio**.
2. Create a new project or open an existing one.
3. Import the scripts from the **LuaVersion** directory.
4. Place the **MainScript.server.lua** in the **ServerScriptService**.
5. Run the project to see the Rubik's Cube solver in action.

## 🤖 Solver Algorithms
The solver in **SolverModule.lua** uses:
- **Breadth-First Search (BFS)** to explore all possible moves systematically.
- **Depth-First Search (DFS)** to dive deeper into solving paths.

Future plans include adding more advanced heuristic-based solving methods.

## 🎨 UI Customization
The **UI/CubeUI.lua** file can be modified to customize the visual representation of the cube. You can adjust colors, animation speed, and interaction elements to enhance the user experience.

## 📈 Future Enhancements
- [ ] Add more solving algorithms, including **A*** and **IDA***.
- [ ] Improve UI elements for better user interaction.
- [ ] Add multiplayer functionality to compete in cube-solving challenges.

## 🔧 Contribution
Contributions to the **LuaVersion** are welcome! Feel free to fork the repository and submit a pull request with improvements, bug fixes, or new features.

