import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, map, Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class GitHubAPIService {
  constructor(private http: HttpClient) {}

  getLastModifiedDateLabel(filePath: string): Observable<string> {
    return this.http
      .get<any>(
        `https://api.github.com/repos/G-Core/product-documentation/commits?path=${filePath}`
      )
      .pipe(
        catchError(() => of('')),
        map((commits) => {
          const modifiedDate = new Date(commits[0]?.commit?.author.date);
          const currentDate = new Date();

          if (isNaN(modifiedDate.getTime())) {
            return '';
          }

          const differenceInMinutes = Math.ceil(
            (+currentDate - +modifiedDate) / 1000 / 60
          );

          if (differenceInMinutes < 60) {
            return `Updated ${differenceInMinutes} minutes ago`;
          } else if (differenceInMinutes < 24 * 60) {
            return `Updated ${Math.floor(differenceInMinutes / 60)} hours ago`;
          } else if (differenceInMinutes < 24 * 60 * 30) {
            return `Updated ${Math.floor(
              differenceInMinutes / 60 / 24
            )} days ago`;
          } else if (differenceInMinutes < 24 * 60 * 365) {
            return `Updated ${Math.floor(
              differenceInMinutes / 60 / 24 / 30
            )} month ago`;
          } else {
            return `Updated ${Math.floor(
              differenceInMinutes / 60 / 24 / 365
            )} years ago`;
          }
        })
      );
  }
}
