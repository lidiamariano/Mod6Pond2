# Módulo 6 - Ponderada 2 - Turtlebot teleoperado
Este projeto implementa um nó de teleoperação (controle remoto) para o robô Turtlebot3 usando ROS 2. O nó permite que o usuário controle o Turtlebot3 usando as teclas do teclado e fornece instruções claras sobre como operar o robô.
## 🤔 Funcionamento do projeto
Controle do Teleop

Use as seguintes teclas para controlar o Turtlebot3:

    'w': Move para frente
    's': Move para trás
    'a': Vira para a esquerda
    'd': Vira para a direita
    'espaço': Para o robô
    'Ctrl+C': Sai do programa
![funcionamento_teleop(1)](https://github.com/lidiamariano/Mod6Pond2/assets/123901342/74e34813-8aaf-4517-b879-c6b3fb15e7d3)

## 💻 Como executar o projeto:
### Pré-requisitos:
- Ubuntu 20.04
- ROS 2 Foxy Fitzroy
- Webots
- Python 3.8 ou superior
### Instalação
1. `git clone https://github.com/lidiamariano/Mod6Pond2.git`
2. `cd ros_ws`
3. `colcon build
   source install/setup.bash`
### Execução
Em um terminal rode:
1. `ros2 launch webots_ros2_turtlebot robot_launch.py`
Em outro terminal:
2. `ros2 run turtlebot3_teleop teleop_node`
