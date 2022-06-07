import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DocumentationComponent } from './components/documentation/documentation.component';
import { HomeComponent } from './components/home/home.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  {
    path: `documentation/cdn-dns`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/video-streaming`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/cloud-computing`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/containers`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/servers`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/security`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/cloud-storage`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/infrastructure`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/hybrid-cloud`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/monitoring`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/custom-services`,
    component: DocumentationComponent,
  },
  {
    path: `documentation/cdn-dns/:title`,
    children: [
      {
        path: '**',
        component: DocumentationComponent,
      },
    ],
    component: DocumentationComponent,
  },
  {
    path: `documentation/video-streaming/:title`,
    children: [
      {
        path: '**',
        component: DocumentationComponent,
      },
    ],
    component: DocumentationComponent,
  },
  {
    path: `documentation/cloud-computing/:title`,
    children: [
      {
        path: '**',
        component: DocumentationComponent,
      },
    ],
    component: DocumentationComponent,
  },
  {
    path: `documentation/containers/:title`,
    children: [
      {
        path: '**',
        component: DocumentationComponent,
      },
    ],
    component: DocumentationComponent,
  },
  {
    path: `documentation/servers/:title`,
    children: [
      {
        path: '**',
        component: DocumentationComponent,
      },
    ],
    component: DocumentationComponent,
  },
  {
    path: `documentation/security/:title`,
    children: [
      {
        path: '**',
        component: DocumentationComponent,
      },
    ],
    component: DocumentationComponent,
  },
  {
    path: `documentation/cloud-storage/:title`,
    children: [
      {
        path: '**',
        component: DocumentationComponent,
      },
    ],
    component: DocumentationComponent,
  },
  {
    path: `documentation/infrastructure/:title`,
    children: [
      {
        path: '**',
        component: DocumentationComponent,
      },
    ],
    component: DocumentationComponent,
  },
  {
    path: `documentation/hybrid-cloud/:title`,
    children: [
      {
        path: '**',
        component: DocumentationComponent,
      },
    ],
    component: DocumentationComponent,
  },
  {
    path: `documentation/monitoring/:title`,
    children: [
      {
        path: '**',
        component: DocumentationComponent,
      },
    ],
    component: DocumentationComponent,
  },
  {
    path: `documentation/custom-services/:title`,
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
      scrollOffset: [0, 110],
    }),
  ],
  exports: [RouterModule],
})
export class AppRoutingModule {}
