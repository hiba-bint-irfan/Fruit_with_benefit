import { Component, inject, Input} from '@angular/core';
import { FormsModule } from '@angular/forms';
import axios from 'axios';
import { BenefitsService } from '../../benefits.service';
import { NgFor, NgIf } from '@angular/common';
import { Fruit } from '../../../type/benefit';


@Component({
  selector: 'app-benefit',
  imports: [FormsModule, NgIf,NgFor],
  templateUrl: './benefit.component.html',
  styleUrl: './benefit.component.scss'
})
export class BenefitComponent {
  @Input() fruitName: string = ''; // Input property to receive the fruit name
  fruitBenefits: Fruit[]=[];
  errorMessage: string = '';
  showMore: boolean = false;


 Benefitservice=inject(BenefitsService);
 ngOnInit(){
  this.Benefitservice.getBenefits(this.fruitName).subscribe(result=>
  {
    this.fruitBenefits=result
   console.log(this.fruitBenefits[0].name)
    
    console.log(this.fruitName)
    console.log(result)
    
  }
  )
 }
  
}
