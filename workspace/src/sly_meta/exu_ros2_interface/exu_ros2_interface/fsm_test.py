import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from std_msgs.msg import String
from statemachine import StateMachine, State

class MyStateMachine(StateMachine):
    state_a = State(initial=True)
    state_b = State()
    state_c = State()
    trigger = (
                state_a.to(state_b,cond='condition_success') | 
                state_a.to(state_c,cond='condition_success2') | 
                state_a.to.itself(cond='condition_self') | 
                state_b.to(state_c) | 
                state_c.to(state_a))


class StateMachineNode(Node):
    def __init__(self):
        super().__init__('state_machine_node')
        self.myfsm = MyStateMachine(self)
        self.subscription = self.create_subscription(
            String,
            'state_transition',
            self.state_transition_callback,
            10)

    def condition_success(self):
        return self.new_state == 'StateA'
    def condition_success2(self):
        return self.new_state == 'StateB'
    def condition_self(self):
        return self.new_state == 'nix'

    def state_transition_callback(self, msg):
        self.new_state = msg.data
        if self.new_state in ['StateA', 'StateB', 'StateC']:
            self.myfsm.send('trigger')
            self.get_logger().info(f'Transitioning trigger got it  {self.new_state}')

    def on_enter_state_a(self):
        self.get_logger().info('Executing function for StateA')
        
    def on_enter_state_b(self):
        self.get_logger().info('Executing function for StateB')

    def on_enter_state_c(self):
        self.get_logger().info('Executing function for StateC')

def main(args=None):
    rclpy.init(args=args)
    node = StateMachineNode()
    #fsm = MyStateMachine(node)
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    try:
        node.get_logger().info('State machine node running')
        executor.spin()

    except KeyboardInterrupt:
        node.get_logger().info('Shutting down')
        rclpy.shutdown()

if __name__ == '__main__':
    main()
