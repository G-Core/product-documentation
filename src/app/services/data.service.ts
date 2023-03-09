import {Injectable} from "@angular/core";
import {Subject} from "rxjs";

@Injectable()
export class DataService {
  constructor() { }

  private emitChangeSource = new Subject<any>();

  changeEmitted$ = this.emitChangeSource.asObservable();

  emitChange(event: any) {
    this.emitChangeSource.next(event);
  }
}
