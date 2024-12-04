import { HttpClient,HttpHeaders } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { map, Observable } from 'rxjs';
import { Fruit } from '../type/benefit';

@Injectable({
  providedIn: 'root'
})
export class BenefitsService {

  httpClient = inject(HttpClient);

 
  getBenefits(name: string) {
    return this.httpClient.get<Fruit[]>('http://localhost:3000/fruits?name='+name)
      
   
  }
  predictFruit(image: File): Observable<any> {
    const formData = new FormData();
    formData.append('file', image);
  
    // No need to set custom headers for FormData; Angular handles it automatically
    return this.httpClient.post<any>('http://127.0.0.1:5000/predict', formData);
  }
  constructor() { }
}
