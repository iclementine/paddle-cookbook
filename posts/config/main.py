import configargparse
from configargparse import ArgumentParser, Namespace

class MyModel(object):
    
    # 标准式 constructor
    def __init__(self, num_layers, hidden_size):
        self.num_layers = num_layers
        self.hidden_size = hidden_size
    
    # 把标准 constructor 需要的东西添加到 argument parser 使得它可以支持命令行参数
    # 同时这些参数的定义和被使用处不要相隔太远， 不要在 maker_parser 里面写一大串面条
    # 而是开局一个 parser, 谁需要， 谁定义， 这样就有模板， 而不是像 config parser 一样找不到
    # config 的定义， 结果全靠配置文件， 其实这个思想有点像 click 诶， 怎么办， 而且它那样写更自由
    # init 注册 init 的参数， forward 注册 forward 的参数， 可以吗？ 但是 click 那样写
    # 调用的时候就省略了参数， 有点黑魔法， 对于包装了 forward 的 run 来说也不是很合适， 因为 
    # click 装饰函数， 但是又不能直接去装饰父类的 __call__ 所以还是还是只来 constructor 
    # 比较好
    @staticmethod
    def add_arg(parser: ArgumentParser):
        g = parser.add_argument_group("My Model config")
        g.add_argument("--num_layers", type=int, help="number of layers")
        g.add_argument("--hidden_size", type=int, help="size of hidden layers")

    # 不需要什么 Config 类， 一切就在往 parser 中添加的那些 key 中处理了
    @classmethod
    def from_spec(cls, spec: Namespace):
        args = spec.num_layers, spec.hidden_size
        return cls(*args)

if __name__ == "__main__":
    parser = ArgumentParser(description="What does this file do?")
    parser.add_argument("-e", "--epoch", type=int, help="epochs to train the model")
    
    # model config
    parser.add('-c', '--config', required=True, is_config_file=True, help='config file path')
    MyModel.add_arg(parser)
    
    args, rest = parser.parse_known_args()
    model = MyModel.from_spec(args)
    print(args)
    
    


