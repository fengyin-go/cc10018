"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class SchemaEntry(BaseModel):
    """标注配置明细结构。"""

    field_0: str | None = None  # 配置编号
    field_1: str | None = None  # 目标域名
    field_2: str | None = None  # 页面类型
    field_3: str | None = None  # 标注字段
    field_4: str | None = None  # CSS选择器
    field_5: str | None = None  # 正则表达式
    field_6: str | None = None  # 提取方式
    field_7: str | None = None  # 优先级

class TemplateEntry(BaseModel):
    """模板配置明细结构。"""

    field_0: str | None = None  # 模板编号
    field_1: str | None = None  # 页面类型
    field_2: str | None = None  # 字段列表
    field_3: str | None = None  # 嵌套结构
    field_4: str | None = None  # 列表提取
    field_5: str | None = None  # 分页规则
    field_6: str | None = None  # 字符编码
    field_7: str | None = None  # 模板版本

class JobEntry(BaseModel):
    """任务配置明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 入口URL
    field_2: str | None = None  # 解析模板
    field_3: str | None = None  # 并发数
    field_4: str | None = None  # 请求间隔
    field_5: str | None = None  # 重试上限
    field_6: str | None = None  # 输出格式
    field_7: str | None = None  # 超时秒数

class ScoreEntry(BaseModel):
    """评分规则明细结构。"""

    field_0: str | None = None  # 规则编号
    field_1: str | None = None  # 目标字段
    field_2: str | None = None  # 评分维度
    field_3: str | None = None  # 权重配置
    field_4: str | None = None  # 阈值下限
    field_5: str | None = None  # 扣分项
    field_6: str | None = None  # 采样比例
    field_7: str | None = None  # 最终等级

class CompareEntry(BaseModel):
    """对比方案明细结构。"""

    field_0: str | None = None  # 方案编号
    field_1: str | None = None  # 基准结果
    field_2: str | None = None  # 对照结果
    field_3: str | None = None  # 对比字段
    field_4: str | None = None  # 容差阈值
    field_5: str | None = None  # 差异标记
    field_6: str | None = None  # 一致率目标
    field_7: str | None = None  # 报告输出

class PipelineEntry(BaseModel):
    """链路步骤明细结构。"""

    field_0: str | None = None  # 步骤编号
    field_1: str | None = None  # 步骤类型
    field_2: str | None = None  # 输入源
    field_3: str | None = None  # 处理逻辑
    field_4: str | None = None  # 输出目标
    field_5: str | None = None  # 依赖步骤
    field_6: str | None = None  # 并行度
    field_7: str | None = None  # 失败策略

class ProxyEntry(BaseModel):
    """代理配置明细结构。"""

    field_0: str | None = None  # 配置编号
    field_1: str | None = None  # 代理类型
    field_2: str | None = None  # 代理地址
    field_3: str | None = None  # 地域标签
    field_4: str | None = None  # 并发上限
    field_5: str | None = None  # 冷却秒数
    field_6: str | None = None  # 连续失败
    field_7: str | None = None  # 切换策略

class AntibotEntry(BaseModel):
    """对抗规则明细结构。"""

    field_0: str | None = None  # 规则编号
    field_1: str | None = None  # 验证码类型
    field_2: str | None = None  # 识别方案
    field_3: str | None = None  # 触发条件
    field_4: str | None = None  # 等待时长
    field_5: str | None = None  # 重试上限
    field_6: str | None = None  # 降级策略
    field_7: str | None = None  # 规则状态

class RateEntry(BaseModel):
    """频率规则明细结构。"""

    field_0: str | None = None  # 规则编号
    field_1: str | None = None  # 目标域名
    field_2: str | None = None  # 每秒上限
    field_3: str | None = None  # 并发窗口
    field_4: str | None = None  # 令牌速率
    field_5: str | None = None  # 惩罚系数
    field_6: str | None = None  # 冷却秒数
    field_7: str | None = None  # 优先级

class RetryEntry(BaseModel):
    """恢复策略明细结构。"""

    field_0: str | None = None  # 策略编号
    field_1: str | None = None  # 关联任务
    field_2: str | None = None  # 最大重试
    field_3: str | None = None  # 退避算法
    field_4: str | None = None  # 初始等待
    field_5: str | None = None  # 最大等待
    field_6: str | None = None  # 可重试码
    field_7: str | None = None  # 死信通道

class DeltaEntry(BaseModel):
    """增量配置明细结构。"""

    field_0: str | None = None  # 配置编号
    field_1: str | None = None  # 目标站点
    field_2: str | None = None  # 增量字段
    field_3: str | None = None  # 当前水位
    field_4: str | None = None  # 回退步数
    field_5: str | None = None  # 批次上限
    field_6: str | None = None  # 去重窗口
    field_7: str | None = None  # 重跑开关

class CleanseEntry(BaseModel):
    """清洗规则明细结构。"""

    field_0: str | None = None  # 规则编号
    field_1: str | None = None  # 目标字段
    field_2: str | None = None  # 空值替换
    field_3: str | None = None  # 标签清除
    field_4: str | None = None  # 空白过滤
    field_5: str | None = None  # 编码转换
    field_6: str | None = None  # 截断长度
    field_7: str | None = None  # 规则版本

class StorageEntry(BaseModel):
    """存储配置明细结构。"""

    field_0: str | None = None  # 配置编号
    field_1: str | None = None  # 输出路径
    field_2: str | None = None  # 存储格式
    field_3: str | None = None  # 分区字段
    field_4: str | None = None  # 压缩算法
    field_5: str | None = None  # 保留天数
    field_6: str | None = None  # 覆写模式
    field_7: str | None = None  # 校验摘要

class LogEntry(BaseModel):
    """日志记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 关联任务
    field_2: str | None = None  # 请求URL
    field_3: str | None = None  # 开始时间
    field_4: str | None = None  # 耗时毫秒
    field_5: str | None = None  # 状态码
    field_6: str | None = None  # 提取行数
    field_7: str | None = None  # 错误信息

