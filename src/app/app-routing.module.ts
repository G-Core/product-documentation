import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DocumentationComponent } from './components/documentation/documentation.component';
import { HomeComponent } from './components/home/home.component';
import { HEADER_HEIGHT } from './constants';

const routes: Routes = [
    { path: '', component: HomeComponent },
    {
        path: `documentation/web-security`,
        component: DocumentationComponent,
    },
    {
        path: `documentation/streaming`,
        component: DocumentationComponent,
    },
    {
        path: `documentation/server-protection`,
        component: DocumentationComponent,
    },
    {
        path: `documentation/storage`,
        component: DocumentationComponent,
    },
    {
        path: `documentation/hosting`,
        component: DocumentationComponent,
    },
    {
        path: `documentation/dns`,
        component: DocumentationComponent,
    },
    {
        path: `documentation/cloud`,
        component: DocumentationComponent,
    },
    {
        path: `documentation/cdn`,
        component: DocumentationComponent,
    },
    {
        path: `documentation/reseller-support`,
        component: DocumentationComponent,
    },
    {
        path: `documentation/account-settings`,
        component: DocumentationComponent,
    },
    {
        path: `documentation/web-security/:title`,
        children: [
            {
                path: '**',
                component: DocumentationComponent,
            },
        ],
        component: DocumentationComponent,
    },
    {
        path: `documentation/streaming/:title`,
        children: [
            {
                path: '**',
                component: DocumentationComponent,
            },
        ],
        component: DocumentationComponent,
    },
    {
        path: `documentation/server-protection/:title`,
        children: [
            {
                path: '**',
                component: DocumentationComponent,
            },
        ],
        component: DocumentationComponent,
    },
    {
        path: `documentation/storage/:title`,
        children: [
            {
                path: '**',
                component: DocumentationComponent,
            },
        ],
        component: DocumentationComponent,
    },
    {
        path: `documentation/hosting/:title`,
        children: [
            {
                path: '**',
                component: DocumentationComponent,
            },
        ],
        component: DocumentationComponent,
    },
    {
        path: `documentation/dns/:title`,
        children: [
            {
                path: '**',
                component: DocumentationComponent,
            },
        ],
        component: DocumentationComponent,
    },
    {
        path: `documentation/cloud/:title`,
        children: [
            {
                path: '**',
                component: DocumentationComponent,
            },
        ],
        component: DocumentationComponent,
    },
    {
        path: `documentation/cdn/:title`,
        children: [
            {
                path: '**',
                component: DocumentationComponent,
            },
        ],
        component: DocumentationComponent,
    },
    {
        path: `documentation/account-settings/:title`,
        children: [
            {
                path: '**',
                component: DocumentationComponent,
            },
        ],
        component: DocumentationComponent,
    },
    {
        path: `documentation/reseller-support/:title`,
        children: [
            {
                path: '**',
                component: DocumentationComponent,
            },
        ],
        component: DocumentationComponent,
    },
];

@NgModule({
    imports: [
        RouterModule.forRoot(routes, {
            useHash: false,
            anchorScrolling: 'enabled',
            scrollOffset: [0, HEADER_HEIGHT + 16],
        }),
    ],
    exports: [RouterModule],
})
export class AppRoutingModule {}
