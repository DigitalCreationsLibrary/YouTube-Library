/*
...
*/

  public void showHome(View view){
        Intent intent = new Intent ( this, MainActivity.class);
        intent.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_SINGLE_TOP);

        startActivity(intent);
    }
}

/*
...
*/
