package ejemplohash;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import java.util.Objects;

/**
 * 
 * @author Dimitri Medina Novelo
 */
public class Maestro {
    private int idMaestro;
    private String Nombre;
    public static int Tam;

    public Maestro(int idMaestro, String Nombre) {
        this.idMaestro = idMaestro;
        this.Nombre = Nombre;
    }

    public int getIDMaestro() {
        return idMaestro;
    }

    public void setIDMaestro(int idMaestro) {
        this.idMaestro = idMaestro;
    }

    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }

    @Override
    public int hashCode() {
        return idMaestro % Tam;
    }
    
   
    
    
    
}