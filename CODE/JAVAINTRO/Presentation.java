/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.aimosta.firstproject;

/**
 *
 * @author AMINA
 */
public class Presentation {
public String prName;
public String prType;
public int prNumber;


    public Presentation(String name, String type, int number){
        this.prName = name;
        this.prType = type;
        this.prNumber = number;
    }
    
 
 public void present(){
     System.out.println(this.prName);
     System.out.println(this.prType);
     System.out.println(this.prNumber);
 }
    
}
