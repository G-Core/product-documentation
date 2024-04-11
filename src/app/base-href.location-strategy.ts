import { Location, PathLocationStrategy } from '@angular/common';
import { Injectable } from '@angular/core';

@Injectable()
export class BaseHrefLocationStrategy extends PathLocationStrategy {
    public override prepareExternalUrl(url: string): string {
        const baseHref = this.getBaseHref();
        const extUrl = super.prepareExternalUrl(url);
        return baseHref === extUrl ? Location.stripTrailingSlash(extUrl) : extUrl;
    }
}
