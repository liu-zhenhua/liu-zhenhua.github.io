# 内容来源与验证

核验日期：2026-10-12。

## 用户确认

- 姓名：Zhenhua Liu（刘振华）。
- 职位及单位：Senior Researcher, Microsoft Research Asia (MSRA)。
- 联系邮箱：zhenhualiu@microsoft.com。
- Google Scholar：https://scholar.google.com/citations?user=bihqxP4AAAAJ&hl=zh-CN&oi=ao 。
- 当前展示的 5 篇论文均属于本人。
- 最终主页地址：https://liu-zhenhua.github.io/ 。

## 设计参考

参考 https://sicxu.github.io/ 的白底窄栏、简介与圆形头像、带配图的论文列表和主题筛选，独立实现页面结构与样式。未复制其个人照片、履历或论文。真实头像暂未提供，页面使用姓名缩写。

## 论文来源

| 论文 | 元数据及身份核验 |
| --- | --- |
| Continue or Replan? Bernoulli-Continuation Policy Learning for Adaptive Horizon Execution | [arXiv](https://arxiv.org/abs/2608.03483)、[项目页面](https://fleetfootwork.github.io/BCP/)。论文首页列出 MSRA 和用户提供的微软邮箱，项目页确认共同第一作者。 |
| A Survey on Vision Transformer | [Crossref](https://api.crossref.org/works/10.1109/TPAMI.2022.3152247)、[arXiv](https://arxiv.org/abs/2012.12556)。正式期刊信息是 IEEE TPAMI 45(1):87–110, 2023；arXiv 标题为 Visual Transformer，接受年份为 2022。页面使用正式期刊标题和出版年份。 |
| Instance-Aware Dynamic Neural Network Quantization | [CVF](https://openaccess.thecvf.com/content/CVPR2022/html/Liu_Instance-Aware_Dynamic_Neural_Network_Quantization_CVPR_2022_paper.html)、[官方代码](https://github.com/huawei-noah/Efficient-Computing/tree/master/Quantization/DynamicQuant)、[Yunhe Wang 主页](https://www.wangyunhe.site/)。官方代码原始实现由当前账号 liu-zhenhua 提交；合作者主页标注 Oral Presentation。 |
| Post-Training Quantization for Vision Transformer | [NeurIPS Proceedings](https://proceedings.neurips.cc/paper/2021/hash/ec8956637a99787bd197eacd77acce5e-Abstract.html)、论文原文及合作者主页。 |
| Pre-Trained Image Processing Transformer | [CVF](https://openaccess.thecvf.com/content/CVPR2021/html/Chen_Pre-Trained_Image_Processing_Transformer_CVPR_2021_paper.html)、[官方代码](https://github.com/huawei-noah/Pretrained-IPT)、论文原文及合作者主页。 |

图片的逐项来源见 [assets/images/SOURCES.md](assets/images/SOURCES.md)。Scholar 在本环境返回 HTTP 429，页面不声称覆盖其全部记录，也未填入无法核实的引用量。主页展示 Selected Publications 并链接 Scholar 的完整列表。

## 验证

- Chrome 检查 1440、768、390、320 像素宽度：无横向溢出，所有图片正常加载，无脚本或本地资源错误。
- 5 篇论文的分类、组合检索、无结果提示、重置和作者加粗均通过检查。
- 独立数据验证键盘操作、HTML 转义及年份排序；测试数据未进入发布页面。
- 禁用 JavaScript 仍可阅读全部论文。
- 站点包含 canonical、站点地图和 robots.txt；GitHub Actions 仅部署生成的 HTML、本地资源和站点元数据。
