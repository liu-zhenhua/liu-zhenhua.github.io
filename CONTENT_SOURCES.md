# 内容核验记录

核验日期：2026-10-12。

## 已核实

- 用户提供的参考主页：https://sicxu.github.io/ 。已查看原始 HTML、CSS 和桌面浏览器截图，以白底窄栏、简介与圆形头像、带配图的论文卡片和主题筛选作为布局参考。
- 用户提供的 Google Scholar：https://scholar.google.com/citations?user=bihqxP4AAAAJ&hl=zh-CN&oi=ao 。页面中的 Scholar 链接保留同一用户 ID。
- 用户确认姓名为 Zhenhua Liu（刘振华）、单位为 MSRA、职位为 Senior Researcher，公开联系邮箱为 zhenhualiu@microsoft.com。页面将 MSRA 展开为 Microsoft Research Asia。
- 当前 GitHub 凭据通过 GitHub `/user` 接口确认登录为 `liu-zhenhua`，公开账号链接为 https://github.com/liu-zhenhua 。没有保存凭据到本项目。
- `https://github.com/zhliu` 是另一个已存在账号，`https://zhliu.github.io/` 当前返回 GitHub Pages 404。无法据此认定用户拥有该账号。
- BCP 原始论文首页列出 `Zhenhua Liu`、Microsoft Research Asia 及用户提供的 `zhenhualiu@microsoft.com`，因此可直接关联身份。原文：https://arxiv.org/pdf/2608.03483 。
- DynamicQuant 官方仓库的 [原始代码提交](https://github.com/huawei-noah/Efficient-Computing/commit/5467e78944b92f9137e709631ca83ad33f9c063b) 由当前账号 `liu-zhenhua` 创建，[项目 README](https://github.com/huawei-noah/Efficient-Computing/tree/master/Quantization/DynamicQuant) 明确列出论文与 Zhenhua Liu 的署名。该身份关联与 CVF 原文的作者记录一致。
- 四篇早期论文的作者姓名、北京大学/华为诺亚方舟实验室单位及合作者记录互相吻合。CVPR 2022 DynamicQuant 与 NeurIPS 2021 ViT-PTQ 的原文还列出相同的第一作者邮箱（旧邮箱仅用于核验，不作为主页联系邮箱）。IPT 和综述的原文也列出同一作者的北京大学及华为单位。结合官方代码记录，已将这 5 篇工作填入 `data/publications.json`，标题标为 Selected Publications。
- 综述的正式出版信息依据 Crossref：*A Survey on Vision Transformer*, IEEE TPAMI 45(1):87–110, 2023，DOI `10.1109/TPAMI.2022.3152247`。原 arXiv 标题使用 *Visual Transformer*，接受年份是 2022，与正式期刊年份不同。

## 尚未核实，不应作为公开履历发布

- 教育经历、研究方向、学术服务均未填写。Git 配置中的邮箱没有用作公开联系邮箱。
- 真实头像未提供；页面使用 `ZL` 字母图形，没有使用他人照片。
- Scholar 在本环境持续返回 HTTP 429；未能直接读取 Scholar 姓名、单位或论文。备用公开入口同样未得到有效 Scholar 内容。
- 尚不能核对 Scholar 的完整论文列表；页面展示上述 5 篇精选工作，并保留完整 Scholar 列表的链接。
- 站点地址按用户原始目标配置为 `https://zhliu.github.io/`，包含 canonical、站点地图和 robots.txt。实际发布仍需要 `zhliu` 账号权限，或用户明确改用当前账号的 `liu-zhenhua.github.io`。
- 再次查询 GitHub API 确认：当前账号仍为 `liu-zhenhua`；`zhliu/zhliu.github.io` 返回 404；当前凭据对 `zhliu/test` 的 `push`、`maintain` 和 `admin` 权限均为 false。现有权限无法在另一个个人账号下创建其用户主页仓库。

当前主要阻碍是目标账号的发布权限。真实头像、额外履历和更多论文可后续补充，不作为发布必需条件。

## 已完成的本地验证

- 正式页面与 5 篇论文候选预览均已使用 Chrome 检查 1440、768、390、320 像素宽度：无横向溢出，无页面脚本错误，无本地资源 HTTP 错误。
- 候选预览的全部论文图片加载成功；组合分类筛选与关键词检索正常。
- 应用 5 篇论文后再次检查正式页面：四种屏幕宽度无横向溢出，所有图片正常加载，筛选/搜索/无结果重置正常，禁用 JavaScript 仍可阅读全部 5 篇论文。姓名、邮箱、作者加粗、canonical 和站点地图均符合当前配置。
- 已生成并检查静态部署包 `../zhliu.github.io-site.zip`，包含页面、本地字体/图片、robots.txt、sitemap.xml 和 `.nojekyll`。没有包含凭据、测试样例或研究临时文件。
- 独立测试数据验证了无结果提示、重置、键盘操作、作者加粗、HTML 转义、年份排序，以及禁用 JavaScript 时仍可阅读论文。测试数据未进入正式页面。
- 这些检查证明页面实现可用，不代表最终域名已部署。
