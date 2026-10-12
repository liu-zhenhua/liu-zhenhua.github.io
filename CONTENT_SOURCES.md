# 内容核验记录

核验日期：2026-10-12。

## 已核实

- 用户提供的参考主页：https://sicxu.github.io/ 。已查看原始 HTML、CSS 和桌面浏览器截图，以白底窄栏、简介与圆形头像、带配图的论文卡片和主题筛选作为布局参考。
- 用户提供的 Google Scholar：https://scholar.google.com/citations?user=bihqxP4AAAAJ&hl=zh-CN&oi=ao 。页面中的 Scholar 链接保留同一用户 ID。
- 用户确认姓名为 Zhenhua Liu（刘振华）、单位为 MSRA、职位为 Senior Researcher，公开联系邮箱为 zhenhualiu@microsoft.com。页面将 MSRA 展开为 Microsoft Research Asia。
- 当前 GitHub 凭据通过 GitHub `/user` 接口确认登录为 `liu-zhenhua`，公开账号链接为 https://github.com/liu-zhenhua 。没有保存凭据到本项目。
- `https://github.com/zhliu` 是另一个已存在账号，`https://zhliu.github.io/` 当前返回 GitHub Pages 404。无法据此认定用户拥有该账号。

## 尚未核实，不应作为公开履历发布

- 教育经历、研究方向、学术服务均未填写。Git 配置中的邮箱没有用作公开联系邮箱。
- 真实头像未提供；页面使用 `ZL` 字母图形，没有使用他人照片。
- Scholar 在本环境持续返回 HTTP 429；未能直接读取 Scholar 姓名、单位或论文。备用公开入口同样未得到有效 Scholar 内容。
- 从 [Jiaolong Yang 的主页](https://yangjiaolong.github.io/)、[BCP 项目页](https://fleetfootwork.github.io/BCP/)、[Yunhe Wang 的主页](https://www.wangyunhe.site/) 找到 5 篇候选论文，已向用户请求确认归属。`data/publications.json` 暂保持空数组；候选数据保存在 `../homepage-review/publications.candidates.json`，含 5 篇论文的独立预览及桌面/手机截图保存在 `../homepage-review/`。确认后可应用相应条目。8002 端口运行的是该预览的临时副本。
- 候选论文的标题、作者、年份已分别对照 arXiv、CVF、NeurIPS 和 Crossref 原始记录。Transformer 综述的正式出版信息为 *A Survey on Vision Transformer*, IEEE TPAMI 45(1):87–110, 2023，DOI `10.1109/TPAMI.2022.3152247`。原 arXiv 标题使用 *Visual Transformer*，接受年份是 2022，与正式期刊年份不同。
- 最终域名待用户选择：`zhliu.github.io` 需要对应账号权限；当前账号可使用 `liu-zhenhua.github.io`。`site_url` 暂留空，避免生成错误 canonical。

补充并确认这些资料后，应重新构建、核验真实论文链接与页面截图，再部署最终站点。

## 已完成的本地验证

- 正式页面与 5 篇论文候选预览均已使用 Chrome 检查 1440、768、390、320 像素宽度：无横向溢出，无页面脚本错误，无本地资源 HTTP 错误。
- 候选预览的全部论文图片加载成功；组合分类筛选与关键词检索正常。
- 独立测试数据验证了无结果提示、重置、键盘操作、作者加粗、HTML 转义、年份排序，以及禁用 JavaScript 时仍可阅读论文。测试数据未进入正式页面。
- 这些检查证明页面实现可用，不代表最终域名已部署或候选论文已确认归属。
