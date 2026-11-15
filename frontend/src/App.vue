<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">网页内容语义抽取引擎</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向结构化、半结构化网页的语义标注、抽取规则配置、内容解析模板、质量评分、结果对比与解析链路编排的语义抽取引擎。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "语义标注", path: "/schema" }, { label: "解析模板", path: "/template" }, { label: "抽取任务", path: "/job" }, { label: "质量评分", path: "/score" }, { label: "结果对比", path: "/compare" }, { label: "解析链路", path: "/pipeline" }, { label: "代理调度", path: "/proxy" }, { label: "反爬对抗", path: "/antibot" }, { label: "频率控制", path: "/rate" }, { label: "失败恢复", path: "/retry" }, { label: "增量抽取", path: "/delta" }, { label: "内容清洗", path: "/cleanse" }, { label: "结果存储", path: "/storage" }, { label: "抽取日志", path: "/log" }, { label: "定时调度", path: "/schedule" }, { label: "采集监控", path: "/monitor" }, { label: "数据导出", path: "/export" }, { label: "站点认证", path: "/auth" }]
</script>
