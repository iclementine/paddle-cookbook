## 命名空间，这是什么，能吃吗？





1. `__init__(name_scope, dtype)` 是所有 Layer 的基类的 constructor 形式。 表示这个 Layer 将会置于这个命名空间。可以类比文件路径。比如说 `FC("/usr/local", other_parameters, dtype="float32")`, 就表示在 `/usr/local` 下建立一个 FC Layer （可以类比为一个文件夹）， 而这个文件夹的名字就是 `FC_0`, 这个是由它的 `classname` 和次序决定的。比如说再建立一个 `FC` layer，那么它的名字就是 `FC_1`。
2. Layer 如果包含 sublayer, 那么为了使得参数的层次反映 Layer 自身的 sublayer 结构。我们会把 sublayer 建立在 Layer 的命名空间里面。相当于在一个文件夹里面再建立一个文件夹。这反映在代码层面，比如说在一个 layer 里面建立一个 `FC` 作为其子层，这么写 `self.sub_module = FC(self.full_name(), other_parameters, dtype)` 就可以保持层次结构。