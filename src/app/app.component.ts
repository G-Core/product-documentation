import { Meta } from '@angular/platform-browser';
import { Component, Renderer2 } from '@angular/core';
import { NavigationEnd, Router } from '@angular/router';
import { ScullyRoute, ScullyRoutesService } from '@scullyio/ng-lib';
import { Observable, filter } from 'rxjs';
import config from '../config';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
})
export class AppComponent {
    public links$: Observable<Array<ScullyRoute>> = this.scully.available$;

    constructor(
        private scully: ScullyRoutesService,
        public router: Router,
        private renderer: Renderer2,
        private meta: Meta,
    ) {
        if (config.environment === 'preprod') {
            this.meta.addTag({ name: 'robots', content: 'noindex, nofollow' });
            this.meta.addTag({
                name: 'ahrefs-site-verification',
                content: '485c75b4075240e83007bc97f02920c7da086265822292d779184e3ff0bbda3a',
            });
        }

        router.events.pipe(filter((e) => e instanceof NavigationEnd)).subscribe(() => {
            let currentUrl = `https://gcore.com/docs${this.router.url}`;
            if (this.router.url === '/') {
                currentUrl = currentUrl.slice(0, -1);
            }
            this.updateCanonicalTag(currentUrl);
        });
    }

    private updateCanonicalTag(url: string): void {
        let tag = document.head.querySelector('link[data-canonical]');
        if (tag) {
            this.renderer.setAttribute(tag, 'href', url);
        } else {
            tag = this.renderer.createElement('link');
            this.renderer.setAttribute(tag, 'data-canonical', '');
            this.renderer.setAttribute(tag, 'rel', 'canonical');
            this.renderer.setAttribute(tag, 'href', url);
            this.renderer.appendChild(document.head, tag);
        }
    }
}
