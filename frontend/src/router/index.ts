import { createRouter, createWebHistory } from 'vue-router'

import Overview from '@/views/Overview.vue'
const Schema = () => import('@/views/schema/index.vue')
const Template = () => import('@/views/template/index.vue')
const Job = () => import('@/views/job/index.vue')
const Score = () => import('@/views/score/index.vue')
const Compare = () => import('@/views/compare/index.vue')
const Pipeline = () => import('@/views/pipeline/index.vue')
const Proxy = () => import('@/views/proxy/index.vue')
const Antibot = () => import('@/views/antibot/index.vue')
const Rate = () => import('@/views/rate/index.vue')
const Retry = () => import('@/views/retry/index.vue')
const Delta = () => import('@/views/delta/index.vue')
const Cleanse = () => import('@/views/cleanse/index.vue')
const Storage = () => import('@/views/storage/index.vue')
const Log = () => import('@/views/log/index.vue')
const Schedule = () => import('@/views/schedule/index.vue')
const Monitor = () => import('@/views/monitor/index.vue')
const Export = () => import('@/views/export/index.vue')
const Auth = () => import('@/views/auth/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'overview', component: Overview },
    { path: '/schema', name: 'schema', component: Schema },
    { path: '/template', name: 'template', component: Template },
    { path: '/job', name: 'job', component: Job },
    { path: '/score', name: 'score', component: Score },
    { path: '/compare', name: 'compare', component: Compare },
    { path: '/pipeline', name: 'pipeline', component: Pipeline },
    { path: '/proxy', name: 'proxy', component: Proxy },
    { path: '/antibot', name: 'antibot', component: Antibot },
    { path: '/rate', name: 'rate', component: Rate },
    { path: '/retry', name: 'retry', component: Retry },
    { path: '/delta', name: 'delta', component: Delta },
    { path: '/cleanse', name: 'cleanse', component: Cleanse },
    { path: '/storage', name: 'storage', component: Storage },
    { path: '/log', name: 'log', component: Log },
    { path: '/schedule', name: 'schedule', component: Schedule },
    { path: '/monitor', name: 'monitor', component: Monitor },
    { path: '/export', name: 'export', component: Export },
    { path: '/auth', name: 'auth', component: Auth },
  ],
})

export default router
