import { Meta, Title } from '@angular/platform-browser';
import { Component, OnInit, Renderer2 } from '@angular/core';
import { ActivatedRoute, ActivatedRouteSnapshot, NavigationEnd, Router } from '@angular/router';
import { ScullyRoute, ScullyRoutesService } from '@scullyio/ng-lib';
import { filter, map, Observable, switchMap } from 'rxjs';
import config from '../config';
import { sourcebuster } from './utils/sourcebuster';
import { AnalyticsService } from './services/analitycs.service';

const defaultDescription = 'Gcore | Global Hosting, CDN, Edge and Cloud Services';
const defaultTitle = 'Product Documentation';

const defineDomain = (): string => {
    switch (config.environment) {
        case 'prod':
            return 'gcore.com';
        case 'preprod':
            return 'preprod.world';
        default:
            return '';
    }
};

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
})
export class AppComponent implements OnInit {
    public links$: Observable<Array<ScullyRoute>> = this.scully.available$;

    public showCookieModal: boolean;

    constructor(
        private scully: ScullyRoutesService,
        public router: Router,
        private renderer: Renderer2,
        private activatedRoute: ActivatedRoute,
        private meta: Meta,
        private readonly titleService: Title,
        private analitycsService: AnalyticsService,
    ) {
        if (config.environment === 'preprod') {
            this.meta.addTag({ name: 'robots', content: 'noindex, nofollow' });
            this.meta.addTag({
                name: 'ahrefs-site-verification',
                content: '485c75b4075240e83007bc97f02920c7da086265822292d779184e3ff0bbda3a',
            });
        }

        router.events
            .pipe(
                filter((e) => e instanceof NavigationEnd),
                switchMap(() => this.links$),
                map((links) => links.find((link) => link.route === this.router.url)),
            )
            .subscribe((link) => {
                const lastChildRouteSnapshot: ActivatedRouteSnapshot = this.getLastChildRouteSnapshot();

                const title = link?.pageTitle || lastChildRouteSnapshot.data.title || defaultTitle;
                const description =
                    link?.pageDescription || lastChildRouteSnapshot.data.description || defaultDescription;

                this.titleService.setTitle(title);

                this.meta.updateTag({
                    name: 'description',
                    content: description,
                });
                this.meta.updateTag({ name: 'og:description', content: description });

                let currentUrl = `https://gcore.com/docs${this.router.url}`;
                if (this.router.url === '/') {
                    currentUrl = currentUrl.slice(0, -1);
                }
                this.updateCanonicalTag(currentUrl);
            });
    }

    public ngOnInit(): void {
        this.setUTMCookie();

        if (!window.sessionStorage.getItem('fontPreloaded')) {
            setTimeout(() => {
                const link = document.createElement('link');
                link.setAttribute('rel', 'stylesheet');
                link.setAttribute('href', 'https://static.gcore.pro/fonts/inter/index.css');
                document.head.appendChild(link);
            }, 2000);
            window.sessionStorage.setItem('fontPreloaded', 'true');
        }

        this.showCookieModal = this.analitycsService.applyCookiesConsent();
    }

    public closeCookiesModal(): void {
        this.showCookieModal = false;
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

    private getLastChildRouteSnapshot(): ActivatedRouteSnapshot {
        let child: ActivatedRoute = this.activatedRoute.firstChild;
        let snapshot: ActivatedRouteSnapshot;
        while (child) {
            if (child.firstChild) {
                child = child.firstChild;
            } else {
                snapshot = child.snapshot;
                child = null;
            }
        }
        return snapshot;
    }

    private setUTMCookie(): void {
        sourcebuster.init({
            domain: defineDomain(),
        });
    }
}
