import { Injectable } from '@angular/core';
import { marketingCookies, statisticCookies } from '../constants/analytics';

const ONE_YEAR = 1000 * 60 * 60 * 24 * 365;

export enum CookiesConsent {
    All = 'all',
    Marketing = 'marketing',
    Statistic = 'statistic',
    DeclineAll = 'decline_all',
}

@Injectable({
    providedIn: 'root',
})
export class AnalyticsService {
    public getCookies(): { [key: string]: string } {
        return document.cookie.split('; ').reduce((cookesMap: { [key: string]: string }, cookie: string) => {
            const [key, value] = cookie.split('=');
            if (key === '_ga') {
                cookesMap[key] = this.formatGaId(value);
            } else {
                cookesMap[key] = value;
            }
            return cookesMap;
        }, {});
    }

    public applyCookiesConsent(): boolean {
        const cookies = this.getCookies();
        const cookiesConsent = cookies.cookies_consent;
        if (cookiesConsent) {
            switch (cookiesConsent) {
                case CookiesConsent.All:
                    break;
                case CookiesConsent.DeclineAll:
                    marketingCookies.concat(statisticCookies).forEach((cookie) => this.disableCookie(cookie, cookies));
                    break;
                case CookiesConsent.Marketing:
                    statisticCookies.forEach((cookie) => this.disableCookie(cookie, cookies));
                    break;
                case CookiesConsent.Statistic:
                    marketingCookies.forEach((cookie) => this.disableCookie(cookie, cookies));
                    break;
            }
            return false;
        } else {
            return true;
        }
    }

    public setCookiesConsent(value: CookiesConsent): void {
        document.cookie = `cookies_consent=${value}; max-age=${ONE_YEAR}`;
        this.applyCookiesConsent();
    }

    private formatGaId(value: string): string {
        if (!value) {
            return '';
        }
        const firstDotIndex = value.indexOf('.');
        const secondDotIndex = value.indexOf('.', firstDotIndex + 1);
        return value.slice(secondDotIndex + 1);
    }

    private disableCookie(cookie: string, cookies: { [key: string]: string }): void {
        if (cookie.endsWith('*')) {
            const names = Object.keys(cookies).filter((cookieName) => cookieName.startsWith(cookie.replace('*', '')));
            names.forEach(
                (cookieName) =>
                    (document.cookie = `${cookieName}=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/; domain=${window.location.hostname}`),
            );
        }
        document.cookie = `${cookie}=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/; domain=${window.location.hostname}`;
    }
}
