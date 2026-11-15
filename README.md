# 网页内容语义抽取引擎

面向结构化、半结构化网页的语义标注、抽取规则配置、内容解析模板、质量评分、结果对比与解析链路编排的语义抽取引擎。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 语义标注 | `schema` | 标注配置 | 配置编号、目标域名、页面类型 |
| 解析模板 | `template` | 模板配置 | 模板编号、页面类型、字段列表 |
| 抽取任务 | `job` | 任务配置 | 任务编号、入口URL、解析模板 |
| 质量评分 | `score` | 评分规则 | 规则编号、目标字段、评分维度 |
| 结果对比 | `compare` | 对比方案 | 方案编号、基准结果、对照结果 |
| 解析链路 | `pipeline` | 链路步骤 | 步骤编号、步骤类型、输入源 |
| 代理调度 | `proxy` | 代理配置 | 配置编号、代理类型、代理地址 |
| 反爬对抗 | `antibot` | 对抗规则 | 规则编号、验证码类型、识别方案 |
| 频率控制 | `rate` | 频率规则 | 规则编号、目标域名、每秒上限 |
| 失败恢复 | `retry` | 恢复策略 | 策略编号、关联任务、最大重试 |
| 增量抽取 | `delta` | 增量配置 | 配置编号、目标站点、增量字段 |
| 内容清洗 | `cleanse` | 清洗规则 | 规则编号、目标字段、空值替换 |
| 结果存储 | `storage` | 存储配置 | 配置编号、输出路径、存储格式 |
| 抽取日志 | `log` | 日志记录 | 记录编号、关联任务、请求URL |
| 定时调度 | `schedule` | 调度计划 | 计划编号、关联任务、调度表达式 |
| 采集监控 | `monitor` | 监控指标 | 指标编号、关联站点、成功率阈值 |
| 数据导出 | `export` | 导出通道 | 通道编号、数据来源、目标系统 |
| 站点认证 | `auth` | 认证配置 | 配置编号、目标站点、认证方式 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。

领域：数据工程
子方向：数据采集、爬虫与RPA