class ScheduleEntry(BaseModel):
    """调度计划明细结构。"""

    field_0: str | None = None  # 计划编号
    field_1: str | None = None  # 关联任务
    field_2: str | None = None  # 调度表达式
    field_3: str | None = None  # 时区
    field_4: str | None = None  # 最大并行
    field_5: str | None = None  # 超时终止
    field_6: str | None = None  # 依赖检查
    field_7: str | None = None  # 通知策略

class MonitorEntry(BaseModel):
    """监控指标明细结构。"""

    field_0: str | None = None  # 指标编号
    field_1: str | None = None  # 关联站点
    field_2: str | None = None  # 成功率阈值
    field_3: str | None = None  # 延迟阈值
    field_4: str | None = None  # 错误率告警
    field_5: str | None = None  # 检测频率
    field_6: str | None = None  # 告警级别
    field_7: str | None = None  # 通知渠道

class ExportEntry(BaseModel):
    """导出通道明细结构。"""

    field_0: str | None = None  # 通道编号
    field_1: str | None = None  # 数据来源
    field_2: str | None = None  # 目标系统
    field_3: str | None = None  # 导出格式
    field_4: str | None = None  # 传输协议
    field_5: str | None = None  # 频率限制
    field_6: str | None = None  # 加密开关
    field_7: str | None = None  # 完整性校验

class AuthEntry(BaseModel):
    """认证配置明细结构。"""

    field_0: str | None = None  # 配置编号
    field_1: str | None = None  # 目标站点
    field_2: str | None = None  # 认证方式
    field_3: str | None = None  # 凭证标识
    field_4: str | None = None  # 有效期天
    field_5: str | None = None  # 会话保持
    field_6: str | None = None  # 刷新触发
    field_7: str | None = None  # 失效告警
