# Zhenhua Liu · Academic homepage

参考 [Sicheng Xu 的主页](https://sicxu.github.io/) 独立实现的静态学术主页：简介、头像、论文配图、分类筛选、搜索和移动端布局。没有运行时框架或第三方脚本，关闭 JavaScript 仍可阅读全部论文；字体保存在本地。

## 本地查看

```bash
cd /home/liuzhenhua/personal/zhliu.github.io
python3 scripts/build.py --output _site
python3 -m http.server 8000 --bind 127.0.0.1 --directory _site
```

打开 `http://localhost:8000`。在远程开发环境中可转发 8000 端口。也可以运行 `python3 scripts/build.py` 后直接打开根目录的 `index.html`。

## 更新内容

- `data/profile.json`：姓名、中英文姓名、简介、邮箱、头像路径、研究兴趣和个人链接。
- `data/publications.json`：论文条目，按年份倒序生成，分类由条目自动提取。
- `assets/images/`：头像与论文图片。
- `assets/style.css`：版式和配色。
- `templates/index.html`：页面结构。根目录 `index.html` 为生成文件，请先修改数据或模板，再重新构建。

论文条目的结构如下（示例仅说明字段，不是个人论文）：

```json
{
  "title": "Paper title",
  "short_title": "Short title",
  "authors": ["First Author", "Zhenhua Liu", "Last Author"],
  "venue": "Conference name",
  "year": 2026,
  "category": "Research topic",
  "image": "assets/images/paper.jpg",
  "image_alt": "A description of the paper figure",
  "links": [
    {"label": "Paper", "url": "https://example.com/paper"},
    {"label": "Code", "url": "https://github.com/owner/repository"}
  ]
}
```

`image` 和 `image_alt` 可省略；缺少图片时展示 `short_title` 或会议名称。作者与 `profile.json` 的 `name` 匹配时自动加粗。列表第一条链接同时作为标题和图片的跳转链接。不要将示例域名用于真实内容。

`profile.json` 中的 `sections` 可以添加教育经历、学术服务等已确认信息：每项包含 `title` 和字符串数组 `items`。未提供的栏目不显示。没有真实头像时显示姓名缩写，没有论文数据时提供 Scholar 入口。

## GitHub Pages

仓库内已包含 `.github/workflows/pages.yml`：推送到 `main` 后用 Python 构建，再通过 GitHub Actions 部署 `_site`。只上传生成的静态页面与素材。

1. 确认最终 GitHub 用户名，将仓库命名为 `<username>.github.io`。
2. 将 `data/profile.json` 的 `site_url` 设为 `https://<username>.github.io/`。构建时会生成 canonical、站点地图和 robots.txt。
3. 在仓库 **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**。
4. 推送 `main`，等待 `Deploy academic homepage` 成功。

`zhliu.github.io` 是 GitHub 用户 `zhliu` 对应的用户站点。当前环境登录的是 `liu-zhenhua`，其用户站点对应 `liu-zhenhua.github.io`。在 `liu-zhenhua` 账号下创建名为 `zhliu.github.io` 的仓库不会获得 `zhliu.github.io` 域名。

## 当前内容来源与待补信息

见 [CONTENT_SOURCES.md](CONTENT_SOURCES.md)。页面已填入用户确认的姓名、职位和邮箱，以及通过论文原文、合作者主页和官方代码仓库交叉核实的 5 篇精选论文。真实头像未提供，暂使用姓名缩写。

站点已按用户指定的 `https://zhliu.github.io/` 配置，尚未部署；当前登录账号 `liu-zhenhua` 缺少目标账号 `zhliu` 的发布权限。若最终改用 `liu-zhenhua.github.io`，需同时修改仓库名称和 `site_url`，然后重新构建。

Poppins 字体按 SIL Open Font License 发行，授权文本保存在 `assets/fonts/OFL.txt`。网站未复制参考主页的个人照片、论文、履历或分析脚本。
