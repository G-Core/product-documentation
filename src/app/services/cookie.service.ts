import { Inject, Injectable } from '@angular/core';
import { DOCUMENT } from '@angular/common';

const ONE_YEAR = 60 * 60 * 24 * 365;

@Injectable({
    providedIn: 'root',
})
export class CookieService {
    constructor(@Inject(DOCUMENT) private document: Document) {}

    public setCookie(name: string, value: string, maxAgeSeconds: number = ONE_YEAR, domain?: string): void {
        this.document.cookie = `${name}=${value};max-age=${maxAgeSeconds * 1000};path=/;secure=true;${
            domain ? `domain=${domain}` : ''
        }`;
    }

    public getCookie(name: string): string | null {
        const cookies = this.document.cookie.split(';');
        const cookie = cookies.find((c) => c.trim().startsWith(`${name}=`));
        if (!cookie) {
            return null;
        }
        return cookie.split('=')[1];
    }

    public deleteCookie(name: string): void {
        this.setCookie(name, '', -1);
    }
}
