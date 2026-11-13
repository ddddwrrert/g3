# G3

G3 是包在 [Harness²](https://github.com/google-research/harness2) 外面的一层控制循环。模型权重和 Planner、Probe、Compose 的规则保持不动。跨任务留下的是单条编辑和方向的胜负，不是融合后的整份 harness。

`third_party/harness2` 是 Harness² 提交 `6868817518876de8fd170c6a8354daca273b6191` 的源码，未改，Apache-2.0。

直接调用的是：

- `harness2.core.tree`：组件树的校验、diff、多样性
- `harness2.core.library.Library`：没有 `cue`、`lesson`、`evidence` 就不写入
- `harness2.core.selection.assign_ids`：选择器只看匿名交付物
- `harness2.core.ledger.Ledger`：记录每一次运行
- `harness2.core.context.assert_tree_has_no_grader_verdicts`：评分结果不写进 harness

这一层做的收口：

- 每个方向只改一件事，同一种改动不重复 Probe
- 领先者再跑一次，两次行为不一致就不采纳
- 合并稿先跑通才有资格被选中。失败后逐条拿掉再跑，只记下那一对改动
- 下一道任务从基础 harness 开始。库里没有签名三元组的整份树不会被套用
- 三元组要被这次采用，并且没有冲掉已经生效的行为，才标成 confirmed
- 没通过的 Probe 会带着改动写入 `hindsight.jsonl`，同一类失败出现时重新提案
- 赢过的方向排在没试过的方向前面

AHC 适配器在 `g3/ahc.py`。它不自带题库。设置 `ORGANON_ROOT` 指向含有 `tasks/ale_bench` 的目录后才能读 baseline。

运行：

```bash
python -m g3
python -m unittest tests.test_closed_loop
```

需要 Python 3.12 或 3.13。
