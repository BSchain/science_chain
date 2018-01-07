# science_chain
chain for science data sharing

## (1) block文件
>基本函数: new_block（产生新的块）、to_dict（返回块对应的dict）、save_block(保存至文件),

>考虑字段有: index(块高度)、timestamp(时间戳)、prev_hash(前一块的hash)、nonce(关键字进行pow验证)、current_transactions（当前所有的交易）
## (2) chain文件
>由于随着交易进行，chain会逐渐增长，目前没有打算直接保存在内存中。至于对chain合法性的验证，可以通过依次读取block文件，进行hash值校验以及pow证明；

>基本函数有: find_block_by_index、 add_block
>考虑字段有: chain_length（长度）、chain（所有的block构成）
## (3) coin文件

作为transaction的一个属性，用于记录信用度是否花费，（这里没有想太明白）
## (4) transaction文件

>通过action关键字区分不同的操作。需要考虑的因素较多，login、upload、buy、download等，

>目前字段有: data_uuid、action、 buyer 、 seller （这个名字可以改改）、coin_in、coin_out

>主要函数:new_transaction等

## (5) config文件

保存block存储的文件目录、保存当前挖矿的难度系数、保存transaction以及block的字段类型等

## (6) utils 文件
常用的函数实现。
>hash(block) 根据传递的block生成hash值、chain_valid 验证chain的合法性、proof_of_work（pow函数实现）

## (7) node文件

用于其他网络节点的注册，函数目前未定义

## (8) cli文件

设置全局参数，尚未定义具体参数

## (9) mine文件

挖矿服务的主要函数。（主要通过传递的current_transactions 生成新的block）