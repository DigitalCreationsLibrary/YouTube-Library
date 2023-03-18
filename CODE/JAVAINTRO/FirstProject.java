/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.aimosta.firstproject;

/**
 *
 * @author AMINA
 */
public class FirstProject {
    public static String name="First";
    public static String type="Project";
    public static int number=1;

    public static void main(String[] args) {
        Presentation pr = new Presentation(FirstProject.name, FirstProject.type, FirstProject.number);
        pr.present();
    }
    

}
