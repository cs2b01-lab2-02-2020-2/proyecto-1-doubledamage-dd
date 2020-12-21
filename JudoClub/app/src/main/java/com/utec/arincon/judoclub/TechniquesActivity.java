package com.utec.arincon.judoclub;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class TechniquesActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_techniques);
    }


    public void openGoKyo(View view) {
        Intent intent = new Intent(TechniquesActivity.this, GoKyoActivity.class);
        startActivity(intent);
    }

    public void openNeWaza(View view) {
        Intent intent = new Intent(TechniquesActivity.this, NeWazaActivity.class);
        startActivity(intent);
    }
}