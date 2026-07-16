# Git 双远程同步命令速查表（gitee 主仓库 + github 镜像）

## 核心原则

**只对 gitee 做 pull/rebase，github 只做镜像备份，永远强推不拉取。**
两个远程各自独立 rebase 会导致 commit hash 不一致，反复出现 diverged。

---

## 一次性修复当前分叉

```bash
git push gitee main --force-with-lease
```

两边内容其实一致，只是 commit hash 不同，强推同步即可。
用 `--force-with-lease` 而不是 `--force`，防止意外覆盖别人新推的内容。

---

## 日常提交流程

```bash
git add .
```

把所有修改加入暂存区（准备提交）

```bash
git commit -m "本次学习内容"
```

生成一次版本记录

```bash
git pull gitee main --rebase
```

只对主仓库 gitee 拉取并变基，把本地提交接到远程最新提交后面

> 如果冲突：手动改冲突文件 → `git add .` → `git rebase --continue`

```bash
git push gitee main
```

推送主仓库

```bash
git push github main --force-with-lease
```

直接强推镜像到 github，**不 pull、不 rebase**，github 内容始终等于 gitee

---

## 查看状态（可选）

```bash
git status
```

---

## 注意事项

| 内容                                                                                                                   | 优先级             |
| ---------------------------------------------------------------------------------------------------------------------- | ------------------ |
| 只对 gitee pull/rebase，github 只强推镜像                                                                              | **必须掌握** |
| 不要在 github 网页端直接改文件，不要在别的设备单独 clone github 开发，否则会产生本地没有的独立提交，强推时会被覆盖丢失 | **必须掌握** |
| rebase 冲突的手动解决流程                                                                                              | 了解即可           |
| 更复杂的多仓库同步方案（mirror push、CI 自动同步）                                                                     | 暂时不学           |
